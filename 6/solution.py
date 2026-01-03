import re
import numpy as np

def read_data() -> list[str]:
    # read file
    with open('input.txt', "r") as f:
        txt = f.read().splitlines()
        return txt


def solution_part1() -> int:
    result = 0
    data = read_data()
    new_data = [] # list of lists
    for i, line in enumerate(data):
        vals = line.split(" ")
        vals = line.split() # remove empty strings
        for j,val in enumerate(vals):
            if len(new_data) <= j:
                new_data.append([])
            new_data[j].append(val)

    for col in new_data:
        operator = col[-1]
        numbers = list(map(int, col[:-1]))
        if operator == "+":
            result += sum(numbers)
        elif operator == "*":
            prod = 1
            for n in numbers:
                prod *= n
            result += prod

    return result
    

def solution_part2() -> int:
    result = 0
    data = read_data()
    arr = data[:-1]
    operators = data[-1]
    new_arr = []
    v = []
    for i, operator in enumerate(operators):
        # add operator if not space
        if operator != " ":
            v = []
            v.append(operator)

        numbers = [row[i] for row in arr] # get column
        numbers = [n for n in numbers if n != ' '] # remove spaces
        number = "".join(numbers) # combine digits

        if numbers:
            v.append(number)
        else:
            new_arr.append(v)
        if i == len(operators) - 1:
            new_arr.append(v)

    for v in new_arr:
        if not v:
            continue
        operator = v[0]
        numbers = list(map(int, reversed(v[1:])))
        if operator == "+":
            result += sum(numbers)
        elif operator == "*":
            prod = 1
            for n in numbers:
                prod *= n
            result += prod
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())