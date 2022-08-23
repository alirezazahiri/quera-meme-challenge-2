# lines = []
rgb_array = []
i = 0
color_rpc_dict = {}

while True:
    i += 1
    try:
        line = input()
    except EOFError:
        break
    if i % 2 == 0:
        continue
    splitted_line = line.strip().split(") (")
    splitted_line = splitted_line[1:len(splitted_line[-1])-1:1]
    for rgb in splitted_line:
        r, g, b = rgb.split(", ")
        if not(int(r), int(g), int(b)) in rgb_array:
            rgb_array.append((int(r), int(g), int(b)))
            color_rpc_dict[(int(r), int(g), int(b))] = 1
        else:
            color_rpc_dict[(int(r), int(g), int(b))] += 1
    


# for rgb in splitted_line:
#     r, g, b = rgb.split(", ")
#     if not(int(r), int(g), int(b)) in rgb_array:
#         rgb_array.append((int(r), int(g), int(b)))
#         color_rpc_dict[(int(r), int(g), int(b))] = 1
#     else:
#         color_rpc_dict[(int(r), int(g), int(b))] += 1

s = 0
for key in rgb_array:
    if color_rpc_dict[key] < 5:
        del color_rpc_dict[key]
        continue
    print(key, ":", color_rpc_dict[key])
    s += color_rpc_dict[key]
print(s)