with open("day06/input.txt") as file:
    input = list([i for i in file.read().strip()])

    bufferSize = 4
    data = input

    buffer = set()
    endIndex = 0
    startIndex = 0

    while (len(buffer) < bufferSize):
        buffer.add(data[endIndex])
        endIndex += 1
        if (len(buffer) < (endIndex-startIndex)):
            startIndex += 1
            endIndex = startIndex
            buffer.clear()
    print(endIndex)
