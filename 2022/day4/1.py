file = open("input.txt", "r")
lines = file.readlines()

sections = []
count = 0

for i, item in enumerate(lines):
    item = item.strip().split(",")
    for j, pair in enumerate(item):
        item[j] = pair.split("-")
    sections.append(item)

for section in sections:
    if (int(section[0][0]) <= int(section[1][0]) and int(section[0][1]) >= int(section[1][1])) or (int(section[1][0]) <= int(section[0][0]) and int(section[1][1]) >= int(section[0][1])):
        count += 1
    # print(section[0], section[1], count)

print(count)