# ...existing code...
class Food:
    def __init__(self, screen_width=640, screen_height=480, block_size=20):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.position = self.spawn_food()

    def spawn_food(self):
        import random
        x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
        y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
        self.position = (x, y)   # ensure self.position is updated when called
        return self.position

    def get_position(self):
        return self.position

    def reset_food(self):
        self.position = self.spawn_food()

    def render(self, screen):
        import pygame
        # draw food as a red square centered on its grid position
        rect = pygame.Rect(self.position[0], self.position[1], self.block_size, self.block_size)
        pygame.draw.rect(screen, (255, 0, 0), rect)
# ...existing code...