f = open("inputs/02.txt")

def parser(file):
	return [[int(j) for j in l.split()] for l in file.read().strip().split("\n")]

def part1(input):
	o = 0
	for report in input:
		prev = report[0]
		ascending = prev < report[1]
		for level in report[1:]:
			diff = abs(prev - level)
			if diff > 3 or (prev < level) != ascending or prev == level:
				break
			prev = level
		else:
			o += 1
	return o

def part21(input):
	o = 0
	for report in input:
		prev = report[0]
		ascending = prev < report[1]
		for index, level in enumerate(report[1:]):
			diff = abs(prev - level)
			if diff > 3 or (prev < level) != ascending or prev == level:
				# 1 error case, retry popping one then the other:
				c1_report = [i for i in report]
				c1_report.pop(index)
				
				passed = True
				prev = c1_report[0]
				ascending = prev < c1_report[1]
				for level in c1_report[1:]:
					diff = abs(prev - level)
					if diff > 3 or (prev < level) != ascending or prev == level:
						passed = False
					prev = level
				if passed:
					o += 1
					break

				c2_report = [i for i in report]
				c2_report.pop(index+1)
				passed = True
				prev = c2_report[0]
				ascending = prev < c2_report[1]
				for level in c2_report[1:]:
					diff = abs(prev - level)
					if diff > 3 or (prev < level) != ascending or prev == level:
						passed = False
						break
					prev = level
				if passed:
					o += 1
					break

				# try removing the first level
				c0_report = [i for i in report]
				c0_report.pop(0)
				passed = True
				prev = c0_report[0]
				ascending = prev < c0_report[1]
				for level in c0_report[1:]:
					diff = abs(prev - level)
					if diff > 3 or (prev < level) != ascending or prev == level:
						passed = False
						break
					prev = level
				if passed:
					o += 1
					break
				break
			prev = level
		else:
			o += 1
	return o

def part2(input):
	o = 0
	for report in input:
		prev = report[0]
		ascending = prev < report[1]
		for level in report[1:]:
			diff = abs(prev - level)
			if diff > 3 or (prev < level) != ascending or prev == level:
				# brute
				for i in range(len(report)):
					c_report = [l for l in report]
					c_report.pop(i)
					prev = c_report[0]
					ascending = prev < c_report[1]
					for level in c_report[1:]:
						diff = abs(prev - level)
						if diff > 3 or (prev < level) != ascending or prev == level:
							break
						prev = level
					else:
						o += 1
						break
				break
			prev = level
		else:
			o += 1
	return o

from time import time

t0 = time()
stuff = parser(f)
print(f"parsed in: {time()-t0}")
# print(stuff)

t0 = time()
print(part1(stuff))
print(f"p1 in: {time()-t0}")

t0 = time()
print(part21(stuff))
print(f"p2 in: {time()-t0}")

t0 = time()
print(part2(stuff))
print(f"p2brute in: {time()-t0}")