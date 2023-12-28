import pygame

class Game:

    def __init__(self, screen, space):
        self.screen = screen
        self.space = space
        self.balls = []

    
    def draw(self):
        self.screen.fill(pygame.Color("white"))
        self._draw_title()
        for ball in self.balls:
            ball.draw(self.screen)

    def _draw_title(self):
        font = pygame.font.Font(None, 16)
        text = """LMB: Create ball
        LMB + Shift: Create many balls
        RMB: Drag to create wall, release to finish
        Space: Pause physics simulation"""
        y = 5
        for line in text.splitlines():
            text = font.render(line, 1, pygame.Color("black"))
            self.screen.blit(text, (5, y))
            y += 10


    def add_ball(self, ball):
        self.space.add(ball.body, ball.shape)
        self.balls.append(ball)