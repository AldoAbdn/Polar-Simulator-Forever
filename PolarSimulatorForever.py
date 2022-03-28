import imp
import sys, pygame
from pygame.locals import * # Needed for Key Constants
pygame.init() # Initializes Pygame

# Declarations
size = width, height = 320, 240 # Defines Windows Size
speed = [0, 0] # X and Y Speeds
black = 0, 0, 0 # Represents black colour as RGB

# Sets Windows Size
screen = pygame.display.set_mode(size)

# Creates ball sprite
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# Game Loop
while 1:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    # Handle Key Presses
    keys = pygame.key.get_pressed()
    # Handle Up
    if keys[K_UP] or keys[K_w]:
        speed[1] = -1
        ballrect = ballrect.move(speed)

    # Draw to Screen
    screen.fill(black)
    screen.blit(ball, ballrect)

    # Updates Display
    pygame.display.flip() 
