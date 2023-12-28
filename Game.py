import pygame
import pymunk
from GameObjects.Bucket import Bucket
from constants import SCREEN_SIZE

from utils import flipy

class Game:

    def __init__(self, screen, space):
        self.screen = screen
        self.space = space

        screen_x, screen_y = SCREEN_SIZE
        self.bucket = Bucket(center_position=(screen_x / 2, screen_y / 2 - 100), width=screen_x * 0.6, height=screen_y * 0.5, static_body=self.space.static_body)
        self.bucket.add_self_to_space(self.space)
        self.balls = []

        
        
    
    def draw(self):
        self.screen.fill(pygame.Color("white"))
        self._draw_title()
        self.bucket.draw(self.screen)
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
            pygame.draw.lines(self.screen, pygame.Color("grey"), False, [p1, p2])

    def add_ball(self, ball):
        self.space.add(ball.body, ball.shape)
        self.balls.append(ball)