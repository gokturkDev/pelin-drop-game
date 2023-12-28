import pygame

from constants import SCREEN_SIZE


class BallSpawner:

    def __init__(self):
        self.x = 0

    def update_position(self, x):
        self.x = x

    def draw(self, screen):
        pygame.draw.line(screen, pygame.Color("red"), (self.x, 20), (self.x, SCREEN_SIZE[1]))