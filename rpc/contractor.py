filename = input()

color_rpc_dict = {}

with open(filename, "r") as file:
    for line in file:
        color_str, prc = line.split(" : ")
        prc = int(prc)
        color = [int(_) for _ in color_str.split(",")]
        color = (color[0], color[1], color[2])
        color_rpc_dict[color] = prc

print(filename, "= {", end="")
for item in color_rpc_dict:
    print(item, ":" , color_rpc_dict[item], ",")

print("}")