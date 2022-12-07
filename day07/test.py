lines = open("day07/input.txt").readlines()


def create_path(l):
    return '/'.join(l).replace("//", "/")


fs = {}
curr = []
part1 = 0

for line in lines:
    line = line.replace("\n", "")
    if line.startswith("$ cd "):
        directory = line.replace("$ cd ", "")
        if directory != "..":
            curr.append(directory)
        else:
            curr.pop()
        fs.setdefault(create_path(curr), 0)
    elif line.startswith("$ ls"):
        continue
    else:
        a, b = line.split(" ")
        if a != "dir":
            fs[create_path(curr)] += int(a)

for item in fs:
    for item2 in fs:
        if item != item2 and item2.startswith(item):
            fs[item] += fs[item2]
    if fs[item] <= 100000:
        part1 += fs[item]

print(part1)
