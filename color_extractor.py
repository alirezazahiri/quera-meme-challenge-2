import matplotlib.image as img

filepath = input()

image = img.imread(filepath)

r, g, b = [], [], []

for row in image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

colors = []
precentage = {}

for i in range(len(r)):
    if not (f'{r[i]},{g[i]},{b[i]}' in colors):
        colors.append(f'{r[i]},{g[i]},{b[i]}')
        precentage[f'{r[i]},{g[i]},{b[i]}'] = 1
    else:
        precentage[f'{r[i]},{g[i]},{b[i]}'] += 1

LENGTH = len(colors)
colors = sorted(list(set(colors)))

for color in colors:
    print(color, ":", precentage[color])
