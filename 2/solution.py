
def getData():
    with open('input.txt', 'r') as file:
        # Read the contents of the file
        lines = file.read()
    
    return lines.split(',')

            
def solution_part1():
    result = 0
    id_ranges = getData()
    for id_range in id_ranges:
        parts = id_range.split('-')
        start = int(parts[0])
        end = int(parts[1])
        for id in range(start, end + 1):
            mid = len(str(id)) // 2
            left = str(id)[:mid]
            right = str(id)[mid:]
            if left == right:
                result += id
    return result


def solution_part2():
    result = 0
    id_ranges = getData()
    for id_range in id_ranges:
        parts = id_range.split('-')
        start = int(parts[0])
        end = int(parts[1])
        for id in range(start, end + 1):
            id_len = len(str(id))
            mid = id_len // 2
                # if its not dividable, skip
            sizes = [s for s in range(1, mid+1) if id_len % s == 0]
            for size in sizes:
                parts = [str(id)[s:s+size] for s in range(0, id_len, size)]
                # print(f"size:{size} parts:{parts}")
                if all(part == parts[0] for part in parts):
                    result += id
                    break

    return result

if __name__ == "__main__":
    # result1 = solution_part1()
    # print("part1:",result1)
    result2 = solution_part2()
    print("part2:",result2)