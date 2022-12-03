
totalPoints = 0
with open("day02/input.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]

# python dictionary with possible outcomes
possibleSolutions = {
    "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6
}
for round in rounds:
    totalPoints = totalPoints + possibleSolutions[round]

print(totalPoints)
