import re


def append_first_last_digit(input_string):
    digits = re.findall(r"\d", input_string)
    return int(digits[0] + digits[-1])


def find_calibration(filename):
    calibration = []
    with open(filename) as file:
        for line in file:
            calibration.append(append_first_last_digit(line.strip()))
    file.close()
    return calibration


print(sum(find_calibration("input.txt")))
