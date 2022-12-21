def isDuplicate(chars):
    for char in chars:
        if chars.count(char) > 1:
            return True
    return False

def message_marker():
    file = open("input.txt", "r")
    data = file.readlines()

    start_index = 0

    for char in data[0]:
        end_index = start_index + 14
        char_set = data[0][start_index:end_index]

        if not isDuplicate(char_set):
            return (end_index)

        start_index += 1

print(message_marker())