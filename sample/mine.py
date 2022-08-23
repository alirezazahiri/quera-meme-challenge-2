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

cache = {}
sum_ = 0
for line in lines:
    for item in line.split(') (')[1:-1]:
        color = item.replace(' ','')
        sum_ += 1
        try:
            cache[color]+=1
            
        except:
            cache[color]=1

print(len(cache))

trash_hold = int(sum_* 0.005)

for key in list(cache.keys())[:]:
    if cache[key]< trash_hold:
        del cache[key]
print(len(cache))


