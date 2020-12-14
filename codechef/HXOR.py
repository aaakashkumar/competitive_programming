# https://www.codechef.com/DEC20B/problems/HXOR
# @author Akash Kumar

def get_two_to_the_power_p(n):
    return 1<<(len(bin(n))-2-1)

def get_lexicographically_smallest_sequence(n, x, sequence):
    
    i = 0
    j = 1

    while sequence[i] == 0:
        i += 1
        j = i + 1

    while x != 0:

        if j == n-1 and sequence[i] == 0:
            break

        two_raised_to_p = get_two_to_the_power_p(sequence[i])
        
        sequence[i] ^= two_raised_to_p

        if n == 2:
            sequence[j] ^= two_raised_to_p
            x -= 1

        else:
            while j <= n-1:
                if sequence[j] ^ two_raised_to_p > sequence[j]:
                    j += 1
                else:
                    break
            
            if j == n:
                sequence[j-1] ^= two_raised_to_p
            else:
                sequence[j] ^= two_raised_to_p

            x -= 1

            if sequence[i] == 0:
                i += 1
                j = i + 1
        
    if x != 0:
        if x % 2 == 0:
            return sequence

        else:
            if n == 2:
                two_raised_to_p = get_two_to_the_power_p(sequence[i])
                sequence[i] ^= two_raised_to_p
                sequence[j] ^= two_raised_to_p
            else:
                return sequence

    return sequence

def main():
    """
    Main driver function for submission
    """

    # input T
    test_case_count = int(input())

    for _ in range(test_case_count):

        # input N and X
        n, x = map(int, input().split())

        # input sequence A
        a = list(map(int, input().split()))

        print(*get_lexicographically_smallest_sequence(n, x, a))

def test_lexicographically_smallest_sequence():
    # test cases with n > 2 
    assert get_lexicographically_smallest_sequence(3, 3, [2, 2, 3]) == [0, 0, 3]
    assert get_lexicographically_smallest_sequence(3, 5, [4, 8, 16]) == [0, 0, 28]
    assert get_lexicographically_smallest_sequence(3, 3, [4, 8, 16]) == [0, 0, 28]
    assert get_lexicographically_smallest_sequence(4, 4, [2, 5, 5, 9]) == [0, 0, 0, 11]
    assert get_lexicographically_smallest_sequence(4, 6, [2, 5, 5, 9]) == [0, 0, 0, 11]
    assert get_lexicographically_smallest_sequence(5, 4, [10, 11, 12, 13, 14]) == [0, 0, 4, 4, 14]
    
    # test cases with n = 2
    assert get_lexicographically_smallest_sequence(2, 4, [4, 16]) == [1, 21]
    assert get_lexicographically_smallest_sequence(2, 3, [4, 6]) == [0, 2]
    assert get_lexicographically_smallest_sequence(2, 4, [4, 6]) == [1, 3]
    print("The test case ran successfully")

def run(mode='submit'):
    """
    Function to run the function based on whether to test with 
    existing sample cases or to take input from the user
    :param mode: Mode for testing the code, takes either 'submit' or 'test' 
    """

    if mode == 'submit':
        main()
    elif mode=='test':
        test_lexicographically_smallest_sequence()
    else:
        print("Invalid run mode")


run('test')