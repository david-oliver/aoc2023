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
            dice_count, colour = j.strip().split(" ")
            dice_count = int(dice_count)
            match colour:
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
    total = []
    for line in file:
        game_id = get_game_id(line.strip())
        game_data = get_game_data(line.strip())
        if validate_game_data(game_data):
            total.append(game_id)
    print(sum(total))
