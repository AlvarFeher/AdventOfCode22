with open("day04/input.txt") as file:
    pairs = [i for i in file.read().strip().split("\n")]
count = 0
for pair in pairs:
    margins = pair.split(",")  # get both margins
    p1 = margins[0].split("-")  # get limits of p1
    p2 = margins[1].split("-")  # get limits of p2
    # convert to int
    a = int(p1[0])
    b = int(p1[1])
    c = int(p2[0])
    d = int(p2[1])
    # check
    if (b >= c and b <= d) or (d >= a and d <= b):  # now is any overlap
        count += 1

print(count)
