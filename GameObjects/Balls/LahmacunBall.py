import pymunk
from GameObjects.Balls.Ball import Ball
from GameObjects.Balls.MagnolyaBall import MagnolyaBall
from utils import load_sprite


class LahmacunBall(Ball):
    def __init__(self, position):
        entity_id = "lahmacun_ball"

        body = pymunk.Body(10, 100)
        body.position = position

        shape = pymunk.Circle(body, 25, (0, 0))
        shape.friction = 0.5

        sprite = load_sprite("lahmacun.png", 60, 70)

        super().__init__(body, shape, entity_id, sprite, MagnolyaBall, False)