# this is a tree data structure ->               /dir0
#                                   dir 1     -   dir 2   -   file1
#                               dir 3 - file2     dir4
#                               file5            file6

# if a directory is found, get in, traverse it -> RECURSION
#  https://www.youtube.com/watch?v=YLHPABNNgZU

from collections import defaultdict
from functools import lru_cache
from pprint import pprint

input = open("day07/input.txt").readlines()


with open("day07/input.txt") as fin:
    blocks = ("\n" + fin.read().strip()).split("\n$ ")[1:]  # parse by blocks

path = []

dirSizes = defaultdict(int)
children = defaultdict(list)

# build tree by reading blocks of commands


def analyzeDirectories(block):
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])

        return

    absPath = "/".join(path)
    sizes = []
    for line in outputs:
        if not line.startswith("dir"):
            # if it is a number, store it (it is the size)
            sizes.append(int(line.split(" ")[0]))
        else:
            dirName = line.split(" ")[0]
            children[absPath].append(f"{absPath}/{dirName}")

    dirSizes[absPath] = sum(sizes)


for block in blocks:
    analyzeDirectories(block)

# to get the total size of a directory(with its subdirectories sizes), we must do DFS


def dfs(absPath):
    size = dirSizes[absPath]
    for child in children[absPath]:
        size += dfs(child)
    return size


sum = 0
for path in dirSizes:
    if dfs(path) <= 100000:
        sum += dfs(path)
print(sum)
