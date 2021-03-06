import math

handle = open("input.txt")
data = handle.read().strip().split('\n')

(minions, cockpit, body, pods) = data

def sphere_volume(cockpit):
    return math.pi * (4/3) * (float(cockpit)**3)

def cylinder_volume(body):
    (radius, height) = body.split()
    return math.pi * float(height) * (float(radius)**2)

def pyramid_volume(pods):
    (length, width, height) = pods.split()
    return (1/3) * float(length) * float(width) * float(height)

volume = {
    "Cockpit": sphere_volume(cockpit) - (2.2 + 4.1),
    "Body":  cylinder_volume(body) - 12.1,
    "Pods": pyramid_volume(pods) * 2,
    "Minions Need": float(minions) * 1.2
}

total_volume = 0
for (key, value) in volume.items():
    rounded = round(value, 2)
    print(key, "{0:.2f}".format(rounded))
    if key != "Minions Need":
        total_volume += rounded

accepted = total_volume - volume["Minions Need"]
print("PLAN", "ACCEPTED" if accepted >= 0 else "REJECTED")

handle.close()