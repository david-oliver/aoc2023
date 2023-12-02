from aoc2 import modify_number_string, find_calibration

import pytest


@pytest.mark.parametrize(
    "input_string, output",
    [
        ("gtwonejcncdlhpsxjrxnmpvfgtdrcdtd2nm", "gt2o1ejcncdlhpsxjrxnmpvfgtdrcdtd2nm"),
        ("5sixczhncsix2qcqsevenfive4", "5s6xczhncs6x2qcqs7nf5e4"),
        ("71oneone", "71o1eo1e"),
        ("5lmctnqtqc49eightnt", "5lmctnqtqc49e8tnt"),
    ],
)
def test_modify_number_string(input_string, output):
    assert modify_number_string(input_string) == output


def test_find_calibration():
    assert find_calibration("input_test1.txt") == [23, 27, 94]
