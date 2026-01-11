from collections import deque
from pathlib import Path
from typing import List
from functools import cache

def read_data(path: str) -> List[str]:
    """Read lines from input file."""
    return Path(path).read_text(encoding="utf-8").splitlines()

data = read_data("input.txt")

def solution_part1() -> int:
    result = 0
    start = data[0].find("S")
    beams = deque([(0,start)])
    seen = set()

    while beams:
        row, col = beams.popleft()
        if (row, col) in seen:
            continue
        seen.add((row, col))

        if data[row][col] == "^":
            result += 1
            beams.append((row, col - 1))
            beams.append((row, col + 1))
        else:
            if row + 1 < len(data):
                beams.append((row + 1, col))
    return result

@cache
def solve(row,col) -> int:
    # base case
    if row >= len(data):
        return 1
    
    # recursive case
    if data[row][col] == "^":
        return solve(row, col - 1) + solve(row, col + 1)
    else:
        return solve(row + 1, col)

def solution_part2() -> int:
    result = 0
    start = data[0].find("S")
    result = solve(1, start)
    return result

if __name__ == "__main__":
    # print("part1:", solution_part1())
    print("part2:", solution_part2())