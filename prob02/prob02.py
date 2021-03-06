pie = 3.1415926536

handle = open("input.txt")
data = handle.read().strip().split()

height = float(data[0])
radius = float(data[1])

def volume(z, h):
    return "{0:.2f}".format(pie * z * z * h)
    
print(volume(radius, height), "cubic inches")

handle.close()