from aocd import lines

def solve():
    digits = [""] * 10
    print(digits)

    count = 0
    for line in lines:
        inp, out = line.split(" | ")
        for o in out.split():
            if len(o) in [2, 3, 4, 7]:
                count += 1

    print(f"part 1: {count}")

solve()