# NOT SUBMITTED TO COMPETITION

handle = open("input.txt")
data = handle.read().strip().split('\n')
data.pop()

villagers = []

def protection(vpf):
    return int(vpf) * 10

def time_minutes(unformatted):
    (hours, minutes) = unformatted.split(':')
    return (int(hours) * 60) + int(minutes)

for line in data:
    (villager, applied, vpf) = line.strip().split()
    # (Protection means their VPF will last until a time greater than or equal to 17:00).

    if time_minutes(applied) + protection(vpf) <= time_minutes("17:00"):
        villagers.append(villager.split('-').pop())

if len(villagers) == 0:
    print("Blah, blah, blah, time to order delivery")
else:
    print(f"Villagers ({ ', '.join(villagers) }) look tasty")