from pathlib import Path
from typing import List, Tuple

type Pos = Tuple[int, int]

def read_data(path: str) -> List[str]:
    """Read lines from input file."""
    return Path(path).read_text(encoding="utf-8").splitlines()

def walk(data: List[str], pos: Pos, splits: List[Pos]) -> Pos:
    x, y = pos
    # if we reached the bottom, return splits
    if y + 1 >= len(data):
        return splits

    # if x is out of bounds, return splits
    if x < 0 or x >= len(data[0]):
        return splits
        
    # move down until we find a split or reach the bottom
    for y in range(y + 1, len(data)):
        if data[y][x] == "^": # did we find a split?
            # recurse x -1 and x + 1
            print(f"split at {(x, y)}")
            left = walk(data, (x - 1, y), splits + [(x, y)])
            right = walk(data, (x + 1, y), splits + [(x, y)])
            return left + right
    else:
        return splits
    


def solution_part1() -> int:
    result = 0
    data = read_data("input.txt")
    start = data[0].find("S")
    splits = []
    splits = walk(data, (start, 0), splits)
    #remove duplicates
    splits = list(set(splits))
    return len(splits)

def solution_part2() -> int:
    result = 0
    data = read_data("example.txt")
    print(f"data: {data}")
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    # print("part2:", solution_part2())