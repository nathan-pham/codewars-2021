handle = open("input.txt")
data = handle.read().rstrip().split('\n')
number = data.pop(0)

data.reverse()

for i in range(int(number)):
    print(data[i])

handle.close()