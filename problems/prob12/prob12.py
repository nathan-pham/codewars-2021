handle = open("input.txt")

(weapon, speed, unit_d, per, unit_t) = handle.read().strip().split()

"""
MILES, KILOMETERS, YARDS, FEET, METERS, INCHES,
CENTIMETERS, HOUR, MINUTE, SECOND.

GIANT-SLINGSHOT 1980.00 FEET PER MINUTE
1 meter is equal to 3.28 feet for the purposes of this problem
"""

def get_height(speed):
    return (speed**2) / (2 * 9.805)

# mult factor to convert into proper units
conversions = {
    # time => s
    "hour": 1 / (60 * 60),
    "minute": 1 / 60,
    "second": 1,

    # distance => m
    "miles": 5280 / 3.28,
    "kilometers": 1000,
    "yards": 3 / 3.28,
    "feet": 1 / 3.28,
    "meters": 1,
    "inches": 1 / (12 * 3.28),
    "centimeters": 1 / 100
}

def convert(value, distance, duration):
    return float(value) * conversions[distance.lower()] * conversions[duration.lower()]

expected = get_height(convert(speed, unit_d, unit_t))

result = "SUCCESS"
if expected < 25:
    result = "SPLAT"
elif expected > 50:
    result = "OUCH"

print(weapon, "will launch the messenger", "{0:.2f}".format(round(expected, 2)), f"meters high, {result}!")

handle.close()