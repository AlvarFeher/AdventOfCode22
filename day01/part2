data = open('day01/input.txt', 'r', encoding='utf-8').readlines()
current = 0
max = 0
sums = []
for line in data:
    line = line.rstrip()  # remove \n from line
    if (line != ""):
        current = current + int(line)
    else:
        sums.append(current)
        current = 0

sums.sort()
print(sums[-1], "  ", sums[-2], "  ", sums[-3])
print("total: ", sums[-1] + sums[-2] + sums[-3])
