import pygame

pygame.init() # Initialises pygame's functions and variables

WIDTH,HEIGHT = 800,600 # Screen dimensions

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) # Create the screen

is_running = True # Define a variable that tells us if the game is running

# Colours in (RED,GREEN,BLUE) form. 
BLACK = (0,0,0)
WHITE = (245,245,245)

# Rectangle definitions in (Position X, Position Y, length X, length Y) form.
GROUND = pygame.rect.Rect(0,580,900,20)

# Player
PLAYER_IMAGE = pygame.image.load("images/player.png") # Loads an image
PLAYER_RECT = PLAYER_IMAGE.get_rect() # Creates a rectangle from the image
PLAYER_RECT.midleft = ((400,564)) # Sets the starting position of the player
K_LEFT_DOWN = False
K_RIGHT_DOWN = False

while is_running: # The main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if the X is pressed
            exit()
        if event.type == pygame.KEYDOWN: # Checks what buttons have been pressed
            if event.key == pygame.K_LEFT: # Checks if left key pressed
                K_LEFT_DOWN = True
            if event.key == pygame.K_RIGHT: # Checks if right key pressed
                K_RIGHT_DOWN = True
        if event.type == pygame.KEYUP: # Checks what buttons are not pressed anymore
            if event.key == pygame.K_LEFT: 
                K_LEFT_DOWN = False
            if event.key == pygame.K_RIGHT:
                K_RIGHT_DOWN = False

    # Player movement
    if K_LEFT_DOWN:
        PLAYER_RECT.x -= 1
    if K_RIGHT_DOWN:
        PLAYER_RECT.x += 1
    

    SCREEN.fill(BLACK) # Make the entire screen black.
    pygame.draw.rect(SCREEN,WHITE,GROUND) # Draw a rectangle at the bottom of the screen.

    SCREEN.blit(PLAYER_IMAGE,PLAYER_RECT)

    pygame.display.update() # Take all of the images on the screen and display them.