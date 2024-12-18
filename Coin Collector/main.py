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

player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 20
player_speed = 10

obstacle_width = 120
obstacle_height = 30
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_increase = 0.3

coin_radius = 20
coin_x = random.randint(0, screen_width - obstacle_width)
coin_y = -obstacle_height
coin_speed = 3
coin_speed_increase = 0.3