#         [J]         [B]     [T]    
#         [M] [L]     [Q] [L] [R]    
#         [G] [Q]     [W] [S] [B] [L]
# [D]     [D] [T]     [M] [G] [V] [P]
# [T]     [N] [N] [N] [D] [J] [G] [N]
# [W] [H] [H] [S] [C] [N] [R] [W] [D]
# [N] [P] [P] [W] [H] [H] [B] [N] [G]
# [L] [C] [W] [C] [P] [T] [M] [Z] [W]
#  1   2   3   4   5   6   7   8   9 

stacks = {
    1: ["L", "N", "W", "T", "D"],
    2: ["C", "P", "H"],
    3: ["W", "P", "H", "N", "D", "G", "M", "J"],
    4: ["C", "W", "S", "N", "T", "Q", "L"],
    5: ["P", "H", "C", "N"],
    6: ["T", "H", "N", "D", "M", "W", "Q", "B"],
    7: ["M", "B", "R", "J", "G", "S", "L"],
    8: ["Z", "N", "W", "G", "V", "B", "R", "T"],
    9: ["W", "G", "D", "N", "P", "L"]
}

file = open("input.txt", "r")
lines = file.readlines()
answer = ""

for line in lines:
    # Move n from n to n
    numbers = [int(char) for char in line.split() if char.isdigit()]
    amount = numbers[0]
    fromStack = numbers[1]
    toStack = numbers[2]

    for i in range(amount):
        stacks[toStack].append(stacks[fromStack].pop())

for stack in stacks:
    answer += stacks[stack][-1]
print(answer)
