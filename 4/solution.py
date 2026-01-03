from encodings.punycode import digits
from pathlib import Path
from typing import Iterator, List, Tuple

def read_data() -> list[list][str]:
    # read file
    with open('input.txt', "r") as f:
        return [list(line) for line in f.read().splitlines()]

def solution_part1() -> int:
    result = 0
    matrix = read_data()
    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char != '@':
                continue

            up_left = (x - 1, y - 1)
            up = (x, y - 1)
            up_right = (x + 1, y - 1)
            left = (x - 1, y)
            right = (x + 1, y)
            down_left = (x - 1, y + 1)
            down = (x, y + 1)
            down_right = (x + 1, y + 1)
            neighbors = [up_left, up, up_right, left, right, down_left, down, down_right]
            rolls = 0
            for n in neighbors:
                nx, ny = n
                if nx < 0 or ny < 0:
                    continue
                if nx >= len(matrix[0]) or ny >= len(matrix):
                    continue
                neighbor_char = matrix[ny][nx]
                if neighbor_char:
                    if neighbor_char == '@':
                        rolls += 1
            if rolls < 4:
                result += 1
            
    return result

def solution_part2() -> int:
    result = 0
    matrix = read_data()
    found = list[(int,int)]()
    while True:
        for cord in found:
            y, x = cord
            matrix[y][x] = 'x'
        found = list[(int,int)]()
        for y, line in enumerate(matrix):
            for x, char in enumerate(line):
                if char != '@':
                    continue

                up_left = (x - 1, y - 1)
                up = (x, y - 1)
                up_right = (x + 1, y - 1)
                left = (x - 1, y)
                right = (x + 1, y)
                down_left = (x - 1, y + 1)
                down = (x, y + 1)
                down_right = (x + 1, y + 1)
                neighbors = [up_left, up, up_right, left, right, down_left, down, down_right]
                rolls = 0
                for n in neighbors:
                    nx, ny = n
                    if nx < 0 or ny < 0:
                        continue
                    if nx >= len(matrix[0]) or ny >= len(matrix):
                        continue
                    neighbor_char = matrix[ny][nx]
                    if neighbor_char:
                        if neighbor_char == '@':
                            rolls += 1
                if rolls < 4:
                    found.append((y,x))
                    result += 1
        if not found:
            break
            
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())