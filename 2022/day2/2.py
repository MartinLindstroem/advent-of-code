# A: Rock 1
# B: Paper 2
# C: Scissors 3

# X: Lose
# Y: Draw
# Z: Win

# Win: 6 points
# Draw: 3 points
# Lose: 0 points

options = {
    "A": 1 , # Rock
    "B": 2,  # Paper
    "C": 3   # Scissor
}

outcomeScore = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

file = open("input.txt", "r")
lines = file.readlines()
score = 0

for line in lines:
    line = line.replace("\n", "").split(" ")
    if line[0] == "A":
        if line[1] == "X":
            score += options["C"] + outcomeScore["lose"]
        if line[1] == "Y":
            score += options[line[0]] + outcomeScore["draw"]
        if line[1] == "Z":
            score += options["B"] + outcomeScore["win"]
    if line[0] == "B":
        if line[1] == "X":
            score += options["A"] + outcomeScore["lose"]
        if line[1] == "Y":
            score += options["B"] + outcomeScore["draw"]
        if line[1] == "Z":
            score += options["C"] + outcomeScore["win"]
    if line[0] == "C":
        if line[1] == "X":
            score += options["B"] + outcomeScore["lose"]
        if line[1] == "Y":
            score += options["C"] + outcomeScore["draw"]
        if line[1] == "Z":
            score += options["A"] + outcomeScore["win"]
print(score)

