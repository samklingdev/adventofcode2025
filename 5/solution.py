def read_data() -> tuple[list[tuple[int,int]],list[int]]:
    # read file
    with open('input.txt', "r") as f:
        id_ranges = []
        ingredient_ids = [] 
        parts = f.read().split("\n\n")
        for line in parts[0].split("\n"):
            start, end = line.split("-")
            id_ranges.append((int(start), int(end)))

        for line in parts[1].split("\n"):
            ingredient_ids.append(int(line))
        return (id_ranges, ingredient_ids)


def solution_part1() -> int:
    result = 0
    id_ranges, ingredient_ids = read_data()
   
    for ingredient_id in ingredient_ids:
         for id_range in id_ranges:
            start, end = id_range
            if ingredient_id >= start and ingredient_id <= end:
                result += 1
                break
    return result
    

def solution_part2() -> int:
    result = 0
    id_ranges, _ = read_data()

    # sort ranges by start
    id_ranges = sorted(id_ranges, key=lambda r: r[0])
    new_ranges = [id_ranges[0]]

    for start, end in id_ranges[1:]:
        last_start, last_end = new_ranges[-1]
        if start <= last_end:  # overlap -> merge into last
            new_ranges[-1] = (last_start, max(last_end, end))
        else:
            new_ranges.append((start, end))

    result = sum(end - start + 1 for start, end in new_ranges)
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())