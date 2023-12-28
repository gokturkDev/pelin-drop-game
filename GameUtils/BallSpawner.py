import pygame
from GameObjects.Balls.LahmacunBall import LahmacunBall
from GameObjects.Balls.MagnolyaBall import MagnolyaBall
from GameObjects.Balls.MucverBall import MucverBall
from GameObjects.Balls.ZeytinBall import ZeytinBall

from constants import SCREEN_SIZE
import random


class BallSpawner:

    def __init__(self):
        self.x = 0
        self.spawn_cooldown = 1000
        self.last_spawn = pygame.time.get_ticks()

    def update_position(self, x):
        self.x = x

    def draw(self, screen):
        pygame.draw.line(screen, pygame.Color("red"), (self.x, 20), (self.x, SCREEN_SIZE[1]))

    def spawn_ball(self):
        now = pygame.time.get_ticks()
        if (now - self.last_spawn < self.spawn_cooldown):
            return None

        self.last_spawn = now
        rand = random.random()
        if (rand > 0.7):
            return ZeytinBall(position=(self.x, SCREEN_SIZE[1] - 20))
        elif (rand < 0.9):
            return LahmacunBall(position=(self.x, SCREEN_SIZE[1] - 20))
        elif (rand < 0.95):
            return MagnolyaBall(position=(self.x, SCREEN_SIZE[1] - 20))
        else:
            return MucverBall(position=(self.x, SCREEN_SIZE[1] - 20))