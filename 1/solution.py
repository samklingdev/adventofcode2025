from pathlib import Path
from typing import Iterator, Tuple

def read_data(path: str) -> Tuple[str, int]:
    """Read lines from input file."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [(token[0], int(token[1:])) for token in lines]

data = read_data("input.txt")

def spin_right(idx, steps):
    wraps = 0
    for _ in range(steps):
        idx += 1
        if idx > 99: 
            idx = 0
        if idx == 0:
            wraps += 1
    return idx, wraps

def spin_left(idx, steps):
    wraps = 0
    for _ in range(steps):
        idx -= 1
        if idx < 0: 
            idx = 99
        if idx == 0:
            wraps += 1
    return idx, wraps
           
def solution_part1():
    idx = 50
    result = 0
    for [dir,steps] in data:
        if dir == 'L':
            idx, _ = spin_left(idx, steps)
            if idx == 0: 
                result += 1
        elif dir == 'R':
            idx, _ = spin_right(idx, steps)
            if idx == 0:
                result += 1
    return result

def solution_part2():
    idx = 50
    wraps = 0
    for [dir,steps] in data:
        if dir == 'L':
            idx, wrap = spin_left(idx, steps)
            wraps += wrap
        elif dir == 'R':
            idx, wrap = spin_right(idx, steps)
            wraps += wrap
    return wraps


if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())