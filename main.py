import pygame

pygame.init() # Initialises pygame's functions and variables

WIDTH,HEIGHT = 800,600 # Screen dimensions

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) # Create the screen

is_running = True # Define a variable that tells us if the game is running

# Colours in (RED,GREEN,BLUE) form. 
BLACK = (0,0,0)
WHITE = (245,245,245)

# Constant rectangles
GROUND = pygame.rect.Rect(0,580,900,20)

while is_running: # The main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    SCREEN.fill(BLACK) # Make the entire screen black.
    pygame.draw.rect(SCREEN,WHITE,GROUND) # Draw a rectangle at the bottom of the screen.
    pygame.display.update() # Take all of the images on the screen and display them.