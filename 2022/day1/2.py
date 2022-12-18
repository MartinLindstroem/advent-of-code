file = open("input.txt", "r")
lines = file.readlines()
calories = 0

myList = []

for line in lines:
    if line != "\n":
        calories += int(line)
    else:
        myList.append(calories)
        calories = 0
sortedList = myList[0:3].sort()
print(sum(sorted(myList, reverse=True)[0:3]))
