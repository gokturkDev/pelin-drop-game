import os
import pygame
from constants import SCREEN_SIZE


def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y + SCREEN_SIZE[1]


def load_sprite(sprite_name, width, height):
    sprite_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "assets/" + sprite_name
    )
    sprite_surface = pygame.image.load(sprite_path)
    resized_surface = pygame.transform.scale(sprite_surface, (width, height))
    return resized_surface
