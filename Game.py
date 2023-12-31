import pygame
import pymunk
from GameObjects.StaticObjects.Bucket import Bucket
from GameObjects.StaticObjects.Deadzone import Deadzone
from GameUtils.BallSpawner import BallSpawner
from constants import SCREEN_SIZE

from utils import flipy

class Game:

    def __init__(self, screen, space):
        self.screen = screen
        self.space = space

        screen_x, screen_y = SCREEN_SIZE

        self.bucket = Bucket(center_position=(screen_x / 2, screen_y / 2 - 100), width=screen_x * 0.6, height=screen_y * 0.5, static_body=self.space.static_body)
        self.bucket.add_self_to_space(self.space)
        self.balls = []
        self.ball_spawner = BallSpawner()
        
        self.game_ended = False
        self.game_won = False
        
    
    def draw(self):
        self.screen.fill(pygame.Color("white"))
        self._draw_title()
        self.bucket.draw(self.screen)
        self.ball_spawner.draw(self.screen)
        for ball in self.balls:
            ball.draw(self.screen)

    def _draw_title(self):
        font = pygame.font.Font(None, 16)
        text = """Yemekleri Düşürmeden Ispanağa Tamamla! <3"""
        y = 5
        for line in text.splitlines():
            text = font.render(line, 1, pygame.Color("black"))
            self.screen.blit(text, (5, y))
            y += 10


    def _draw_static_lines(self):
        for line in self.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = round(pv1.x), round(flipy(pv1.y))
            p2 = round(pv2.x,), round(flipy(pv2.y))
            pygame.draw.lines(self.screen, pygame.Color("grey"), False, [p1, p2])

    def add_ball(self, ball):
        self.space.add(ball.body, ball.shape)
        self.balls.append(ball)

    def remove_ball(self, ball):
        self.space.remove(ball.body, ball.shape)
        self.balls.remove(ball)


    def find_ball_by_shape(self, shape):
        return self.find_ball_by_coordinates(shape.body.position.x, shape.body.position.y)

    def find_ball_by_coordinates(self, x, y):
        for ball in self.balls:
            if ball.body.position.x == x and ball.body.position.y == y:
                return ball
        return None

    def ball_collision_handler(self, arbiter, space, data):
        ball1, ball2 = self.find_ball_by_shape(arbiter.shapes[0]), self.find_ball_by_shape(arbiter.shapes[1])
        if ball1 is None or ball2 is None:
            return
        
        if ball1.entity_id == ball2.entity_id:

            if (ball1.next_ball_class is not None):
                self.remove_ball(ball1)
                self.remove_ball(ball2)

                new_ball_position = ((ball1.body.position.x + ball2.body.position.x) / 2, (ball1.body.position.y + ball2.body.position.y) / 2)

                new_ball = ball1.next_ball_class(new_ball_position)
                impulse = arbiter.total_impulse.x, arbiter.total_impulse.y * -1
                new_ball.body.apply_impulse_at_local_point(impulse, (0, 0))
                
                self.add_ball(new_ball)
            else:
                self.game_ended = True
                self.game_won = ball1.is_winning_ball

    def deadzone_collision_handler(self, arbiter, space, data):
        self.game_ended = True
        self.game_won = False