# Frog Sort
# https://www.codechef.com/FEB21C/problems/FROGS
# @author Akash Kumar

def get_frog_sort_step_count(n, w, l):
    """
    :param n: Number of frogs
    :param w: List of weights of the frogs at their respective index
    :param l: List of the amount a frog at the ith position can jump in one step
    """

    W_to_position = {}  # mapping from a wight to it's position (index)
    for index, weight in enumerate(w):
        W_to_position[weight] = index

    # print("W_to_position: ", W_to_position)

    step_count = 0
    
    for i in range(2, n+1):
        if W_to_position[i] > W_to_position[i-1]:
            continue
        
        temp_step_count = ((W_to_position[i-1] - W_to_position[i]) // l[W_to_position[i]]) + 1
        # print("steps required for ", i, ":", temp_step_count)

        step_count += temp_step_count
        W_to_position[i] += temp_step_count * l[W_to_position[i]]
    
    return step_count


test_case_count = int(input())

for test_case in range(test_case_count):
    n = int(input())
    w = list(map(int, input().split()))
    l = list(map(int, input().split()))

    print(get_frog_sort_step_count(n, w, l))