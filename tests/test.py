import pytest
import random
from sudoku import generate_complete_grid, is_valid_move, generate_sudoku, has_unique_solution, remove_numbers

def test_generate_complete_grid():
    grid = generate_complete_grid()
    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)
    assert all(num in range(1, 10) for row in grid for num in row)

def test_is_valid_move():
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    assert is_valid_move(grid, 0, 2, 4) == True
    assert is_valid_move(grid, 0, 2, 5) == False
    assert is_valid_move(grid, 0, 2, 6) == False

def test_remove_numbers():
    grid = generate_complete_grid()
    original_grid = [row[:] for row in grid]
    remove_numbers(grid)
    assert has_unique_solution(grid) == True
    assert grid != original_grid

# def test_has_unique_solution():
    # grid_with_unique_solution = generate_complete_grid()
    # assert has_unique_solution(grid_with_unique_solution) == True
    
    # grid_with_no_unique_solution = [row[:] for row in grid_with_unique_solution]
    # grid_with_no_unique_solution[0][0] = 1
    # assert has_unique_solution(grid_with_no_unique_solution) == False

def test_generate_sudoku():
    grid = generate_sudoku()
    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)
    assert has_unique_solution(grid) == True

if __name__ == "__main__":
    pytest.main()
