# https://www.codechef.com/DEC20B/problems/POSPREFS
# submission: https://www.codechef.com/viewsolution/40183918
# @author Akash Kumar

def get_postive_prefix_array(n, k):
    sequence = list(range(1, n+1))

    if k == n:
        return sequence

    for index, number in enumerate(sequence):
        if number % 2 == 0: 
            sequence[index] = -number
        
        else:
            k -= 1

        if k == n-(index+1) or k == 0:
            break
    
    if k == 0:
        index += 1
        while index < n:
            sequence[index] = -sequence[index]
            index += 1

    return sequence


# input T
test_case_count = int(input())

for _ in range(test_case_count):

    # input N and K
    n, k = map(int, input().split())

    print(*get_postive_prefix_array(n, k))
