file = open("input.txt", "r")
lines = file.readlines()

def split_list(input):
    list1 = []
    list2= []
    for i in range(len(input)):
        input[i] = input[i].strip().split("   ")
        list1.append(int(input[i][0]))
        list2.append(int(input[i][1]))
    list1.sort()
    list2.sort()

    return [list1, list2]

def calc_similarity_score():
    similarty_score = 0
    distances = split_list(lines)

    for i in range(len(distances[0])):
        similarty_score += distances[0][i] * distances[1].count(distances[0][i])
    
    print(similarty_score)

calc_similarity_score()