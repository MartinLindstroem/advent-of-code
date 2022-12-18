file = open("input.txt", "r")
lines = file.readlines()
calories = 0
biggest = 0

for line in lines:
    if line != "\n":
        calories += int(line)
        if calories > biggest:
            biggest = calories
    else:
        calories = 0

print(biggest)
