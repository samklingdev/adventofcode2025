from pathlib import Path
from typing import Iterator, Tuple


def read_ranges(path: Path = Path(__file__).with_name("input.txt")) -> Iterator[Tuple[str, int]]:
    text = path.read_text()
    for token in text.split("\n"):
        a, b = token[0], token[1:]
        yield a, int(b)

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
    for [dir,steps] in read_ranges():
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
    for [dir,steps] in read_ranges():
        if dir == 'L':
            idx, wrap = spin_left(idx, steps)
            wraps += wrap
        elif dir == 'R':
            idx, wrap = spin_right(idx, steps)
            wraps += wrap
    return wraps


if __name__ == "__main__":
    result1 = solution_part1()
    print("part1:",result1)
    result2 = solution_part2()
    print("part2:",result2)