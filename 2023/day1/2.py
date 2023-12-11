import re

file = open("input.txt", "r")
# file = open("test_input.txt", "r")
lines = file.readlines()
spelled_out_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

pattern = r'(?:one|two|three|four|five|six|seven|eight|nine|\d)'
total = 0

for line in lines:
    line = line.strip()
    numbers = re.findall(pattern, line)
    print(line)
    
    for number in numbers:
        for alpha_num in spelled_out_numbers:
            if number == alpha_num:
                idx = numbers.index(number)
                numbers[idx] = spelled_out_numbers[number]
    
    calibration_value = numbers[0] + numbers[-1]
    # print(calibration_value)
    total += int(calibration_value)

print(total)
