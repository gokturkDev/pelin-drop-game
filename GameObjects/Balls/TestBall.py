import pymunk
from GameObjects.Balls.Ball import Ball
from constants import COLLTYPE_BALL


class TestBall(Ball):
    def __init__(self, position):
        self.body = pymunk.Body(10, 100)
        self.body.position = position

        self.shape = pymunk.Circle(self.body, 10, (0, 0))
        self.shape.friction = 0.5
        self.shape.collision_type = COLLTYPE_BALL