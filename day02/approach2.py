# first approach i thought of, it needs a lot of if statements tho

totalPoints = 0
plays = []  # array storing both plays in a round -> plays[A,X]

with open("day02/input.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]

for round in rounds:
    plays = round.split()
    if plays[0] == "A" & plays[1] == "X":
        totalPoints = totalPoints + 4
    # do al cases and that's it, way better with the dictionary
