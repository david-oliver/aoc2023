#!/usr/bin/env python3

import re
import math
from collections import defaultdict

INVALID_SYMBOL = "0123456789."
GEAR_SYMBOL = "*"
gear_count = defaultdict(list)


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


def add_gear_value(value, row, col, gear_count):
    key = str(row) + "," + str(col)
    gear_count[key].append(value)


def check_if_part_number(
    grid, value, start_row, end_row, start_col, end_col, gear_count
):
    is_part_number = False
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if is_inside_grid(grid, row, col) and grid[row][col] not in INVALID_SYMBOL:
                if grid[row][col] in GEAR_SYMBOL:
                    add_gear_value(value, row, col, gear_count)
                is_part_number = True
    return is_part_number


def sum_grid_candidates(grid, gear_count):
    total = 0
    for row, grid_row in enumerate(grid):
        for find in re.finditer(r"\d+", grid_row):
            if check_if_part_number(
                grid,
                int(find.group(0)),
                row - 1,
                row + 2,
                find.start() - 1,
                find.end() + 1,
                gear_count,
            ):
                total += int(find.group(0))
    return total


def sum_gears(gear_count):
    total = 0
    for k in gear_count:
        if len(gear_count[k]) == 2:
            total += math.prod(gear_count[k])
    return total


grid = populate_grid("input.txt")
print(sum_grid_candidates(grid, gear_count))
print(sum_gears(gear_count))
