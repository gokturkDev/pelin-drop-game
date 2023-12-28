import pygame
import pymunk
from Game import Game
from GameLoop.process_input import process_input
from constants import *
from GameObjects.Mouse import Mouse
from utils import flipy


def time_step_forward(space):
    dt = 1.0 / 60.0
    for x in range(1):
        space.step(dt)

def render(game):
    game.draw()


def main():
    ### PyGame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("Arial", 16)

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    ### Mouse
    mouse = Mouse()
    space.add(mouse.body, mouse.shape)

    space.add_collision_handler(
        COLLTYPE_MOUSE, COLLTYPE_BALL
    ).pre_solve = Mouse.mouse_coll_func

    ### Game Logic
    game = Game(screen=screen, space=space)

    should_update = True


    while running:
        for event in pygame.event.get():
            process_input(event, game)
            
        if should_update:
            time_step_forward(space)

        render(game)
       
        ### Flip screen
        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))

if __name__ == '__main__':
    main()