with open("day05/input.txt") as file:
    moves = [i for i in file.read().strip().split("\n")]


init = [

    ["V", "N", "F", "S", "M", "P", "H", "J"],
    ["Q", "D", "J", "M", "L", "R", "S"],
    ["B", "W", "S", "C", "H", "D", "Q", "N"],
    ["L", "C", "S", "R"],
    ["B", "F", "P", "T", "V", "M"],
    ["C", "N", "Q", "R", "T"],
    ["R", "V", "G"],
    ["R", "L", "D", "P", "S", "C", "Z"],
    ["F", "B", "P", "G", "V", "J", "S", "D"]
]

for move in moves:
    # get move info
    parts = move.split()
    amount = int(parts[1])
    src = int(parts[3])-1
    dst = int(parts[5])-1

    # move crates
    cratesToMOve = init[src][:amount]  # get crates that will be moved

    init[src] = init[src][amount:]
    init[dst] = list(reversed(cratesToMOve)) + init[dst]


for stack in init:
    print(stack[0])
