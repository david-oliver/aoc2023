import re


def modify_number_string(string):
    mapping = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for k, v in mapping.items():
        string = string.replace(k, v)

    return string


def append_first_last_digit(input_string):
    digits = re.findall(r"\d", input_string)
    return int(digits[0] + digits[-1])


def find_calibration(filename):
    calibration = []
    with open(filename) as file:
        for line in file:
            line = modify_number_string(line.strip())
            calibration.append(append_first_last_digit(line.strip()))
    file.close()
    return calibration


print(sum(find_calibration("input.txt")))
