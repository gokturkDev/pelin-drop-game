import pymunk
from GameObjects.Balls.Ball import Ball
from GameObjects.Balls.HanimGobegiBall import HanimGobegiBall
from utils import load_sprite


class KabakBall(Ball):
    def __init__(self, position):
        entity_id = "kabak_ball"

        body = pymunk.Body(10, 100)
        body.position = position

        shape = pymunk.Circle(body, 30, (0, 0))
        shape.friction = 0.5

        sprite = load_sprite("kabak.png", 60, 70)

        super().__init__(body, shape, entity_id, sprite, HanimGobegiBall, False)