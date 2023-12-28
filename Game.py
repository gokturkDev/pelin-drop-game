import pygame
import pymunk

from utils import flipy

class Game:

    def __init__(self, screen, space):
        self.screen = screen
        self.space = space
        self.balls = []

        self.static_lines = [
            pymunk.Segment(space.static_body, (11.0, 280.0), (407.0, 246.0), 0.0),
            pymunk.Segment(space.static_body, (407.0, 246.0), (407.0, 343.0), 0.0),
        ]
        self.space.add(*self.static_lines)
        

    
    def draw(self):
        self.screen.fill(pygame.Color("white"))
        self._draw_title()
        self._draw_static_lines()
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

    def _draw_static_lines(self):
        for line in self.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = round(pv1.x), round(flipy(pv1.y))
            p2 = round(pv2.x,), round(flipy(pv2.y))
            pygame.draw.lines(self.screen, pygame.Color("lightgray"), False, [p1, p2])

    def add_ball(self, ball):
        self.space.add(ball.body, ball.shape)
        self.balls.append(ball)