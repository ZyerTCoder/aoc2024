f = open("inputs/01.txt")

def parser(file):
    return [l for l in file.read().strip().split("\n")]

def part1(input):
    o = 0
    l0 = sorted([int(l.split(" ")[0]) for l in input])
    l1 = sorted([int(l.split(" ")[-1]) for l in input])
    for (a, b) in zip(l0, l1):
        o += abs(a-b)
    return o

def part2(input):
    o = 0
    l0 = sorted([int(l.split(" ")[0]) for l in input])
    l1 = sorted([int(l.split(" ")[-1]) for l in input])
    counter = {}
    for i in l1:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    for i in l0:
        if i in counter:
            o += i * counter[i]
    return o

stuff = parser(f)
print(part1(stuff))
print(part2(stuff))