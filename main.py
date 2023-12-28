from functools import partial
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


def should_quit_loop(event):
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        return True

def setup_collision_handlers_for_balls(game):
    COLLISION_TYPES = [COLLTYPE_ZEYTIN, COLLTYPE_LAHMACUN, COLLTYPE_MAGNOLYA, COLLTYPE_MUCVER, COLLTYPE_KABAK, COLLTYPE_HANIMGOBEGI, COLLTYPE_ISPANAK]
    for coltype in COLLISION_TYPES:
        handler = game.space.add_collision_handler(coltype, coltype)
        handler.post_solve = partial(game.ball_collision_handler, collision_type=coltype)

    handler = game.space.add_collision_handler(COLLTYPE_LAHMACUN, COLLTYPE_MOUSE)
    handler.pre_solve = Mouse.mouse_coll_func

def main():
    ### PyGame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    clock = pygame.time.Clock()
    running = True

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    ### Mouse
    mouse = Mouse()
    space.add(mouse.body, mouse.shape)

    ### Game Logic
    game = Game(screen=screen, space=space)

    ### Collision Handlers
    setup_collision_handlers_for_balls(game)

    should_update = True


    while running:
        for event in pygame.event.get():
            if (should_quit_loop(event)):
                running = False
                break
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