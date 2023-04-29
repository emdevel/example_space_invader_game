import pygame

pygame.init() # Initialises pygame's functions and variables

WIDTH,HEIGHT = 800,600 # Screen dimensions

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT)) # Create the screen

FPS = 60
CLOCK = pygame.time.Clock()

# Colours in (RED,GREEN,BLUE) form. 
BLACK = (0,0,0)
WHITE = (245,245,245)
RED = (255,30,30)

# Rectangle definitions in (Position X, Position Y, length X, length Y) form.
GROUND = pygame.rect.Rect(0,580,900,20)

# Player
player_image = pygame.image.load("images/player.png") # Loads an image
player_rect = player_image.get_rect() # Creates a rectangle from the image
player_rect.midleft = ((400,564)) # Sets the starting position of the player
k_left_down = False
k_right_down = False

# Enemies
list_enemies = [] # Creates an empty list to store your enemies
enemy_moving_left = True
enemy_move_down = True
enemy_speed = 1
enemy_image = pygame.image.load("images/enemy.png") # Loads image of enemies
for i in range(0,4): # Creates a loop that repeats 4 times
    for j in range(0,4): # Creates a loop within the loop that repeats 4 times
        ENEMY_RECT = enemy_image.get_rect() # Creates a rectangle of the enemy
        ENEMY_RECT.topleft = ( (50+(50*i) , 40+(30*j)) ) # Repositions the enemy
        list_enemies.append(ENEMY_RECT) # Adds the enemy to the list
    
# Bullets
list_bullets = [] # Creates an empty list that will store all the bullets
bullet_image = pygame.image.load("images/bullet.png")

# Fonts
font = pygame.font.Font("fonts/game_over.ttf",40) # Gets and stores the font
win_text = font.render("YOU WIN",False,BLACK)
end_text = font.render("Press any key to end",False,WHITE)
lose_text = font.render("YOU LOSE",False,WHITE)

# Game conditions    
is_running = True # Define a variable that tells us if the game is running
has_won = False
has_lost = False


frame = 0 # Will be used to keep track of the frame
while is_running: # The main game loop
    frame+=1 # Increment frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if the X is pressed
            exit()
        if event.type == pygame.KEYDOWN: # Checks what buttons have been pressed
            if event.key == pygame.K_LEFT: # Checks if left key pressed
                k_left_down = True
            if event.key == pygame.K_RIGHT: # Checks if right key pressed
                k_right_down = True
            if event.key == pygame.K_SPACE: # Shoots when space is pressed
                list_bullets.append(pygame.rect.Rect(player_rect.x+8,player_rect.y-16,16,16)) # Creates a bullet above the player

        if event.type == pygame.KEYUP: # Checks what buttons are not pressed anymore
            if event.key == pygame.K_LEFT: 
                k_left_down = False
            if event.key == pygame.K_RIGHT:
                k_right_down = False
        
    # Logic checks
    if len(list_enemies) == 0: # Checks if enemies are alive
        is_running = False
        has_won = True

    # Player movement
    if k_left_down:
        player_rect.x -= 3
    if k_right_down:
        player_rect.x += 3
    

    # Enemy movement
    for enemy in list_enemies:
        if enemy.y >= 570: # If enemy gets below the ground, you lose the game
            has_lost = True
            is_running = False
        if enemy_moving_left:
            enemy.x+=enemy_speed
            if enemy.x > 800:
                enemy_moving_left = False
                enemy_move_down = True
    
        else:
            enemy.x-=enemy_speed
            if enemy.x <0:
                enemy_moving_left = True
                enemy_move_down = True

    if enemy_move_down:
        for enemy in list_enemies:
            enemy.y+=15
        enemy_move_down = False

    # Bullet movement
    for bullet in list_bullets:
        if bullet.y < 0: # Delete the bullets if they go above the screen
            list_bullets.remove(bullet)
        bullet.y-=3 # Move bullet up
        for enemy in list_enemies: # Check if the bullet has hit an enemy and then delete them
            if bullet.colliderect(enemy):
                list_enemies.remove(enemy)
                list_bullets.remove(bullet)
        

    # Draw everything: 

    SCREEN.fill(BLACK) # Make the entire screen black.
    pygame.draw.rect(SCREEN,WHITE,GROUND) # Draw a rectangle at the bottom of the screen.

    # Player blit
    SCREEN.blit(player_image,player_rect)

    # Enemy blit
    for enemy in list_enemies:
        SCREEN.blit(enemy_image,enemy)

    # Player blit
    for bullet in list_bullets:
        SCREEN.blit(bullet_image,bullet)


    pygame.display.update() # Take all of the images on the screen and display them.
    CLOCK.tick(FPS)

while has_won: # Write what happens when you win
    SCREEN.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if the X is pressed
            exit()
        
    SCREEN.blit(win_text,(400,400)) # Draw the text on the screen
    
    pygame.display.update()
    
while has_lost: # What happens when you lose
    SCREEN.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checks if the X is pressed
            exit()
        
    SCREEN.blit(lose_text,(300,300))
    

    pygame.display.update()
