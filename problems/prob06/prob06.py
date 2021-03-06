handle = open("input.txt")
encrypted = handle.read().strip().split('\n').pop()

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
cipher = "FGHIJKLMNOPQRSTUVWXYZABCDE "

decode = ""
for i in range(len(encrypted)):
    num = cipher.find(encrypted[i])
    decode += text[num]

print(decode)

handle.close()