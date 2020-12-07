# https://www.codechef.com/DEC20B/problems/POSPREFS
# submission: https://www.codechef.com/viewsolution/40184257
# @author Akash Kumar

"""
Since the problem statement is poorly explained on Codechef, the problem statement
has been discussed here. There are two values given, N and K. We have to return a
sequence of N numbers, say A, such that for every index i of A, the value of A[i] 
is either -i or i. The complicated part is, there have to be exactly K values of i
such that, if you sum all the values from A[0] to A[i], you'll get a positive sum.
There can be no less and no greater than K values, for which the sum from A[0] to 
A[i] is positive.

For example, let N = 10 and K = 8. In this case, [1, -2, 3, -4, 5, 6, 7, 8, 9, 10] 
is a correct solution since there are exactly K values for which the sum from A[0]
to A[i] is positive, which are 1, 3, 5, 6, 7, 8, 9, 10.

Similarly for N = 5 and K = 2, [1, -2, 3, -4, -5] is a correct solution, as 1 is 
positive and 1+(-2)+3 is positive, but 1+(-2) or 1+(-2)+3+(-4) or 1+(-2)+3+(-4)
are negative.
"""


def get_postive_prefix_array(n, k):
    """
    Function to generate the positive prefix array
    :param n: the number of elements required in the result
    :param k: the exact number of elements, when which summed should be positive
    :return sequence: a sequence such that an element at index i can take only the values
    i or -i, and there are exactly k elements whose sum is positive
    """

    # initialize sequence to an array of [1,2,...,n]
    sequence = list(range(1, n+1))

    # if k equals n, all numbers will be positive
    if k == n:
        return sequence

    for index, number in enumerate(sequence):

        if number % 2 == 0: 
            # if we take the odd numbers as positive
            # and the even numbers as negative, we keep the sum close to 0.
            # by keeping the sum close to 0, we ensure that
            # if we've obtained k numbers such that their sum(sequence[:k]) is positive
            # then we can safely make the rest of the numbers negative
            sequence[index] = -number
        
        else:
            # another correct k value found if odd number
            k -= 1

        if k == n-(index+1) or k == 0:
            # if there are exactly k numbers left, they all have to be positive
            break
    
    if k == 0:
        # if k equals 0, it means k values have been found, but the array has not 
        # finished traversal, so make the rest of the values negative
        index += 1
        while index < n:
            sequence[index] = -sequence[index]
            index += 1

    return sequence

def check_positive_prefixes(n, k, sequence):
    """
    Function to check if a sequence satisfies the problem statement
    :param n: the number of elements required in the result
    :param k: the exact number of elements, when which summed should be positive
    :return: true if it satisfies the problem statement, else false
    """

    k_temp = 0
    for i in range(1, len(sequence)+1):
        if sum(sequence[:i]) > 0:
            k_temp += 1
    
    return True if k == k_temp else False

def test_positive_prefixes():
    """
    Function to test some sample cases for the problem
    """

    assert check_positive_prefixes(3, 3, get_postive_prefix_array(3, 3))
    assert check_positive_prefixes(10, 7, get_postive_prefix_array(10, 7))
    assert check_positive_prefixes(10, 8, get_postive_prefix_array(10, 8))
    assert check_positive_prefixes(5, 2, get_postive_prefix_array(5, 2))
    print("All sample test cases ran successfully")

def main():
    """
    Main driver function for submission
    """

    # input T
    test_case_count = int(input())

    for _ in range(test_case_count):

        # input N and K
        n, k = map(int, input().split())

        print(*get_postive_prefix_array(n, k))

def run(mode='submit'):
    """
    Function to run the function based on whether to test with 
    existing sample cases or to take input from the user
    :param mode: Mode for testing the code, takes either 'submit' or 'test' 
    """

    if mode == 'submit':
        main()
    elif mode=='test':
        test_positive_prefixes()
    else:
        print("Invalid run mode")


run('test')