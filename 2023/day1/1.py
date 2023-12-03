file = open("input.txt", "r")
lines = file.readlines()

calibration_value = None
total = 0
numbers = []


for line in lines:
    line = line.strip()
    
    for char in line:
        if char.isdigit():
            numbers.append(char)
    calibration_value = numbers[0] + numbers[-1]
    total += int(calibration_value)

    numbers = []

print(total)
