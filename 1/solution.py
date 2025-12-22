
def getData():
    vals = []    

    with open('input.txt', 'r') as file:
        # Read the contents of the file
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n','')
            dir = line[0]
            num = int(line[1:])
            vals.append((dir, num))

    return vals

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
    vals = getData()
    for [dir,steps] in vals:
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
    vals = getData()
    for [dir,steps] in vals:
        if dir == 'L':
            idx, wrap = spin_left(idx, steps)
            print(dir, steps, idx, wrap)
            wraps += wrap
        elif dir == 'R':
            idx, wrap = spin_right(idx, steps)
            print(dir, steps, idx, wrap)
            wraps += wrap
    return wraps


if __name__ == "__main__":
    result1 = solution_part1()
    print("part1:",result1)
    result2 = solution_part2()
    print("part2:",result2)