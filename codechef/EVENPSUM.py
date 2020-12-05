# https://www.codechef.com/DEC20B/problems/EVENPSUM
# @author Akash Kumar

def even_pair_count(a, b):
    return (a//2 if a%2==0 else a//2+1) * (b//2 if b%2==0 else b//2+1) \
            + (a//2) * (b//2)


test_case_count = int(input())

for _ in range(test_case_count):

    a, b = map(int, input().split())

    print(even_pair_count(a, b))