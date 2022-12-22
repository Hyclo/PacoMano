import pygame

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game dimensions
WIDTH = 640
HEIGHT = 480

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up ghost speed
ghost_speed = 1.0

# Set random variabel
gameOver = False
score = 0

def gameLoop(ghost_speed, score):

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the player
    player_image = pygame.image.load("pacman.png").convert()
    player_rect = player_image.get_rect()

    # Set up the ghosts
    ghost_image = pygame.image.load("ghost.png").convert()
    ghost_rect = ghost_image.get_rect()
    ghost_rect.x = 580
    ghost_rect.y = 420

    # Set up the dots
    dot_image = pygame.image.load("dot.png").convert()
    dots = []
    for i in range(10):
        dot = dot_image.get_rect()
        dot.x = i * 60
        dot.y = i * 40
        dots.append(dot)

    # Set up the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            player_rect.x += 5
        if keys[pygame.K_UP]:
            player_rect.y -= 5
        if keys[pygame.K_DOWN]:
            player_rect.y += 5

        # Move the ghost
        
        if player_rect.x > ghost_rect.x:
            ghost_rect.x += ghost_speed
        if player_rect.x < ghost_rect.x:
            ghost_rect.x -= ghost_speed
        if player_rect.y > ghost_rect.y:
            ghost_rect.y += ghost_speed
        if player_rect.y < ghost_rect.y:
            ghost_rect.y -= ghost_speed
        if ghost_rect.right > WIDTH:
            ghost_rect.left = 0

        # Check for collisions
        if player_rect.colliderect(ghost_rect):
            print("You lose!")
            running = False

        # Check for dot collection
        for dot in dots:
            if player_rect.colliderect(dot):
                dots.remove(dot)

        # Check for win --------------------------------------------------------
        if not dots:
            print("You win!")
            score += 1
            print(score)
            ghost_speed += 0.2
            gameLoop(ghost_speed, score)
            # running = False

        # Draw the screen
        screen.fill(BLACK)
        screen.blit(player_image, player_rect)
        screen.blit(ghost_image, ghost_rect)
        for dot in dots:
            screen.blit(dot_image, dot)
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)
if gameOver == False:
    gameLoop(ghost_speed, score)
# Shut down Pygame
pygame.quit()
