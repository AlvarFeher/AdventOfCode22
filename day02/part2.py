# same as first part with different conditions
totalPoints = 0
with open("day02/input.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]

# python dictionary with desired outcome results
possibleSolutions = {
    "A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7
}
for round in rounds:
    totalPoints = totalPoints + possibleSolutions[round]

print(totalPoints)
