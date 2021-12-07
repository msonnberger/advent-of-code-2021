from aocd import data

def faster_sum(n):
    return (n * n + n) // 2

def solve(part2 = False):
    positions = [int(x) for x in data.split(',')]
    min_cost = 1e12

    for i in range(min(positions), max(positions) + 1):
        total_cost = 0
        for pos in positions:
            if not part2:
                total_cost += abs(pos - i)
            else:
                total_cost += faster_sum(abs(pos - i))

        min_cost = min(min_cost, total_cost)

    part = 2 if part2 else 1
    print(f"part {part}: {min_cost}")

solve()
solve(part2=True)