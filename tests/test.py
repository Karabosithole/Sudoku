import pygame
import pytest
import sys
import os
import copy

# Adjust the path to import from the correct module where your functions are defined
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sudoku import get_cell, draw_grid, draw_numbers, grid  # Change 'sudoku' to your actual module name

# Initialize Pygame for testing
pygame.init()
screen = pygame.display.set_mode((540, 600))

def test_get_cell_valid_coordinates():
    """Test the `get_cell` function with valid coordinates."""
    # Valid cell coordinates
    assert get_cell((0, 0)) == (0, 0)          # Top-left corner
    assert get_cell((59, 59)) == (0, 0)        # Inside the first cell
    assert get_cell((60, 60)) == (1, 1)        # Inside the second cell
    assert get_cell((539, 539)) == (8, 8)      # Bottom-right corner (last cell)

    # Out of bounds coordinates
    assert get_cell((540, 540)) == (-1, -1)    # Just outside the grid
    assert get_cell((600, 600)) == (-1, -1)    # Well outside the grid
    assert get_cell((-1, -1)) == (-1, -1)      # Negative coordinates

def test_get_cell_center_coordinates():
    """Test the `get_cell` function with center coordinates."""
    assert get_cell((30, 30)) == (0, 0)  # Center of the first cell
    assert get_cell((330, 330)) == (5, 5)  # Center of the sixth cell

def test_get_cell_out_of_bounds():
    """Test the `get_cell` function with out-of-bounds coordinates."""
    assert get_cell((-1, -1)) == (-1, -1)  # Out of bounds top-left
    assert get_cell((540, 600)) == (-1, -1)  # Out of bounds bottom-right
    assert get_cell((500, -10)) == (-1, -1)  # Out of bounds top-right
    assert get_cell((-10, 500)) == (-1, -1)  # Out of bounds bottom-left

def test_get_cell_edge_cases():
    """Test edge cases for getting cells at grid boundaries."""
    assert get_cell((0, 300)) == (5, 0)  # Left edge center of the middle row
    assert get_cell((540, 300)) == (-1, -1)  # Right edge
    assert get_cell((270, 0)) == (0, 4)  # Top edge center of the middle column
    assert get_cell((270, 600)) == (-1, -1)  # Bottom edge

def test_draw_grid():
    """Test that `draw_grid` runs without errors."""
    try:
        draw_grid(screen)
    except Exception as e:
        pytest.fail(f"draw_grid() raised an exception: {e}")

def test_draw_numbers():
    """Test that `draw_numbers` renders correctly without errors."""
    try:
        draw_numbers(screen, grid)
    except Exception as e:
        pytest.fail(f"draw_numbers() raised an exception: {e}")

def test_update_cell():
    """Test cell update in the grid to ensure cells can be updated properly."""
    local_grid = copy.deepcopy(grid)  # Use a copy of the grid
    row, col = 0, 2  # Choose an empty cell
    local_grid[row][col] = 4  # Assign a number to the cell
    assert local_grid[row][col] == 4  # Check the cell has been updated
    local_grid[row][col] = 0  # Reset for other tests

def test_pygame_initialization():
    """Test that Pygame initializes correctly."""
    assert pygame.get_init() == True

def test_draw_grid_lines():
    """Test that grid lines are drawn without errors."""
    try:
        draw_grid(screen)
    except Exception as e:
        pytest.fail(f"draw_grid() raised an exception: {e}")

def test_draw_numbers_with_empty_grid():
    """Test that `draw_numbers` renders correctly with an empty grid."""
    empty_grid = [[0] * 9 for _ in range(9)]  # Create an empty grid
    try:
        draw_numbers(screen, empty_grid)  # Should run without errors
    except Exception as e:
        pytest.fail(f"draw_numbers() raised an exception with an empty grid: {e}")

def test_cell_out_of_bounds():
    """Test that getting a cell with out-of-bounds coordinates returns invalid values."""
    assert get_cell((-10, -10)) == (-1, -1)  # Out of bounds
    assert get_cell((540, 600)) == (-1, -1)  # Out of bounds

# Run the tests
if __name__ == "__main__":
    pytest.main()
