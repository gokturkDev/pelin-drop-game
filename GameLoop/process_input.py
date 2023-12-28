import pygame
import pymunk
from GameObjects.Balls.LahmacunBall import LahmacunBall

from constants import X, Y
from utils import flipy


def process_input(event, game):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        ball = game.ball_spawner.spawn_ball()
        if (ball):
            game.add_ball(ball)
       
       
       
        