# https://www.codechef.com/DEC20B/problems/POSPREFS
# @author Akash Kumar

def get_postive_prefix_array(n, k):
    multiplier = -1 if k % 2 == 0 else 1
    sequence = list()

    for i in range(1, k+1):
        sequence.append(i*multiplier)
        multiplier *= -1

    sequence += list(-x for x in range(k+1, n+1))

    return sequence


# input T
test_case_count = int(input())

for _ in range(test_case_count):

    # input N and K
    n, k = map(int, input().split())

    print(*get_postive_prefix_array(n, k))