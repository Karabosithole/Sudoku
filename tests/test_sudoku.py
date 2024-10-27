import pygame
import pytest
from main import get_cell, draw_grid, draw_numbers, grid

# Initialize Pygame for testing
pygame.init()
screen = pygame.display.set_mode((540, 600))

def test_get_cell():
    """Test that `get_cell` function correctly translates mouse position to grid cell."""
    assert get_cell((0, 0)) == (0, 0)  # Top-left corner
    assert get_cell((539, 599)) == (8, 8)  # Bottom-right corner
    assert get_cell((270, 300)) == (5, 4)  # Center of the grid
