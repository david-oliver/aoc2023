from aoc1 import get_game_id, get_game_data, validate_game_data

import pytest


@pytest.mark.parametrize(
    "input_string, output",
    [
        (
            "Game 27: 1 blue, 5 red, 5 green; 11 blue, 7 red, 5 green; 8 blue, 7 green, 4 red; 3 green, 3 blue; 14 green, 1 blue",
            27,
        ),
        (
            "Game 28: 12 green, 1 red, 1 blue; 17 green, 1 red, 1 blue; 1 red, 1 blue, 15 green",
            28,
        ),
        (
            "Game 29: 15 green, 10 blue; 6 green, 5 blue, 2 red; 19 green, 5 blue",
            29,
        ),
    ],
)
def test_get_game_id(input_string, output):
    assert get_game_id(input_string) == output


@pytest.mark.parametrize(
    "input_string, output",
    [
        (
            "Game 27: 1 blue, 5 red, 5 green; 11 blue, 7 red, 5 green; 8 blue, 7 green, 4 red; 3 green, 3 blue; 14 green, 1 blue",
            " 1 blue, 5 red, 5 green; 11 blue, 7 red, 5 green; 8 blue, 7 green, 4 red; 3 green, 3 blue; 14 green, 1 blue",
        ),
        (
            "Game 28: 12 green, 1 red, 1 blue; 17 green, 1 red, 1 blue; 1 red, 1 blue, 15 green",
            " 12 green, 1 red, 1 blue; 17 green, 1 red, 1 blue; 1 red, 1 blue, 15 green",
        ),
        (
            "Game 29: 15 green, 10 blue; 6 green, 5 blue, 2 red; 19 green, 5 blue",
            " 15 green, 10 blue; 6 green, 5 blue, 2 red; 19 green, 5 blue",
        ),
    ],
)
def test_get_game_data(input_string, output):
    assert get_game_data(input_string) == output


@pytest.mark.parametrize(
    "input_string, output",
    [
        (
            " 1 blue, 5 red, 5 green; 11 blue, 7 red, 5 green; 8 blue, 7 green, 4 red; 3 green, 3 blue; 14 green, 1 blue",
            False,
        ),
        (
            " 12 green, 1 red, 1 blue; 17 green, 1 red, 1 blue; 1 red, 1 blue, 15 green",
            False,
        ),
        (
            " 1 green, 1 blue; 6 green, 5 blue, 2 red; 1 green, 1 blue",
            True,
        ),
    ],
)
def test_validate_game_data(input_string, output):
    assert validate_game_data(input_string) == output
