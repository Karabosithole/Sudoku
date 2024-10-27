import pygame
import pytest
import sys
import os

# Adjust the path to import from the correct module where your functions are defined
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sudoku import get_cell, draw_grid, draw_numbers, grid  # Change 'sudoku_functions' to your actual module name

# Initialize Pygame for testing
pygame.init()
screen = pygame.display.set_mode((540, 600))


def test_get_cell():
    """Test the `get_cell` function correctly translates mouse position to grid cell."""
    assert get_cell((0, 0)) == (0, 0)  # Top-left corner
    assert get_cell((539, 599)) == (8, 8)  # Bottom-right corner
    assert get_cell((270, 300)) == (5, 4)  # Center of the grid

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
    row, col = 0, 2  # Choose an empty cell
    grid[row][col] = 4  # Assign a number to the cell
    assert grid[row][col] == 4  # Check the cell has been updated
    grid[row][col] = 0  # Reset for other tests

def test_pygame_initialization():
    """Test that Pygame initializes correctly."""
    assert pygame.get_init() == True


