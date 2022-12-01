data = open('day01/input.txt', 'r', encoding='utf-8').readlines()
current = 0
max = 0
for line in data:
    line = line.rstrip()  # remove \n from line
    if (line != ""):
        current = current + int(line)
        if (current > max):
            max = current
    else:
        current = 0

print(max)
