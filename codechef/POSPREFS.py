# https://www.codechef.com/DEC20B/problems/POSPREFS
# submission: https://www.codechef.com/viewsolution/40184257
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

def check_positive_prefixes(n, k, sequence):
    k_temp = 0
    for i in range(1, len(sequence)+1):
        if sum(sequence[:i]) > 0:
            k_temp += 1
    
    return True if k == k_temp else False

def test_positive_prefixes():
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