# Maximise Function
# https://www.codechef.com/FEB21C/problems/MAXFUN
# @author Akash Kumar


def get_maximum_triple_sum(a, n):
    """
    Returns the maximum sum possible as per the problem statement
    :param a: the array
    :param n: number of elements in the array
    """
    if n == 3:
        # if only three numbers are present, choose all
        return abs(a[0]-a[1]) + abs(a[1]-a[2]) + abs(a[2]-a[0])
    
    max_value_index = 0
    min_value_index = 0

    for index in range(1, n):
        if a[index] > a[max_value_index]: max_value_index = index
        if a[index] < a[min_value_index]: min_value_index = index
    
    middle_index = None
    for index in range(n):
        if index != min_value_index and index != max_value_index:
            middle_index = index
            break
    
    # maximum number can be obtained if two of the 
    # numbers are the minimum and maximum number in
    # the array. the third number can be any other 
    # number in the array
    return abs(a[min_value_index]-a[middle_index]) \
        + abs(a[middle_index]-a[max_value_index])  \
        + a[max_value_index]-a[min_value_index]


t = int(input())

for test_case_count in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(get_maximum_triple_sum(a, n))
    
