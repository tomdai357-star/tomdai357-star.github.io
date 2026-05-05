def check_collisions(snake, food):
    if snake.head == food.position:
        return True
    return False

def update_score(score):
    return score + 1

def reset_game(snake, food):
    snake.reset()
    food.spawn_food()