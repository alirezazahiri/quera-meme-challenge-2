import random

answers = ["Buttons",
           "Drake",
           "Tornado",
           "Michael"]

lines = []
_ = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    if _ == 0:
        _ += 1
        continue
    lines.append(line.strip())

i = 0
while i < 10:
    i += 1
    rand_num = random.randint(0, 3)

print(answers[rand_num])
