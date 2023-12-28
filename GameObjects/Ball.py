import pygame
import pymunk

from constants import COLLTYPE_BALL
from utils import flipy


class Ball:

    def __init__(self, position):
        self.body = pymunk.Body(10, 100)
        self.body.position = position

        self.shape = pymunk.Circle(self.body, 10, (0, 0))
        self.shape.friction = 0.5
        self.shape.collision_type = COLLTYPE_BALL


    def draw(self, screen):
        r = self.shape.radius
        v = self.body.position
        rot = self.body.rotation_vector
        p = int(v.x), int(flipy(v.y))
        p2 = p + pymunk.Vec2d(rot.x, -rot.y) * r * 0.9
        p2 = int(p2.x), int(p2.y)
        pygame.draw.circle(screen, pygame.Color("blue"), p, int(r), 2)
        pygame.draw.line(screen, pygame.Color("red"), p, p2)