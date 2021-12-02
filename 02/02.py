from aocd import submit, lines

def part1():
    depth = horizontal = 0

    for line in lines:
        instruction = line.split()[0]
        value = int(line.split()[1])

        match instruction:
            case 'forward':
                horizontal += value
            case 'up':
                depth -= value
            case 'down':
                depth += value

    print(f'part 1: {depth * horizontal}')
    #submit(depth * horizontal)


def part2():
    depth = horizontal = aim = 0

    for line in lines:
        instruction = line.split()[0]
        value = int(line.split()[1])

        match instruction:
            case 'forward':
                horizontal += value
                depth += aim * value
            case 'up':
                aim -= value
            case 'down':
                aim += value

    print(f'part 2: {depth * horizontal}')
    #submit(depth * horizontal)

part1()
part2()