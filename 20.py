import copy


def test():
    global algorithm
    global image
    
    algorithm = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
""".split("\n")
    algorithm.remove("")
    algorithm.remove("")

    algorithm = "".join(algorithm)

    image = """
#..#.
#....
##..#
..#..
..###
""".split("\n")
    image.remove("")
    image.remove("")

def a1():
    global algorithm
    global image

    algorithm = """
#..#.#######.##...##.##.#.#..#..#.....####...####.##.###...##.####......##.###.##...#..##..#.######...###..########.#.##.#.#..#..##.##..####.###.###..#...##.##.###.....###..###....#.####.#..##....#.##...##.#..#.....###.#..#.....##..##.#.#.....#....####.#.#.#....#.#...#.##...#.#.#....#.#.#....##.#.####.##..#####.####.#.####..#...###.###..##...#..###.####...#..#.####.###.##..##....#.####....#.#..##.#..#.##.##..#......###.#...#..#.#.#.##.######.##.##..####.##..#.###.##.....##...#.....#..#....###..####.#.##..#.
""".split("\n")
    algorithm.remove("")
    algorithm.remove("")
    algorithm = "".join(algorithm)

    image = """
#.#...#.....#..#.#....#.#.###.......###.###...##...#..#..###.###...##...#.#####...##..##.#.#..##....
##.####...#.#.#.##.##....###.##..##..#.##....#.####.#.#####.#..............#.###...#..#####.#....###
#.#...#..#.##..#.#.#.##.##..####..####.#..#####.#.....#####..#.##..####.#.....#.#..##..##....##.#.#.
.#..##.##.#######....####.##..######..##...#...#####....##.######.##..#..##.#.#.#.#..#....#.##.###.#
...#.###.##..##..##.#..###..#.#..#..#...#..........##..##.##..#.#...##.#.#.#.#...##.#..##.....##.##.
...##.#.#..####..#.##.#.#....#.#..#####.#..#.#.#.##..###.##..###.##...###.##.#...#.##.##........##..
#..#.#......#..##.#......#..##..#.#.#.....#.#####.##...#......#.#...##.###.#.#.#.#..###..#.##.#.....
#.#..##.#.###...#.##.#.##..########.####.#.#...##.#.##....#.....#...#..##.####.#...##.#.##.#.#...#.#
##.....#.###...##....#...##.####.####..#....##.#.#.##...#.#######.#.####.##.#.##.##.....##.####.#...
#.#.##.###.#...##.#.#.###..#.#.#..##.######..#.##......#..##..###.#.#...#...###.#.#..#.##.###..#..##
#####....#####.......##.#.#...###.##.###..##.##....#.####.####..........####.#...#....####..##.#####
.#.#..#.#...#.#..#..##.#.#.#...##.....##.###.#.#......#.#.#.##..#..###..#.#..#.###...###.#.#.#.#.#.#
#.#..###..##.#.#.#...##.####..##....#.##.#.#...#..#...#..#..#..##....#.......#######.#.##...#.###.##
#..#..#####...##.###.#.#.#.#....#..#.####.####...#..#.##.####.####.###.#.##.#..##.#.##.##.#.#...##.#
..#.###...#.####...##..#.###....##.#..#..#.#.#....##...####.##..#.#.##...##.......#.#..#..##.#.##...
#...##.##..#...#.###.#.#.##..##...####.##.#.#..#....#####....##.#####..#####.#..##.#.....##.###..##.
..#..###..#.#.########.#######..######...##.##.##..##...####..##....#....##..#...##...#.####.#...##.
.......##.#.#...##.#..#.##.#..##.##..#......#####.#....#..#..#####....#.#..#.##.##.#.#..###..##.####
.#...##..######.#...##.#######.####.####...#.####......###.#.#.#.###..#...#.#..#.#..##...#..##.#.#.#
####.#.####..#..#...#..####.#......####...###....##########...####.#...#...#.###..###.....#....#..#.
...#.##.....###...##.#..##.....#..##.##........##.####.##..#...#..######...##.#....##..#..#######.#.
##.##..#...#....#.........###.........##...#........#.#.###..#...#.#.##....#.......#....##.##..#####
.######.##..####...#...#.##..####...#######.###...#.#.#...##.#......###..#..#.#.#...##........##.##.
.#.##.##.....#......##.##.#.##..##....##..#####.........#.##........#..######.##.#.#......#.....##.#
#.#.######.#..##.#.##..#.###..#.#..##...###.###...#.#.......#.##...#.#..#....###..####.##..#.#.##.#.
.#..#...#.#..#.......###...#.##.####..##.#......#..#.#..####.#.#...###.##.#.....#...###.#....###.##.
#..##.#...##..####.#.##..#..####.##.###.....###..#.####.##.#####...######.#.###.###.##.######..#..#.
######.#.#.#.#..#.##.#......###......##..#....#...#..##...#..#.##..#.#####.######...##..#.##..###.##
#..##...#.#..#..##.####....#.#..##.###...##..#####.##.#....###.......#.#.#.#......##.##.#..#.#.#.#.#
.#..#..#.######.#.....##.#.#...#....#########....########...##...##.#..#.###.##.#..#..#######.#.##..
..##...##.###..##......#...#..#....#....###..##.#..###.#...##.#..#.####.#.##...#..####.....##..##...
#.##...###...#...#.##..#.....##.###.##...#.#..#.##.#..###..#.##.##.....#.##..#.####..#.#.#..###.##.#
#...#..#.#...##.#..##.##.#..##.#...###...###...#..###..########.####.###.#.....#..#..###.#.##...#.##
#.##.######.####...#.#...###.#..#...#.#.###.##.#...##...##.##.###.##.####..#.#####...#....###....##.
#...#.#.##.#.#..###..#.#..##.##..###..#.#.#..#..#..####.##..##.#..#..............#.###.##.#.#..#####
##.#..#.##...#....####.##....#..##.###......#..##....##########.#.###...#.##...#..##.#....#...#.####
#..#.#...#.#..#....##.##...###.....####..#..##.##.####..#.#.#.######..#...##...#.........##.#.####..
.#..#.#.#....#.#...##..#.#.##.##.....######...###.##.##.##.#..###...##.#.....##.##..#..####..###..#.
.#.##..##....#.###.#...##....#..#.########.##.#.#..#######...##.#.###.#.###...###.#..###.....####...
#.##...#...###.####.###.#.##.#.##..#..#.####...###..###..#...##...#.#.#..###.#.#####.#######.###.###
##.#####.#..##.#..#.##.##..........######.#.###.###.#...##..##..#.......##..#.##.##.###.####......##
#.###..##....#.###...#...#.#..###...##.###.###.####.##..#####.#...#.####...##..######....#...#.#####
.#.#.####....#####...#...###..#...#.....###..###.##.#.....#..#.#.#.##..##.....##.....###.#...#.####.
##....##..#..#.##..##..#.#.#.#...#.#......##.#..#.##.#..#.###..#.#.#..##......####...#..#.##..####..
##..#.##.........######.#..##...#.##.###.#.#######.##...#.#####...#........######....#.#.####...#.##
##.#.......##.#...#.....#.#.####.#.##.##...#.##.#..#.#.##..###.#..##....#...##..##.##.#.##.#....#...
...#######...#..####..#.###.#.##..#.....#..##...###.....###.....##...##.#.......##.#.#.#.##....####.
.##.##...#...####.......##...##.##..#...###.#.#...#.####.##.#.######...#.#..###.##..####.##.##...#..
.#######.###.##...#.####...#.......#.#..##.##.#####.#.#....#..###.#.##...#.###...#...##.#..###......
##.#..#...##.####.#.###.####.#.##.#.##.......###..#####.#..#..###.####.#..#....#..#..##..#...#.##.#.
.#..###.##....##..##.######..#####..##.##....#.####....#.#.###...##...#######....####.#.##...##.#..#
#.###.##.....#...#..#..###..##.#..#..##.##.#...#...#.#....#......#.#.##.#.##.##...##.##.##.#....#.#.
..#.#.###.#..#.#.##.#.#..#.#.#.#.##...#.##..######.##.#####...#...##..#.###.##...#.#.#..#.#######.##
###.######..###...#.#.##.....###.......##.##.#........##..##...##.#.#.#.##.###.##.##..#......##..###
.#..#.#.##...#..##......###....#..##.#..##.##..##....###....##.#..##...###..##..#.####..##...#######
##.#..####..##....#..####..#.#.##..###...##.#.#...##.#..###.##..###.####.##.#.###..#...#.##.#...#.##
...#..#.....#...#...###..####.##....#.##.##.#...###.#..#####.#.##.#..#..##......#..##.##..###.#...##
.#..#..########.#...#.####..#.#..#..#..####...##.#.####.#.#...#.#.###..#####.###.....####.#..#.#.#..
...#.#####.###.#..#.##.#.#...#.##....#####..##.##..############.#.##..#.#.....###.#.############....
..#..#....#..#..##.######..###...##..#.....##.#.##....#..####.#...#..##.....##..##.###.##.#..#######
#..#..##......#...####.####.##...######.#..##...###..#.#.#########..###.#.##.#.##.#...#.####.##...#.
.##.#...###.###..#.##...#...#..##.#....#.#....###.###.##.####.#.#.#..#....#.##.###..#...##..#...#.##
..##..#...##.#..#...#....#....###.##.##.##...##..####..#####.###.#.#....#.##....###.#....##...###.##
######.........#..#...####.#.......#.#####.#..#....#.#.####.#####...##..#####..###.#.#.##.###...#.##
...#.#...#.#..####.##....##.##.##.##...#...#..##..######.####..##.#.#..##..##.##...##.#...######....
.##..####..#.........####....##....#..##...#####....#.#...#......##.#.#.##...###..##.##..####..####.
#####...#.##...#######.#.######..##.....#..##...#..###.###..####.####.#####.#..#...##.....##.###..#.
##........#...#..#....#.###.##....#..#..###.#..##.#####.##....#.#..#.#..##.##...##.#....##..##.###..
###.#..#.###.#.###.###.#....##....#.#..##..####.###.##...##.##.#...#...#.....#####....###.#.##.##.##
.#...#....#.#...#.####..#..#...###..##.#..##.......##...##.##.#..#.#..##.##..##..###..##....##.#...#
###.#.#...#..#..###.#.#.##.....#..##...#.#....##.##.....###.####......####....#..##..#.#....#.##.#..
........#..#.#.##.##...#...#.#.##...##.#..#..#.#.##.####.###..######.##...#...#.##.#.###..##.#..##..
....##.#####.#.##.#.....#.#.###....#.###...#.####.##.##.#.########.##.#..##.#.##.##########.#..#...#
#..........###.####..#.....##....#.##.##..###.##........#..#...###.#..#..##.#.#.###.#.##.####..#####
#...#..##...#.#..#...###.#...#..#.###...###..#....####.##.###..#.#...##...##.#..#.###...#..###...###
####.###....####.#..#....#.#...##.#.######..#..#...##....#.#######...####..#.##......#...#..###..#..
##.#.#####.###.#...#.##..######..#...#.#####..#.##.#.#.##.###....######.#.....#..##..##..#...##..#..
.#########.##.##...#.#...##.###.#....###.#......#....##.##.#..####..##..##..#.##..#...#########....#
##....##.##..###....#...#..#...#.##.##..#######.#.##..##.#.#..#.###.##.###.#.#.#.##.#...##.######.#.
.##.#.#.#####.##...#.##...#...#..####.##..#.######..##.#.#.#....#...#..#.####.#..#..#.#...##.....###
..##.##..#........#........#.#.#.##.#....####....##....##.##...##.#.#...####.##.#####.....##.#.#.#..
#..####.#....##.###.#######..#...#..##.#...##..##.#.##..##.#.##.#.#...#.#.###.#..#.##.###..#.#....#.
#....#...#..##.##.####.#..#..####...#.#.#...#######...##..##...#.#.########...#..##.##.#...#.###.###
...##..##.##.###..###...#.####..#.....##.#..#.....##....##.#.####..#..#...##..#.#..#######.##.#...##
###...#...##.##.#...#..##.#####.######.###....###........#.##......#.###...###.#.#.##.#####..####.#.
.#########.#####....##.##..#.####.##..####.#...#.###.##.##..####.##..###......#...##..#.#.###.#..##.
.#.###..###....#####.#......#.###......###########..####.#......##.#..#..##..#.#.....#.#...#.##.##.#
..###...#.#.###....#..#####.#.###.###..#.#.#.#..#..##...#..###..#####...#.###.#.##.#.##.##.#.......#
.###..#.##..#..#.##.....#....##..#.#........##.##.########.....###..#....########.#.##.##..#.......#
.#.#..#####..###.#..#...#..#.##..###..#.###.#.##...#..###.#.#.#.##...####.####.#...#..#.###..#.###.#
#.#..##..#...###.#..####...#..#..##.###...###.##.#...#.#......##..##.#####.####....#...##.#..#..##.#
#....#...####.....#.##.#....#.#.##..#....##..####....#..###...#.#.##.#....#.###.###.....#.....#.#.##
#.##.#...#..#...########...#...##...###.##..###..#..##.#.#.#####.#....###.#..#..#.#.#...###.#.##.###
..##.#.###.#..##.#.##..##.##..##.....#..#....#.##.#...###.###....##..####..##....##.###.###.....#..#
#.##.###...##..##...#......#.#..#.......##.#.#.##.##..#....###.#..#.##.###.##....#.##....#.##.###..#
.##..#....#.#...#.###.#.##.#.##....####.######.#.#....##.##.....#.##.####..#.......##..##.#.##.....#
.###.##.....#...#.#..#.#..#..#...###.........#######.#..#######...#...#...#..######.#..#####.###....
#.....#..#....#####.....#....##.#.##..###..##..###.##..#.##..###....#.##...#####.#.#..#.##..##..#.#.
#.#..#....#.#...###.###.##...#.######.##.###..#..#..##.#.##.##.###..####..#..#..#..#...###..##.#..##
....#.###....#.#..##.#.##..#.###..#.#.##..#.#..##.#########..#.###...#.#.#....#.....####...#...##..#
""".split("\n")
    image.remove("")
    image.remove("")


def expand():
    global image
    image = ["." * len(image[0])] + image
    image += ["." * len(image[0])]

    for k in image:
        image[image.index(k)] = "." + k + "."

def inpand():
    global image
    image = image[1:-1]

    for k in image:
        image[image.index(k)] = k[1:-1]



def visible():
    global image
    [print(k) for k in image]

def strintify(string):
    if string == ".":
        return "0"
    if string == "#":
        return "1"
    return None


def enhance():
    global image
    
    new_image = copy.deepcopy(image)
    for line in range(1, len(image) - 1):
        for col in range(1, len(image[0]) - 1):
            b = ""
            b += strintify(image[line-1][col-1])
            b += strintify(image[line-1][col])
            b += strintify(image[line-1][col+1])
            
            b += strintify(image[line][col-1])
            b += strintify(image[line][col])
            b += strintify(image[line][col+1])
            
            b += strintify(image[line+1][col-1])
            b += strintify(image[line+1][col])
            b += strintify(image[line+1][col+1])

            b = int(b, 2)

            new_image[line] = new_image[line][:col] + algorithm[b] + new_image[line][col+1:]

    image = new_image
    inpand()

a1()
#test()

n = 50

for _ in range(n):
    expand()
    expand()
    expand()

for i in range(n):
    enhance()
    print("\renhanced %i/%i" % (i+1, 50), end="")
print("")

print(sum([1 for k in "".join(image) if strintify(k) == "1"]))