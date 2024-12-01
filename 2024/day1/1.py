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

def calculate_dist():
    dist_diff = 0
    distances = split_list(lines)

    for i in range(len(distances[0])):
        dist_diff += distances[0][i] - distances[1][i] if distances[0][i] >= distances[1][i] else distances[1][i] - distances[0][i]
    
    print(dist_diff)



calculate_dist()