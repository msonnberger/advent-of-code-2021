from aocd import data
from collections import defaultdict
import numpy as np

points, folds = data.split('\n\n')

points = [line.split(',') for line in points.splitlines()]
points = [(int(x), int(y)) for x, y in points]
folds = [line.split()[-1].split('=') for line in folds.splitlines()]
folds = [[axis, int(val)] for axis, val in folds]
paper = defaultdict(int)

for point in points:
    paper[point] = 1


def part1():
    axis, val = folds[0]
    fold(axis, val)
    print(f"part 1: {sum(paper.values())}")

def part2():
    for axis, val in folds:
        fold(axis, val)

    max_row = max(x for x, _ in paper.keys())
    max_col = max(y for _, y in paper.keys())

    matrix = np.ones((max_row + 1, max_col + 1))

    for point in paper.keys():
        matrix[point] = 8

    print(matrix.transpose())

def fold(axis, val):
    idx = 0 if axis == 'x' else 1
    point_change = [point for point in paper.keys() if point[idx] > val]

    for point in point_change:
        del paper[point]
        d = point[idx] - val
        x, y = point
        if axis == 'x':
            x = x - 2 * d
        
        if axis == 'y':
            y = y - 2 * d

        new_point = (x, y)
        paper[new_point] = 1

part1()
part2()