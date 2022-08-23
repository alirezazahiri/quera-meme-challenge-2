# constants
BUTTONS = (143.89110301918168, 108.79347420936433,
           120.5628637784213)  # Buttons
DRAKE = (188.62510583586817, 73.76777258615823, 8.482689955784126)  # Drake
TORNADO = (147.42635459973653, 102.35369296309604,
           104.47347260004449)  # Tornado
MICHAEL = (98.02298364354202, 90.400521714608, 90.57076635645798)  # Michael

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

for line in lines[:1]:
    splitted_line = line.split(") (")
    splitted_line[0] = splitted_line[0][1:]
    splitted_line[-1] = splitted_line[-1][:len(splitted_line[-1])-1]
    for rgb in splitted_line:
        r, g, b = rgb.split(", ")
        rgb_array.append((int(r), int(g), int(b)))

rgb_array = sorted(list(set(rgb_array)))

s_r, s_g, s_b = 0, 0, 0

for color in rgb_array:
    s_r += color[0]
    s_g += color[1]
    s_b += color[2]

s_r /= len(rgb_array)
s_g /= len(rgb_array)
s_b /= len(rgb_array)

distances = {
    "BUTTONS": (abs(BUTTONS[0]-s_r), abs(BUTTONS[1]-s_g), abs(BUTTONS[2]-s_b)),
    "DRAKE": (abs(DRAKE[0]-s_r), abs(DRAKE[1]-s_g), abs(DRAKE[2]-s_b)),
    "TORNADO": (abs(TORNADO[0]-s_r), abs(TORNADO[1]-s_g), abs(TORNADO[2]-s_b)),
    "MICHAEL": (abs(MICHAEL[0]-s_r), abs(MICHAEL[1]-s_g), abs(MICHAEL[2]-s_b)),
}

min_dis = (255, 255, 255)
last_key = ""

for key in distances:
    if distances[key] < min_dis:
        min_dis = distances[key]
        last_key = key 

print(ANSWERS[last_key])