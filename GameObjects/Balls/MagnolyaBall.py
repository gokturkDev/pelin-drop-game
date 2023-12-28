import pymunk
from GameObjects.Balls.Ball import Ball
from GameObjects.Balls.MucverBall import MucverBall
from utils import load_sprite


class MagnolyaBall(Ball):
    def __init__(self, position):
        entity_id = "magnolya_ball"

        body = pymunk.Body(10, 100)
        body.position = position

        shape = pymunk.Circle(body, 30, (0, 0))
        shape.friction = 0.5

        sprite = load_sprite("magnolya.png", 60, 70)

        super().__init__(body, shape, entity_id, sprite, MucverBall, False)