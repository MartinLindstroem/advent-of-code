alphaLower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha = alphaLower + list("".join(alphaLower).upper())

itemPrios = {}
groups = []
group = []

prio = 0
prioSum = 0

for char in alpha:
    prio += 1
    itemPrios[char] = prio

file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    line = line.strip()
    group.append(line)
    if len(group) > 2:
        groups.append(group)
        group = []
        continue

for group in groups:
    for char in alpha:
        if char in group[0] and char in group[1] and char in group[2]:
            prioSum += itemPrios[char]

print(prioSum)

