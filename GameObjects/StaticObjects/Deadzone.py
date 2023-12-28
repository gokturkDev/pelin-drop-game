import pygame
import pymunk
from GameObjects.StaticObjects.StaticObject import StaticObject
from constants import COLLTYPE_DEADZONE, SCREEN_SIZE
from utils import flipy


class Deadzone(StaticObject):
    def __init__(self, y):
        self.y = y
        self.deadzone_line = self._create_deadzone_line()

    
    def _create_deadzone_line(self):
        shape =  pymunk.Segment(self.static_body, (0, self.y), (SCREEN_SIZE[0], self.y), 1)
        shape.friction = 1
        shape.collision_type = COLLTYPE_DEADZONE
        return shape
    
    def draw(self, screen):
        line = self.deadzone_line
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = round(pv1.x), round(flipy(pv1.y))
        p2 = round(pv2.x,), round(flipy(pv2.y))
        pygame.draw.lines(screen, pygame.Color("grey"), False, [p1, p2])

    def add_self_to_space(self, space):
        space.add(self.deadzone_line)