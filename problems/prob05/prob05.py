handle = open("input.txt")
data = handle.read().strip().split('\n')

total_duplicates = []
duplicates = {}
number = data.pop(0)

for i in range(int(number)):
    _date = data[i]
    (month, day, year) = _date.strip().split('/')
    formatted = f"{month}/{day}"
    duplicates[formatted] = duplicates.get(formatted, 0) + 1

for key, value in duplicates.items():
    if value > 1:
        total_duplicates.append(key)

if len(total_duplicates) == 0:
    print("0")
    print("duplicates: None")
else:
    print(len(total_duplicates))
    print("duplicates:", ' '.join(total_duplicates))

handle.close()