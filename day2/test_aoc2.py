from aoc2 import count_game_data

import pytest


@pytest.mark.parametrize(
    "input_string, output_dict",
    [
        (
            " 1 blue, 5 red, 5 green; 11 blue, 7 red, 5 green; 8 blue, 7 green, 4 red; 3 green, 3 blue; 14 green, 1 blue",
            {"red": 7, "blue": 11, "green": 14},
        ),
        (
            " 12 green, 1 red, 1 blue; 17 green, 1 red, 1 blue; 1 red, 1 blue, 15 green",
            {"red": 1, "blue": 1, "green": 17},
        ),
        (
            " 1 green, 1 blue; 6 green, 5 blue, 2 red; 1 green, 1 blue",
            {"red": 2, "blue": 5, "green": 6},
        ),
    ],
)
def test_count_game_data(input_string, output_dict):
    assert count_game_data(input_string) == output_dict
