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

selected_cell = None  # To keep track of the selected cell

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

def get_cell(mouse_pos):
    x, y = mouse_pos
    block_size = WIDTH // 9
    col = x // block_size
    row = y // block_size
    return row, col

def main():
    global selected_cell
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
            
            # Get mouse click position to select a cell
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_cell = get_cell(mouse_pos)

            # Check for number input
            if event.type == pygame.KEYDOWN:
                if selected_cell:
                    row, col = selected_cell
                    # Only accept numbers 1-9
                    if event.key in range(pygame.K_1, pygame.K_9):
                        grid[row][col] = event.key - pygame.K_0  # Convert key to number (1-9)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
