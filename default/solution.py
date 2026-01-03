
def read_data() -> list[str]:
    # read file
    with open('input.txt', "r") as f:
        txt = f.read().splitlines()
        return txt


def solution_part1() -> int:
    result = 0
    data = read_data()
    return result
    

def solution_part2() -> int:
    result = 0
    data = read_data()
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())