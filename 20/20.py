from aocd import lines
import numpy as np


algo = lines[0]
lines = lines[2:]
row_count = len(lines)
col_count = len(lines[0])
orig = np.ndarray((row_count, col_count), dtype=object)

for i in range(row_count):
    for j in range(col_count):
        orig[i, j] = lines[i][j]


def enhance(pic):
    shape = pic.shape
    enhanced = np.ndarray((shape[0] - 2, shape[1] - 2), dtype=object)
    
    for x in range(1, shape[0] - 1):
        for y in range(1, shape[1] - 1):
            comb = ''
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    comb += pic[x + i, y + j]

            comb = comb.replace('.', '0').replace('#', '1')
            new_pixel = algo[int(comb, 2)]
            enhanced[x - 1, y - 1] = new_pixel
    
    return enhanced


def solve(n, image):
    for i in range(n):
        if i % 2 == 0:
            image = np.pad(image, 2, constant_values='.')
        else:
            image = np.pad(image, 2, constant_values='#')

        image = enhance(image)

    return np.count_nonzero(image == '#')


print('part 1:', solve(2, orig))
print('part 2:', solve(50, orig))