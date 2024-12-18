import pygame
import random

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("بازی سکه جمع کن")

black = (0, 0, 0)
dark_gray = (40, 40, 40)
light_gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)