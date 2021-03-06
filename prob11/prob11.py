handle = open("input.txt")

lines = handle.read().strip().split('\n')

equation = "-VAR OP VAR"
unknown = ''
"""
f = -k * x
k = -f / x
x = -f / k

always -a operation b
"""

for line in lines:
    (key, value) = line.split()
    if value == '?':
        equation = equation.replace("OP", '*' if key.lower() == 'f' else '/')
        unknown = key
    else:
        equation = equation.replace("VAR", value, 1)

print(unknown, "{0:.2f}".format(round(eval(equation), 2)))

handle.close()