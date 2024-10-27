import pygame
import time

# Initialize Pygame
pygame.init()

# Define constants
WIDTH = 540  # Width of the game window
HEIGHT = 600  # Height of the game window
WHITE = (255, 255, 255)  # Color for the background
BLACK = (0, 0, 0)  # Color for grid and text
FONT = pygame.font.SysFont('Arial', 40)  # Font for displaying numbers

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

selected_cell = None  # Track the currently selected cell

def draw_grid(screen):
    """
    Draws the Sudoku grid lines on the screen.
    
    Args:
        screen (pygame.Surface): The screen surface where the grid is drawn.
    """
    block_size = WIDTH // 9
    for i in range(10):
        # Draw grid lines with different thicknesses for sub-grids
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * block_size), (WIDTH, i * block_size), thickness)
        pygame.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, WIDTH), thickness)

def draw_numbers(screen, grid):
    """
    Draws numbers from the grid onto the screen.
    
    Args:
        screen (pygame.Surface): The screen surface where numbers are drawn.
        grid (list of list of int): The Sudoku puzzle grid with numbers.
    """
    block_size = WIDTH // 9
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                # Render and draw each number in its cell
                text = FONT.render(str(grid[row][col]), True, BLACK)
                screen.blit(text, (col * block_size + 20, row * block_size + 10))

def get_cell(mouse_pos):
    """
    Gets the row and column of the cell selected by mouse click.
    
    Args:
        mouse_pos (tuple of int): The x and y coordinates of the mouse click.
    
    Returns:
        tuple of int: The (row, col) of the selected cell, or (-1, -1) if out of bounds.
    """
    x, y = mouse_pos
    block_size = 60  # Each cell is 60 pixels
    
    # Check for out-of-bounds coordinates
    if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:  # Check against the overall window size
        return -1, -1

    col = x // block_size
    row = y // block_size

    return row, col  # Return (row, col) as expected


# Placeholder function for checking if a number is in a row
def is_number_in_row():
    """
    Checks if a number is in a specific row.
    
    Returns:
        bool: True if number is found in the row, False otherwise.
    """
    return ""  # Placeholder, needs implementation

def main():
    """
    Main function to run the Sudoku game. Initializes the game window,
    handles events, and updates the display.
    """
    global selected_cell
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    running = True
    while running:
        # Fill the screen with a white background
        screen.fill(WHITE)
        draw_grid(screen)
        draw_numbers(screen, grid)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Detect mouse click to select a cell
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_cell = get_cell(mouse_pos)

            # Check for number input (1-9) when a cell is selected
            if event.type == pygame.KEYDOWN:
                if selected_cell:
                    row, col = selected_cell
                    # Accept only number keys (1-9)
                    if event.key in range(pygame.K_1, pygame.K_9 + 1):
                        grid[row][col] = event.key - pygame.K_0  # Convert key to number

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
