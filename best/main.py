import operator
from collections import Counter

# constants
BUTTONS = [
    (253, 253, 253),
    (178, 201, 239),
    (98, 113, 141),
    (199, 35, 67),
    (246, 215, 202),
]  # Buttons
DRAKE = [
    (255, 255, 255),
    (228, 181, 1),
    (198, 27, 8),
    (213, 157, 4),
    (240, 69, 5),
]  # Drake
TORNADO = [
    (158, 106, 90),
    (35, 23, 25),
    (139, 134, 150),
    (188, 128, 115),
    (123, 81, 73),
]  # Tornado
MICHAEL = [
    (22, 22, 27),
    (118, 102, 95),
    (35, 34, 40),
    (123, 115, 112),
    (144, 137, 132),
]  # Michael

ANSWERS = {
    "BUTTONS": "Buttons",
    "DRAKE": "Drake",
    "TORNADO": "Tornado",
    "MICHAEL": "Michael",
}

lines = []
i = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    if i == 0:
        i += 1
        continue
    lines.append(line.strip())

rgb_array = []

for line in lines:
    splitted_line = line.split(") (")
    splitted_line[0] = splitted_line[0][1:]
    splitted_line[-1] = splitted_line[-1][:len(splitted_line)-1]
    splitted_line = splitted_line[1:len(splitted_line)//2]
    for rgb in splitted_line:
        r, g, b = rgb.split(", ")
        rgb_array.append((int(r), int(g), int(b)))

rgb_array = [tup[0] for tup in Counter(rgb_array).most_common(100)]

s_r, s_g, s_b = 0, 0, 0

for color in rgb_array:
    s_r += color[0]
    s_g += color[1]
    s_b += color[2]

s_r /= len(rgb_array)
s_g /= len(rgb_array)
s_b /= len(rgb_array)


def distance_calc(collection=[]):
    r3_distances = []
    for tup in collection:
        r_dis = tup[0] - s_r
        g_dis = tup[1] - s_g
        b_dis = tup[2] - s_b
        r3_dis = r_dis**2 + g_dis**2 + b_dis**2
        r3_distances.append((r3_dis**.5)/len(collection))

    return sum(r3_distances)


distances = {
    "BUTTONS": distance_calc(BUTTONS),
    "DRAKE": distance_calc(DRAKE),
    "TORNADO": distance_calc(TORNADO),
    "MICHAEL": distance_calc(MICHAEL),
}

min_dis = 1000
last_key = ""

for key in distances:
    if distances[key] < min_dis:
        min_dis = distances[key]
        last_key = key

print(ANSWERS[last_key])
