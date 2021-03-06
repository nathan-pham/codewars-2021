handle = open("input.txt")
(height, damageheight, level) = handle.read().strip().split(' ')

if int(damageheight) == 0 or int(damageheight) > int(height):
  for i in range(int(height)):
    print('#')

else:
  for i in range(int(damageheight) - 2):
    print('#')
  level = str((int(level))/10)
  print('#' + '.' * int(level[0]) + '#' * (int(height) - int(damageheight) + 1))
