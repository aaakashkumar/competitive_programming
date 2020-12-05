# https://www.codechef.com/DEC20B/problems/EVENPSUM
# submission: https://www.codechef.com/DEC20B/submit/EVENPSUM
# @author Akash Kumar

def even_pair_count(a, b):
    """
    Function to find the number of pairs of positive integers (X,Y) 
    such that 1≤X≤A, 1≤Y≤B and X+Y is even.
    :param a: A positive integer
    :param b: A positive integer
    :return: number of pairs
    """
    return (a//2 if a%2==0 else a//2+1) * (b//2 if b%2==0 else b//2+1) \
            + (a//2) * (b//2)

# input T
test_case_count = int(input())

for _ in range(test_case_count):

    # input A and B
    a, b = map(int, input().split())

    print(even_pair_count(a, b))