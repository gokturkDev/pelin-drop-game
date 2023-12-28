import math
import pygame
import pymunk

from constants import COLLTYPE_BALL
from utils import flipy


class Ball:

    def __init__(self, body, shape):
       self.entity_id = "ball"
       self.body = body
       self.shape = shape
       self.shape.collision_type = COLLTYPE_BALL
       self.sprite = None

    def draw(self, screen):
        if (self.sprite is None):
            raise Exception("Abstract Class Ball cannot be drawn")
        p = pymunk.Vec2d(self.body.position.x, flipy(self.body.position.y))
        angle_degrees = math.degrees(self.shape.body.angle)
        rotated_sprite= pygame.transform.rotate(self.sprite, angle_degrees)
        offset = pymunk.Vec2d(*rotated_sprite.get_size()) / 2
        p = p - offset

        screen.blit(rotated_sprite, (round(p.x), round(p.y)))

    def debug_draw(self, screen):
        r = self.shape.radius
        v = self.body.position
        rot = self.body.rotation_vector
        p = int(v.x), int(flipy(v.y))
        p2 = p + pymunk.Vec2d(rot.x, -rot.y) * r * 0.9
        p2 = int(p2.x), int(p2.y)
        pygame.draw.circle(screen, pygame.Color("blue"), p, int(r), 2)
        pygame.draw.line(screen, pygame.Color("red"), p, p2)