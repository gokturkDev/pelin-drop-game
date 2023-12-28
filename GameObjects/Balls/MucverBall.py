import pymunk
from GameObjects.Balls.Ball import Ball
from GameObjects.Balls.KabakBall import KabakBall
from utils import load_sprite


class MucverBall(Ball):
    def __init__(self, position):
        entity_id = "mucver_ball"

        body = pymunk.Body(20, 100)
        body.position = position

        shape = pymunk.Circle(body, 45, (0, 0))
        shape.friction = 0.5

        sprite = load_sprite("mucver.png", 70, 80)

        super().__init__(body, shape, entity_id, sprite, KabakBall, False)