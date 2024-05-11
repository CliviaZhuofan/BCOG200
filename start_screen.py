import pygame
import sys

def show_start_screen(screen):
    # Constants for colors and screen dimensions
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 200, 0)
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()

    # Font setup
    start_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 36)
    instructions_font = pygame.font.Font(None, 28)  # Font for the instructions

    # Rendering text
    title_text = start_font.render("Toss Game", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

    button_text = button_font.render("Start", True, WHITE)
    button_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Creating the button surface
    button_surface = pygame.Surface((button_rect.width + 20, button_rect.height + 10))
    button_surface.fill(GREEN)
    button_surface_rect = button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Instructions text split into two lines
    instructions_line1 = "Control the ball with a mouse click to drop it on the boxes below."
    instructions_line2 = "Aim for boxes with higher values to increase your score!"
    instructions_text1 = instructions_font.render(instructions_line1, True, (0, 0, 0))
    instructions_rect1 = instructions_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    instructions_text2 = instructions_font.render(instructions_line2, True, (0, 0, 0))
    instructions_rect2 = instructions_text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))  # Adjust for the second line
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_surface_rect.collidepoint(event.pos):
                    running = False  # Break the loop to start the game
        # Drawing elements
        screen.fill(WHITE)
        screen.blit(title_text, title_rect)
        screen.blit(button_surface, button_surface_rect)
        screen.blit(button_text, button_rect)
        screen.blit(instructions_text1, instructions_rect1)  # Display the first line of instructions
        screen.blit(instructions_text2, instructions_rect2)  # Display the second line of instructions
        pygame.display.flip()
       