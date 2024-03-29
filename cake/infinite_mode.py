import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GIRL_WIDTH, GIRL_HEIGHT = 50, 50
GIRL_SPEED = 5

WHITE = (255, 255, 255)
PINK = (255, 204, 153)


game_state = "start_menu"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cake Stepping Game")

girl_x = SCREEN_WIDTH // 2  # Initial position (centered)

def draw_start_menu():
    screen.fill(WHITE)
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Cake Stepping Game', True, (0, 0, 0))
    start_button = font.render('Start', True, (0, 0, 0))
    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - title.get_height() // 2))
    screen.blit(start_button, (SCREEN_WIDTH // 2 - start_button.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

def handle_input():
    global game_state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:  # If Enter key is pressed (start button)
        game_state = "timed_mode"  # or "infinite_mode"


def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == "start_menu":
            draw_start_menu()
            handle_input()
        elif game_state == "timed_mode":
            # Implement timed mode gameplay
            pass
        elif game_state == "infinite_mode":
            # Implement infinite mode gameplay
            pass

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()