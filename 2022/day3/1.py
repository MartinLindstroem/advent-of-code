alphaLower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha = alphaLower + list("".join(alphaLower).upper())

itemPrios = {}
rucksack = []

prio = 0
prioSum = 0

for char in alpha:
    prio += 1
    itemPrios[char] = prio

file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    line = list(line.strip())
    halfRucksack = int((len(line) / 2))
    rucksack.append(line[0:halfRucksack])
    rucksack.append(line[halfRucksack:])
    for char in alpha:
        if char in rucksack[0] and char in rucksack[1]:
            prioSum += itemPrios[char]
    rucksack = []
print(prioSum)

