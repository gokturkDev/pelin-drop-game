import math
import os
import pygame
import pymunk
from GameObjects.Balls.Ball import Ball
from constants import COLLTYPE_BALL, COLLTYPE_LAHMACUN
from utils import flipy, load_sprite


class LahmacunBall(Ball):
    def __init__(self, position):
        self.entity_id = "lahmacun_ball"

        self.body = pymunk.Body(10, 100)
        self.body.position = position

        self.shape = pymunk.Circle(self.body, 30, (0, 0))
        self.shape.friction = 0.5
        self.shape.collision_type = COLLTYPE_LAHMACUN

        self.sprite = load_sprite("lahmacun.png", 60, 70)