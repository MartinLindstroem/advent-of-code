file = open("input.txt", "r")
lines = file.readlines()
spelled_out_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

calibration_value = None
total = 0
numbers = []


for line in lines[5:6]:
    line = line.strip()

    # for char in line:
    #     if char.isdigit():
    #         numbers.append(char)
    # calibration_value = numbers[0] + numbers[-1]
    # total += int(calibration_value)

    for nr in spelled_out_numbers:
        if nr in line:
            print(line.count(nr), nr)
            numbers.append(spelled_out_numbers[nr])
        if spelled_out_numbers[nr] in line:
            print(line.count(spelled_out_numbers[nr]), spelled_out_numbers[nr])
            numbers.append(spelled_out_numbers[nr])
    


    # print(numbers)
    # numbers = []

# print(total)
