from functools import partial
import pygame
import pymunk
from Game import Game
from GameLoop.process_input import process_input
from GameLoop.update import update
from GameObjects.StaticObjects.Deadzone import Deadzone
from constants import *
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

def setup_collision_handler_for_balls(game):
    handler = game.space.add_collision_handler(COLLTYPE_BALL, COLLTYPE_BALL)
    handler.post_solve = game.ball_collision_handler

def setup_collision_handler_for_deadzone(game):
    handler = game.space.add_collision_handler(COLLTYPE_DEADZONE, COLLTYPE_BALL)
    handler.post_solve = game.deadzone_collision_handler

def display_game_over(screen):
    screen.fill(pygame.Color("white"))
    font = pygame.font.Font(None, 16)
    text = """GAME OVER"""
    text_surface = font.render(text, True, pygame.Color("black"))
    text_rect = text_surface.get_rect(center=(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2))
    screen.blit(text_surface, text_rect)



def main():
    ### PyGame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    clock = pygame.time.Clock()
    running = True

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    ### Game Logic
    game = Game(screen=screen, space=space)
    deadzone = Deadzone(y=0, static_body=space.static_body)
    deadzone.add_self_to_space(space)

    ### Collision Handlers
    setup_collision_handler_for_balls(game)
    setup_collision_handler_for_deadzone(game)



    while running:
        if (game.game_ended):
            display_game_over(screen)
            if (pygame.event.peek(pygame.MOUSEBUTTONDOWN)):
                break
        else:
            for event in pygame.event.get():
                if (should_quit_loop(event)):
                    running = False
                    break
                process_input(event, game)
            time_step_forward(space)
            
            update(game, clock)

            render(game)
       
        ### Flip screen
        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))

    pygame.quit()
    main()

if __name__ == '__main__':
    main()