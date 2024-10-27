import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH = 540  # Width of the game window
HEIGHT = 600  # Height of the game window
WHITE = (255, 255, 255)  # Color for the background
BLACK = (0, 0, 0)  # Color for grid and text
FONT = pygame.font.SysFont('Arial', 40)  # Font for displaying numbers

def generate_sudoku():
    """Generates a random Sudoku puzzle."""
    base = 3
    side = base * base

    # Randomly shuffle numbers
    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s))
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # Generate an empty grid
    grid = [[0 for _ in range(side)] for _ in range(side)]

    for r in range(base):
        for c in range(base):
            for i in range(1, base * base + 1):
                grid[pattern(r, c)][pattern(r, i - 1)] = nums[i - 1]

    # Remove some numbers to create the puzzle
    squares = side * side
    for p in random.sample(range(squares), squares // 2):
        grid[p // side][p % side] = 0

    return grid

# Generate a random Sudoku puzzle
grid = generate_sudoku()

selected_cell = None  # Track the currently selected cell

def draw_grid(screen):
    """Draws the Sudoku grid lines on the screen."""
    block_size = WIDTH // 9
    for i in range(10):
        thickness = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * block_size), (WIDTH, i * block_size), thickness)
        pygame.draw.line(screen, BLACK, (i * block_size, 0), (i * block_size, WIDTH), thickness)

def draw_numbers(screen, grid):
    """Draws numbers from the grid onto the screen."""
    block_size = WIDTH // 9
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                text = FONT.render(str(grid[row][col]), True, BLACK)
                screen.blit(text, (col * block_size + 20, row * block_size + 10))

def get_cell(mouse_pos):
    """Gets the row and column of the cell selected by mouse click."""
    x, y = mouse_pos
    block_size = WIDTH // 9
    if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
        return -1, -1

    col = x // block_size
    row = y // block_size
    return row, col

def is_valid_move(row, col, number):
    """
    Checks if placing the number at (row, col) is valid.
    
    Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        number (int): The number to be placed in the cell.
    
    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Check the row and column for the same number
    for i in range(9):
        if grid[row][i] == number or grid[i][col] == number:
            return False

    # Check the 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == number:
                return False

    return True  # The move is valid

def main():
    """Main function to run the Sudoku game."""
    global selected_cell
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen)
        draw_numbers(screen, grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_cell = get_cell(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if selected_cell:
                    row, col = selected_cell
                    if event.key in range(pygame.K_1, pygame.K_9 + 1):
                        number = event.key - pygame.K_0  # Convert key to number
                        if is_valid_move(row, col, number):  # Validate the move
                            grid[row][col] = number  # Place the number if valid

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
