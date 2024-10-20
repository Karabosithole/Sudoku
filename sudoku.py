import pygame
import time

# Initialize Pygame
pygame.init()

# Define constants
WIDTH = 540
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('Arial', 40)

# Sudoku puzzle (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def draw_grid(screen):
    block_size = WIDTH // 9
    for i in range(10):
        # Draw grid lines
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * block_size), (WIDTH, i * block_size), thickness)
        pygame.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, WIDTH), thickness)

def draw_numbers(screen, grid):
    block_size = WIDTH // 9
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                # Draw numbers
                text = FONT.render(str(grid[row][col]), True, BLACK)
                screen.blit(text, (col * block_size + 20, row * block_size + 10))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen)
        draw_numbers(screen, grid)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

