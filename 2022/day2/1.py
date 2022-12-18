# A: Rock 1
# B: Paper 2
# C: Scissors 3

# X: Rock 1
# Y: Paper 2
# Z: Scissors 3

# Win: 6 points
# Draw: 3 points
# Lose: 0 points

file = open("input.txt", "r")
lines = file.readlines()
score = 0

for line in lines:
    line = line.replace("\n", "").split(" ")
    if line[0] == "A":
        if line[1] == "X":
            score += 4
        if line[1] == "Y":
            score += 8
        if line[1] == "Z":
            score += 3
    if line[0] == "B":
        if line[1] == "X":
            score += 1
        if line[1] == "Y":
            score += 5
        if line[1] == "Z":
            score += 9
    if line[0] == "C":
        if line[1] == "X":
            score += 7
        if line[1] == "Y":
            score += 2
        if line[1] == "Z":
            score += 6
print(score)

