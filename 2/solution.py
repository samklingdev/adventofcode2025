from pathlib import Path
from typing import Iterator, Tuple


def read_ranges(path: Path = Path(__file__).with_name("input.txt")) -> Iterator[Tuple[int, int]]:
    text = path.read_text()
    for token in text.split(","):
        a, b = token.split("-")
        yield int(a), int(b)


def solution_part1() -> int:
    return sum(
        n
        for start, end in read_ranges()
        for n in range(start, end + 1)
        if (s := str(n))[: len(s) // 2] == s[len(s) // 2 :]
    )


def _is_repeated(s: str) -> bool:
    n = len(s)
    # try only divisors up to n//2; check by repeating the candidate slice
    for size in range(1, n // 2 + 1):
        if n % size:
            continue
        if s == s[:size] * (n // size):
            return True
    return False


def solution_part2() -> int:
    return sum(
        n
        for start, end in read_ranges()
        for n in range(start, end + 1)
        if _is_repeated(str(n))
    )


if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())