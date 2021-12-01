from aocd import numbers, submit

def part1():
    count = 0

    for i in range(len(numbers) - 1):
        if numbers[i + 1] > numbers[i]:
            count += 1

    print(f'part 1: {count}')
    submit(count)


def part2():
    count = 0
    window_size = 3

    for i in range(len(numbers) - window_size):
        sum1 = sum(numbers[i : i + window_size])
        sum2 = sum(numbers[i + 1 : i + 1 + window_size])

        if sum2 > sum1:
            count += 1

    print(f'part 2: {count}')
    submit(count)

part1()
part2()