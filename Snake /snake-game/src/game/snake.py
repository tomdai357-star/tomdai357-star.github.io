# ...existing code...
class Snake:
    def __init__(self, init_pos=(100, 100), block_size=20):
        self.block_size = block_size
        # body[0] is the head
        self.body = [init_pos]
        # default direction: right
        self.direction = (self.block_size, 0)

    @property
    def head(self):
        return self.body[0]

    def move(self):
        x, y = self.head
        dx, dy = self.direction
        new_head = (x + dx, y + dy)
        self.body.insert(0, new_head)
        # remove tail
        self.body.pop()

    def grow(self):
        # Insert a copy of the current head so the snake length increases by 1
        self.body.insert(0, self.head)

    def set_direction(self, dx, dy):
        # don't allow reversing directly when length > 1
        if len(self.body) > 1 and (dx, dy) == (-self.direction[0], -self.direction[1]):
            return
        self.direction = (dx, dy)

    def render(self, screen):
        import pygame
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], self.block_size, self.block_size)
            pygame.draw.rect(screen, (0, 255, 0), rect)
# ...existing code...