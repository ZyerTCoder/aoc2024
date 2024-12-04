f = open("inputs/03.txt")

import re

def parser(file):
	return file.read().strip()

def part1(input):
	o = 0
	muls = re.findall(r"mul\(\d+,\d+\)", input)
	for mul in muls:
		left, right = mul.split(",")
		o += int(left[4:]) * int(right[:-1])
	return o

def part1g(input):
	return sum([int(l) * int(r) for l,r in re.findall(r"mul\((\d+),(\d+)\)", input)])

def part2(input):
	dos = input.split("don't()")
	for i, do in enumerate(dos[1:]):
		dos[i+1] = "".join(do.split("do()")[1:])
	return part1g("".join(dos))

stuff = parser(f)
print(part1(stuff))
# print(part1g(stuff))
print(part2(stuff))
