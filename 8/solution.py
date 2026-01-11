from pathlib import Path
from pprint import pprint
from typing import List, Tuple
from functools import cache

def read_data(path: str) -> List[str]:
    """Read lines from input file."""
    return Path(path).read_text(encoding="utf-8").splitlines()

data = read_data("example.txt")

type Point3D = Tuple[int, int, int]

class Node:
    def __init__(self, value: Point3D, next_node: 'Node' = None):
        self.value = value
        self.next = next_node

def calc_distance(p1: Point3D, p2: Point3D) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    if x1 == x2 and y1 == y2 and z1 == z2:
        return 0.0
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

def solution_part1() -> int:
    result = 0
    distances = {}
    circuits = list[set[Point3D]]()
    
    for line in data:
        for other_line in data:
            p1: Point3D = tuple(map(int, line.split(',')))
            p2: Point3D = tuple(map(int, other_line.split(',')))
            if p1[0] == p2[0] and p1[1] == p2[1] and p1[2] == p2[2]:
                continue
            if (p2, p1) in distances:
                continue
            elif (p1, p2) in distances:
                continue
            dist = calc_distance(p1, p2)
            distances[(p1, p2)] = dist


    # sort distances by value
    distances = sorted(distances.items(), key=lambda item: item[1])
    
    # get 10 shortest distances
    distances = distances[0:10]

    for val, distance in distances:
        p1, p2 = val
        print(f"Shortest distance: {distance}, between points {p1} and {p2}")
        
        # do either point belong to an existing circuit?
        for circuit in circuits:
            if p1 in circuit:
                print(f"Adding point {p2} to existing circuit {circuit}")
                circuit.add(p2)
                break
            if p2 in circuit:
                print(f"Adding point {p1} to existing circuit {circuit}")
                circuit.add(p1)
                break
        else:
            print(f"Creating new circuit with points {p1} and {p2}")
            circuits.append(set([p1, p2]))
    
    # sort circuits by length descending
    sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
    
    result = 1
    # multiply lengths of top 3 circuits
    for circuit in sorted_circuits[0:3]:
        print(f"Circuit: {circuit}, length: {len(circuit)}")
        result *= len(circuit)
        
    
    pprint(circuits)
    return result


def solution_part2() -> int:
    result = 0
    return result

if __name__ == "__main__":
    print("part1:", solution_part1())
    print("part2:", solution_part2())
