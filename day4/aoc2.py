#!/usr/bin/env python3

import re

from collections import defaultdict


game_count = defaultdict(int)


def import_games(filename):
    games = []
    for line in open(filename).readlines():
        games.append(line.strip())
    return games


def process_games(games, game_count):
    for row, line in enumerate(games):
        all_numbers = re.findall(r"\d+", line)
        matches = len(set(all_numbers[1:11]).intersection(all_numbers[11:36]))
        for i in range(row + 1, row + matches + 1):
            game_count.setdefault(row, 1)
            game_count.setdefault(i, 1)
            game_count[i] += game_count[row]
    return sum(game_count.values()) + 1


games = import_games("input.txt")
print(process_games(games, game_count))
