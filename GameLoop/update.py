import pygame


def update(game, clock):
    game.ball_spawner.update_position(pygame.mouse.get_pos()[0])

    