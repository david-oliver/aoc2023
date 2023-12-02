#!/usr/bin/env python3

from math import prod
import time


def get_game_id(inputs):
    fields = inputs.split(":")
    return int(fields[0].removeprefix("Game "))


def get_game_data(inputs):
    fields = inputs.split(":")
    return fields[1]


def count_game_data(data):
    fields = data.split(";")
    min_rgb = {"red": 0, "blue": 0, "green": 0}
    for k in fields:
        colours = k.split(",")
        for j in colours:
            dice_count, colour = j.strip().split(" ")
            dice_count = int(dice_count)
            match colour.lower():
                case "red":
                    if min_rgb["red"] < dice_count:
                        min_rgb["red"] = dice_count
                case "blue":
                    if min_rgb["blue"] < dice_count:
                        min_rgb["blue"] = dice_count
                case "green":
                    if min_rgb["green"] < dice_count:
                        min_rgb["green"] = dice_count
    return min_rgb


with open("input.txt") as file:
    total = []
    for line in file:
        game_id = get_game_id(line.strip())
        game_data = get_game_data(line.strip())
        total.append(prod(count_game_data(game_data).values()))
    print(sum(total))
