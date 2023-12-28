import pygame
import pymunk
from GameObjects.Ball import Ball

from constants import COLLTYPE_BALL, X, Y
from utils import flipy


def process_input(event, game):
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key in pygame.K_ESCAPE):
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        p = event.pos[X], flipy(event.pos[Y])
        ball = Ball(position=p)
       
       
       
        