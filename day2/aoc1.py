#!/usr/bin/env python3

RED = 12
GREEN = 13
BLUE = 14


def get_game_id(inputs):
    fields = inputs.split(":")
    return int(fields[0].removeprefix("Game "))


def get_game_data(inputs):
    fields = inputs.split(":")
    return fields[1]


def validate_game_data(data):
    valid = True
    fields = data.split(";")
    for k in fields:
        colours = k.split(",")
        for j in colours:
            counts = j.split(" ")
            dice_count = int(counts[1])
            match counts[2].lower():
                case "red":
                    if dice_count > RED:
                        valid = False
                case "blue":
                    if dice_count > BLUE:
                        valid = False
                case "green":
                    if dice_count > GREEN:
                        valid = False
    return valid


with open("input.txt") as file:
    total = 0
    for line in file:
        game_id = get_game_id(line.strip())
        game_data = get_game_data(line.strip())
        valid_game = validate_game_data(game_data)
        if valid_game:
            total += game_id
    print(total)
