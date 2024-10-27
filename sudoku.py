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

def generate_complete_grid():
    """Generates a fully solved Sudoku grid using backtracking."""
    def is_valid_move(grid, row, col, num):
        # Check if the number is already in the row or column
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        # Check the 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if grid[r][c] == num:
                    return False
        return True

    def solve(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid_move(grid, row, col, num):
                            grid[row][col] = num
                            if solve(grid):
                                return True
                            grid[row][col] = 0  # Reset on backtrack
                    return False
        return True

    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve(grid)
    return grid

def remove_numbers(grid):
    """Removes numbers from the grid to create the puzzle while ensuring it has a unique solution."""
    attempts = 60  # Number of cells to remove
    for _ in range(attempts):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:  # Find a filled cell to remove
            row, col = random.randint(0, 8), random.randint(0, 8)
        backup = grid[row][col]  # Backup the number before removing
        grid[row][col] = 0  # Remove the number

        # Check if there is still a unique solution
        if not has_unique_solution(grid):
            grid[row][col] = backup  # Restore the number if not unique

def has_unique_solution(grid):
    """Check if the grid has a unique solution."""
    def count_solutions(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    count = 0
                    for num in range(1, 10):
                        if is_valid_move(grid, row, col, num):
                            grid[row][col] = num
                            count += count_solutions(grid)
                            grid[row][col] = 0
                        if count > 1:  # More than one solution found
                            return count
                    return count
        return 1  # Found one valid solution

    return count_solutions(grid) == 1  # Check for a unique solution

def generate_sudoku():
    """Generates a valid Sudoku puzzle."""
    full_grid = generate_complete_grid()  # Generate a full grid
    remove_numbers(full_grid)  # Create a puzzle by removing numbers
    return full_grid

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
