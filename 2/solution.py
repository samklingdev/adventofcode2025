
def getData():
    with open('example.txt', 'r') as file:
        # Read the contents of the file
        lines = file.read()
        print(lines.split(','))
    
    return lines.split(',')


def is_invalid(s):
    # Placeholder for actual validation logic
    return False
           
def solution_part1():
    result = 0
    id_ranges = getData()
    for id_range in id_ranges:
        parts = id_range.split('-')
        start = int(parts[0])
        end = int(parts[1])
        for id in range(start, end + 1):
            print(id)
    return result

if __name__ == "__main__":
    result1 = solution_part1()
    print("part1:",result1)