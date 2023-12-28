import pygame
import pymunk
from GameObjects.Ball import Ball

from constants import X, Y
from utils import flipy


def process_input(event, game):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        p = event.pos[X], flipy(event.pos[Y])
        ball = Ball(position=p)
        game.add_ball(ball)
       
       
       
        