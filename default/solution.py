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
    return result

def solution_part2() -> int:
    result = 0
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())