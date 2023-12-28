import math
import os
import pygame
import pymunk
from GameObjects.Balls.Ball import Ball
from constants import COLLTYPE_BALL
from utils import flipy, load_sprite


class LahmacunBall(Ball):
    def __init__(self, position):
        self.entity_id = "lahmacun_ball"

        self.body = pymunk.Body(10, 100)
        self.body.position = position

        self.shape = pymunk.Circle(self.body, 30, (0, 0))
        self.shape.friction = 0.5
        self.shape.collision_type = COLLTYPE_BALL

        self.sprite = load_sprite("lahmacun.png", 60, 70)

    def draw(self, screen):
        p = pymunk.Vec2d(self.body.position.x, flipy(self.body.position.y))
        # we need to rotate 180 degrees because of the y coordinate flip
        angle_degrees = math.degrees(self.shape.body.angle) + 180
        rotated_sprite= pygame.transform.rotate(self.sprite, angle_degrees)
        offset = pymunk.Vec2d(*rotated_sprite.get_size()) / 2
        p = p - offset

        screen.blit(rotated_sprite, (round(p.x), round(p.y)))
        
        super().draw(screen)
        
