import imp
import sys, pygame
from pygame.locals import * # Needed for Key Constants
pygame.init() # Initializes Pygame

# Declarations
size = width, height = 640, 480 # Defines Windows Size
speed = [0, 0] # X and Y Speeds
black = 0, 0, 0 # Represents black colour as RGB

# Sets Windows Size
screen = pygame.display.set_mode(size)

# Clock to cap FPS
clock = pygame.time.Clock()

# Creates ball sprite
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# Create Text Surface
font = pygame.font.SysFont(None, 24)
text = font.render('If you come at the king, you better not miss', True, (50, 50, 50))

# Game Loop
while 1:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    # Handle Key Presses
    keys = pygame.key.get_pressed()
    if keys[K_UP] or keys[K_w]: # Up
        speed = [0, -10]
        ballrect = ballrect.move(speed)
    if keys[K_DOWN] or keys[K_s]: # Down
        speed = [0, 10]
        ballrect = ballrect.move(speed)
    if keys[K_LEFT] or keys[K_a]: # Left
        speed = [-10, 0]
        ballrect = ballrect.move(speed)
    if keys[K_RIGHT] or keys[K_d]: # Right
        speed = [10, 0]
        ballrect = ballrect.move(speed)

    # Draw to Screen
    screen.fill(black)
    screen.blit(text, (150, 230))
    screen.blit(ball, ballrect)

    # Updates Display
    pygame.display.flip() 
    clock.tick(30) # Caps FPS at 30
