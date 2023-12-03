#!/usr/bin/env python3

import re


INVALID_SYMBOL = "0123456789."


def populate_grid(filename):
    grid = []
    for line in open(filename).readlines():
        grid.append(line.strip())
    return grid


def is_inside_grid(grid, row, col):
    in_grid = True
    if row < 0 or row >= len(grid):
        in_grid = False
    elif col < 0 or col >= len(grid[row]):
        in_grid = False
    return in_grid


def check_if_part_number(grid, start_row, end_row, start_col, end_col):
    is_part_number = False
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if is_inside_grid(grid, row, col) and grid[row][col] not in INVALID_SYMBOL:
                is_part_number = True
    return is_part_number


def sum_grid_candidates(grid):
    total = 0
    for row, grid_row in enumerate(grid):
        for find in re.finditer(r"\d+", grid_row):
            if check_if_part_number(
                grid, row - 1, row + 2, find.start() - 1, find.end() + 1
            ):
                total += int(find.group(0))
    return total


grid = populate_grid("input.txt")
print(sum_grid_candidates(grid))
