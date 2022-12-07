with open("day06/input.txt") as file:
    input = list([i for i in file.read().strip()])


buffer = set()
size = 4
count = 0


def repeat(input):
    buf = []
    for i in input:
        if i not in buf:
            buf.append(input.count(i))


for char in input:
    if (len(buffer) < size):  # if buffer is smaller than 4, add chars, if they repeat clear buffer, if dont, stop
        buffer.add(char)
        count += 1
        if (repeat(buffer)):
            buffer.clear()
    else:
        print(0)

print(count)
