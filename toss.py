import pygame
import sys
import random
from box_utils import shuffle_boxes
from start_screen import show_start_screen

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
BALL_SPEED = 5
GRAVITY = 0.5  # Gravity for vertical falling
BOX_WIDTH = 40
BOX_HEIGHT = 200
SCORE_REGION_HEIGHT = 50
TOTAL_BALLS = 10

# Colors
WHITE = (255, 255, 255)
BOX_COLORS = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(20)]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toss Game")

# Display the start screen and wait for user to start the game
show_start_screen(screen)

# Initialize ball properties
ball_x = SCREEN_WIDTH // 2
ball_y = BALL_RADIUS
ball_velocity_x = BALL_SPEED
ball_velocity_y = 0
ball_moving_horizontally = True

# Initialize score and balls remaining
score = 0
balls_remaining = TOTAL_BALLS

# Initially shuffle boxes
boxes = shuffle_boxes()

# Main game loop
while balls_remaining > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and ball_moving_horizontally:
            # Stop horizontal movement and start falling vertically
            ball_moving_horizontally = False
            ball_velocity_x = 0
            ball_velocity_y = BALL_SPEED

    # Ball movement
    if ball_moving_horizontally:
        ball_x += ball_velocity_x
        # Boundary collision check
        if ball_x + BALL_RADIUS > SCREEN_WIDTH or ball_x - BALL_RADIUS < 0:
            ball_velocity_x *= -1
    else:
        ball_y += ball_velocity_y
        ball_velocity_y += GRAVITY

    # Check for collision with boxes
    hit = False
    for box in boxes:
        if pygame.Rect(box).collidepoint(ball_x, ball_y):
            score += boxes.index(box) + 1  # Scoring based on box index
            balls_remaining -= 1  # Decrement ball count
            hit = True
            break

    if not ball_moving_horizontally and (ball_y >= SCREEN_HEIGHT or hit):
        # Reset ball for next toss and shuffle boxes
        ball_x = SCREEN_WIDTH // 2
        ball_y = BALL_RADIUS
        ball_velocity_x = BALL_SPEED
        ball_velocity_y = 0
        ball_moving_horizontally = True
        boxes = shuffle_boxes()

    # Draw the screen
    screen.fill(WHITE)
    pygame.draw.circle(screen, (255, 0, 0), (int(ball_x), int(ball_y)), BALL_RADIUS)
    font = pygame.font.Font(None, 24)  # Font for box numbers
    for index, (box, color) in enumerate(zip(boxes, BOX_COLORS)):
        pygame.draw.rect(screen, color, box)
        # Draw number in the center of the box
        text = font.render(str(index + 1), True, (0, 0, 0))
        text_rect = text.get_rect(center=(box[0] + BOX_WIDTH // 2, box[1] + BOX_HEIGHT // 2))
        screen.blit(text, text_rect)

    # Display score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH - 150, 10))
    
    # Display remaining balls
    balls_text = font.render(f"Balls left: {balls_remaining}", True, (0, 0, 0))
    screen.blit(balls_text, (10, 50))

    pygame.display.flip()

# Clean up
pygame.quit()