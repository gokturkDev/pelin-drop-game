import pygame
import pymunk

from utils import flipy


class Bucket:

    def __init__(self, center_position, width, height, static_body):

        self.center_position = center_position
        self.width = width
        self.height = height
        self.static_body = static_body # pymunk.Space.static_body; Conveinence for creating static bodies. Specific to the space it is created for.

        ## 2k Base, 4k line
        self.base_width = round(width  * 0.4) 
        self.line_width = round(width * 0.2)
        self.base_buffer = 10 # There is very little space between the base and the lines, so we need to add a buffer to make sure the ball doesn't get stuck

        self.lines = [
            self._create_left_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_base_line(),
            self._create_right_line()
        ]
        

    def _create_left_line(self,):
        start_position = (self.center_position[0] - (self.line_width + self.base_width / 2) ,
                            self.center_position[1] + self.height / 2)
        end_position = (self.center_position[0] - (self.base_width / 2),
                            self.center_position[1] - self.height / 2)
        shape =  pymunk.Segment(self.static_body, start_position, end_position, 1)
        shape.friction = 0.99
        return shape
    
    def _create_base_line(self):

        start_position = (self.center_position[0] - self.base_width / 2,
                            self.center_position[1] - self.height / 2)
        end_position = (self.center_position[0] + self.base_width / 2,
                            self.center_position[1] - self.height / 2)
        shape = pymunk.Segment(self.static_body, start_position, end_position, 1)
        shape.friction = 0.99
        return shape
    
    def _create_right_line(self):
        start_position = (self.center_position[0] + self.base_width / 2,
                            self.center_position[1] - self.height / 2)
        end_position = (self.center_position[0] + (self.line_width + self.base_width / 2),
                            self.center_position[1] + self.height / 2)
        shape = pymunk.Segment(self.static_body, start_position, end_position, 1)
        shape.friction = 0.99
        return shape
    

    def draw(self, screen):
        for line in self.lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = round(pv1.x), round(flipy(pv1.y))
            p2 = round(pv2.x,), round(flipy(pv2.y))
            pygame.draw.lines(screen, pygame.Color("grey"), False, [p1, p2])

    def add_self_to_space(self, space):
        for line in self.lines:
            space.add(line)