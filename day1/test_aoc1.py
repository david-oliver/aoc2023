from aoc1 import append_first_last_digit, find_calibration

import pytest


@pytest.mark.parametrize(
    "input_string, output",
    [
        ("gtwonejcncdlhpsxjrxnmpvfgtdrcdtd2nm", 22),
        ("5sixczhncsix2qcqsevenfive4", 54),
        ("71oneone", 71),
        ("5lmctnqtqc49eightnt", 59),
    ],
)
def test_append_first_last_digit(input_string, output):
    assert append_first_last_digit(input_string) == output


def test_find_calibration():
    assert find_calibration("input_test1.txt") == [33, 81, 94]
