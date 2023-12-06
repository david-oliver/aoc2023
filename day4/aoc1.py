#!/usr/bin/env python3

import re


match_points = {
    0: 0,
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 16,
    6: 32,
    7: 64,
    8: 128,
    9: 256,
    10: 512,
}


def process_games(filename):
    points = 0
    for line in open(filename).readlines():
        all_numbers = re.findall(r"\d+", line)
        matches = set(all_numbers[1:11]).intersection(all_numbers[11:36])
        points += match_points[len(matches)]
    return points


print(process_games("input.txt"))
