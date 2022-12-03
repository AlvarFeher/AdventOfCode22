
items = []
value = 0
repeValues = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
    "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
}


def compare(p1, p2, p3):
    for i in p1:
        for j in p2:
            if (i == j) & (i in p3):
                return i


with open("day03/input.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

# divide data into groups of 3
for i in range(0, len(data), 3):  # range(start, length, step increment)
    p1 = data[i]
    p2 = data[i+1]
    p3 = data[i+2]
    repe = compare(p1, p2, p3)
    value += repeValues[repe]

print(value)
