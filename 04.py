f = open("inputs/04.txt")

def parser(file):
	return [[c for c in r.strip()] for r in file.readlines()]

directions = [
	(-1, -1), (-1, 0), (-1, 1),
	(0, -1),          (0, 1),
	(1, -1), (1, 0), (1, 1)
]

directionsX = [
	(-1, -1), (-1, 1),
	(1, -1),  (1, 1)
]

def isInBounds(input, r, c):
	return 0 <= r < len(input) and 0 <= c < len(input[r])

def checkAround(input, r, c):
	o = 0
	for dir in directions:
		dr, dc = r + dir[0], c + dir[1]
		if isInBounds(input, dr, dc):
			if input[dr][dc] == "M":
				dr, dc = dr + dir[0], dc + dir[1]
				if isInBounds(input, dr, dc):
					if input[dr][dc] == "A":
						dr, dc = dr + dir[0], dc + dir[1]
						if isInBounds(input, dr, dc):
							if input[dr][dc] == "S":
								o += 1
	return o

def part1(input):
	o = 0
	for r in range(len(input)):
		for c in range(len(input[r])):
			if input[r][c] == "X":
				o += checkAround(input, r, c)
	return o

def checkAroundX(input, r, c):
	s = 0
	for dir in directionsX:
		dr, dc = r + dir[0], c + dir[1]
		if isInBounds(input, dr, dc):
			if input[dr][dc] == "M":
				dr, dc = r - dir[0], c - dir[1]
				if isInBounds(input, dr, dc):
					if input[dr][dc] == "S":
						s += 1
	return s == 2

def part2(input):
	o = 0
	for r in range(len(input)):
		for c in range(len(input[r])):
			if input[r][c] == "A":
				o += checkAroundX(input, r, c)
	return o

stuff = parser(f)
print(part1(stuff))
print(part2(stuff))
