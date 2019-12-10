from collections import defaultdict
import math

L = """#.....#...#.........###.#........#..
....#......###..#.#.###....#......##
......#..###.......#.#.#.#..#.......
......#......#.#....#.##....##.#.#.#
...###.#.#.......#..#...............
....##...#..#....##....#...#.#......
..##...#.###.....##....#.#..##.##...
..##....#.#......#.#...#.#...#.#....
.#.##..##......##..#...#.....##...##
.......##.....#.....##..#..#..#.....
..#..#...#......#..##...#.#...#...##
......##.##.#.#.###....#.#..#......#
#..#.#...#.....#...#...####.#..#...#
...##...##.#..#.....####.#....##....
.#....###.#...#....#..#......#......
.##.#.#...#....##......#.....##...##
.....#....###...#.....#....#........
...#...#....##..#.#......#.#.#......
.#..###............#.#..#...####.##.
.#.###..#.....#......#..###....##..#
#......#.#.#.#.#.#...#.#.#....##....
.#.....#.....#...##.#......#.#...#..
...##..###.........##.........#.....
..#.#..#.#...#.....#.....#...###.#..
.#..........#.......#....#..........
...##..#..#...#..#...#......####....
.#..#...##.##..##..###......#.......
.##.....#.......#..#...#..#.......#.
#.#.#..#..##..#..............#....##
..#....##......##.....#...#...##....
.##..##..#.#..#.................####
##.......#..#.#..##..#...#..........
#..##...#.##.#.#.........#..#..#....
.....#...#...#.#......#....#........
....#......###.#..#......##.....#..#
#..#...##.........#.....##.....#...."""


# Euclidean distance between (i0, j0) and (i, j)
def metric(i0, j0, i, j):
    dy = i0 - i
    dx = j0 - j
    return math.sqrt(dy*dy + dx*dx)


# Normalizes a [0, 2pi) angle to
# clockwise angle starting at pi/2
def norma(t):
    if t <= math.pi/2:
        return math.pi/2 - t
    else:
        return 2*math.pi - t + math.pi / 2


# Shooting angle from (i, j) to (I, J)
# normalized at [0, 2pi)
def angle_point(i, j, I, J):
    di = i - I
    dj = J - j
    ang = math.atan2(di, dj)
    if ang < 0:
        ang += 2*math.pi
    return ang


# Part 1
L = [list(c) for c in L.split("\n")]
y = len(L)
x = len(L[0])
lengths = []

# For each cell
for i0 in range(y):
    for j0 in range(x):
        if L[i0][j0] == ".":
            continue

        # Compute a set of the number of
        # possible shooting angles
        s = set()
        for i in range(y):
            for j in range(x):
                if L[i][j] == "." or (i == i0 and j == j0):
                    continue
                ang = angle_point(i0, j0, i, j)
                s.add(ang)
        lengths.append([len(s), (i0, j0)])

# Find cell with maximal number of reachable asteorids
how_much, (i0, j0) = max(lengths, key=lambda x: x[0])
print("Part 1:", how_much)

# Part 2
counter_deleted = 1
ang = math.pi/2
left_asteroids_to_destroy = True
while left_asteroids_to_destroy:
    # Group asteroids in a dictionary
    # with key as shooting angle
    d = defaultdict(set)
    for i in range(y):
        for j in range(x):
            if L[i][j] == "." or (i == i0 and j == j0):
                continue
            dis = norma(angle_point(i0, j0, i, j))
            d[dis].add((i, j))

    if len(d) == 0:
        left_asteroids_to_destroy = False

    # Iterate all angles increasingly
    for angle in sorted(d.keys()):
        # Given a certain angle, delete the closest point
        # to the shooting center
        i, j = min(d[angle], key=lambda p: metric(i0, j0, p[0], p[1]))
        L[i][j] = "."

        # Stop execution at the 200-th destroyed cell
        if counter_deleted == 200:
            print("Part 2:", j*100 + i)
            left_asteroids_to_destroy = False
            break
        counter_deleted += 1
