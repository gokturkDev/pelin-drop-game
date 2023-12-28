import pymunk
from constants import *

class Mouse:
    def __init__(self):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.shape = pymunk.Circle(self.body, 3, (0, 0))
        self.shape.collision_type = COLLTYPE_MOUSE

    def mouse_coll_func(arbiter, space, data):
        return None
