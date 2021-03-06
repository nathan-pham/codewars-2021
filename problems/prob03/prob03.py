handle = open("input.txt")
rows = handle.read().strip().split('\n')
found = False

for y in range(len(rows)):
    row = rows[y]
    for x in range(len(row)):
        if rows[y][x] == 'P':
            print(f"Ace, move fast, pigeon is at ({x}, {y})")
            found = True

if not found:
    print("No pigeon, try another map, Ace")

handle.close()