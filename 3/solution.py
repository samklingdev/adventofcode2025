from encodings.punycode import digits
from pathlib import Path
from typing import Iterator, List, Tuple


def read_data() -> list[str]:
    # read file
    with open('input.txt', "r") as f:
        text = f.read().split("\n")
        return text

def solution_part1() -> int:
    result = 0
    text = read_data()
    for battery in text:
        biggest = [0,0]
        for i,c in enumerate(battery):
            n = int(c)
            if n > biggest[0] and i < len(battery)-1:
                biggest[0] = n
                biggest[1] = 0
            elif n > biggest[1]:
                biggest[1] = n
        combined = biggest[0]*10 + biggest[1]
        print(combined)
        result += combined
    return result

def solution_part2() -> int:
    result = 0
    text = read_data()
    for battery in text:
        battery_int = [int(c) for c in battery]
        battery_len = len(battery_int)
        biggest = [0] * 12
        start = 0
        for idx, _ in enumerate(biggest):
            end = battery_len - (11 - idx)
            for i, n in enumerate(battery_int):
                if i < start or i >= end:
                    continue
                if n > biggest[idx]:
                    biggest[idx] = n
                    start = i + 1

        result += int("".join([str(n) for n in biggest]))     
    return result

if __name__ == "__main__":
    # print("part1:", solution_part1())
    print("part2:", solution_part2())