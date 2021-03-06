import math

handle = open("input.txt")
(material, surface) = handle.read().strip().split(' ')

surface_map = ["rubber", "wood", "steel"]
friction_table = {
    "concrete": [0.90, 0.62, 0.57],
    "wood": [0.80, 0.42, 0.30],
    "steel": [0.70, 0.30, 0.74],
    "rubber": [1.15, 0.80, 0.70],
    "ice": [0.15, 0.05, 0.03]
}

coefficient = friction_table[surface.lower()][surface_map.index(material.lower())]

coefficient
min_slope = round(math.degrees(math.atan(coefficient)), 1)

print("{0:.2f}".format(coefficient), min_slope)

handle.close()