import pymunk
from GameObjects.Balls.Ball import Ball
from GameObjects.Balls.IspanakBall import IspanakBall
from utils import load_sprite


class HanimGobegiBall(Ball):
    def __init__(self, position):
        entity_id = "hanimgobegi_ball"

        body = pymunk.Body(25, 100)
        body.position = position

        shape = pymunk.Circle(body, 55, (0, 0))
        shape.friction = 0.5

        sprite = load_sprite("hanimgobegi.png", 95, 100)

        super().__init__(body, shape, entity_id, sprite, IspanakBall, False)