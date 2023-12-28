from constants import SCREEN_SIZE


def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y + SCREEN_SIZE[1]