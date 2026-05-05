# ...existing code...
import pygame
from game.snake import Snake
from game.food import Food
from game.game_logic import check_collisions, reset_game
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SPEED
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20

def load_sound(path, fallback_freq=440, duration_ms=120, volume=0.6):
    try:
        return pygame.mixer.Sound(path)
    except Exception:
        try:
            import numpy as np
            freq = 44100
            t = np.linspace(0, duration_ms/1000, int(freq * duration_ms / 1000), False)
            wave = 0.5 * np.sin(2 * np.pi * fallback_freq * t)
            arr = (wave * 32767).astype(np.int16)
            # stereo: duplicate channel
            stereo = np.column_stack([arr, arr])
            sound = pygame.sndarray.make_sound(stereo)
            sound.set_volume(volume)
            return sound
        except Exception:
            return None

def main():
    import pygame
    from game.food import Food
    # ...existing code...
    pygame.init()
    # ensure mixer is initialized (catch failures)
    try:
        pygame.mixer.init()
    except Exception:
        pass

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # try to load sound files from assets; if they don't exist, fall back gracefully
    eat_sound = load_sound("assets/sounds/eat.wav", fallback_freq=880, duration_ms=90, volume=0.5)
    gameover_sound = load_sound("assets/sounds/gameover.wav", fallback_freq=200, duration_ms=400, volume=0.7)

    snake = Snake(block_size=BLOCK_SIZE)
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
    score = 0

    # base speed and dynamic game speed (increase 5% every 10 apples)
    base_speed = SNAKE_SPEED
    game_speed = base_speed
    prev_speed_level = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # movement controls: arrows + WASD
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake.set_direction(0, -BLOCK_SIZE)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.set_direction(0, BLOCK_SIZE)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.set_direction(-BLOCK_SIZE, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.set_direction(BLOCK_SIZE, 0)

                # reset game
                elif event.key == pygame.K_r:
                    snake = Snake(block_size=BLOCK_SIZE)
                    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
                    score = 0
                    # reset speed tracking
                    game_speed = base_speed
                    prev_speed_level = 0

                # quick quit
                elif event.key == pygame.K_ESCAPE:
                    running = False

        snake.move()
        head_x, head_y = snake.head
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            # play game-over sound if available
            try:
                if gameover_sound:
                    gameover_sound.play()
            except Exception:
                pass

            try:
                font = pygame.font.Font(None, 48)
                go_surf = font.render("Game Over", True, (255, 0, 0))
                screen.blit(go_surf, (SCREEN_WIDTH // 2 - go_surf.get_width() // 2,
                                      SCREEN_HEIGHT // 2 - go_surf.get_height() // 2))
                pygame.display.flip()
                pygame.time.delay(800)
            except Exception:
                pass

            # Reset game state (same as pressing 'R')
            snake = Snake(block_size=BLOCK_SIZE)
            food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
            score = 0
            # reset speed tracking on game over
            game_speed = base_speed
            prev_speed_level = 0
            continue

        if check_collisions(snake, food):
            score += 1
            snake.grow()
            # play eat sound if available
            try:
                if eat_sound:
                    eat_sound.play()
            except Exception:
                pass
            # only reset food position
            food.reset_food()

            # --- increase speed 5% every 10 apples ---
            level = score // 10
            if level > prev_speed_level:
                prev_speed_level = level
                # multiplicative scaling
                game_speed = max(1, int(round(base_speed * (1.05 ** level))))
            # --- end speed scaling ---

        screen.fill((0, 0, 0))  # Clear the screen
        snake.render(screen)
        food.render(screen)

        # optionally draw score (small, non-invasive)
        try:
            font = pygame.font.Font(None, 24)
            score_surf = font.render(f"Score: {score}  (R to reset, Esc to quit)", True, (255,255,255))
            screen.blit(score_surf, (10, 10))
        except Exception:
            pass

        pygame.display.flip()
        # use dynamic game_speed (updated every 10 apples)
        clock.tick(game_speed)

    pygame.quit()

if __name__ == "__main__":
    main()
