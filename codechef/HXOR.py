# https://www.codechef.com/DEC20B/problems/HXOR
# @author Akash Kumar

def get_two_to_the_power_p(n):
    """
    Returns 2 to the power p, as per the problem statement.
    
    p is nothing but the highest power of 2 for the given number n.
    For example, binary of the number 7 is 0111. Here, the highest 
    bit of 1 is at the position 3 from the right. Therefore, p should be 
    3-1, or 2, since we start from 0.

    :param n: An integer
    :return: 2 to the power p
    """
    return 1<<(len(bin(n))-2-1)

def get_lexicographically_smallest_sequence(n, x, sequence):
    """
    Function to calculate the lexicographically smallest sequence as
    per the problem statement. 

    :param n: the number of elements in the sequence
    :param x: the number of operations to be done
    :param sequence: list of integers in the sequence, A1, A2, ..., AN
    :return sequence: the sequence, operated x times to obtain the 
    lexicographically smallest sequence
    """
    
    # initialize i and j to be the first two numbers in the sequence
    i = 0
    j = 1

    while x != 0:

        # break out of the loop if i and j are the last two numbers
        # and i is at it's smallest (i.e., 0)
        if j == n-1 and i == j-1 and sequence[i] == 0:
            break

        # if i is 0, no point in operating it
        elif sequence[i] == 0:
            i += 1
            j = i + 1
            continue

        two_raised_to_p = get_two_to_the_power_p(sequence[i])
        
        sequence[i] ^= two_raised_to_p

        if n == 2:
            # bound to perform xor on the first two numbers if n equals 2
            sequence[j] ^= two_raised_to_p
            x -= 1
            continue

        else:
            
            while j <= n-1:
                # find the next number in the range 1+1 to n-1
                # which, upon xorring with 2**p, does not increase the value
                if sequence[j] ^ two_raised_to_p > sequence[j]:
                    j += 1
                else:
                    break
            
            if j == n:
                # if none of the numbers are decreased, incrementing the
                # last number is the least costly
                sequence[j-1] ^= two_raised_to_p
            else:
                sequence[j] ^= two_raised_to_p

            x -= 1
        
    if x != 0:
        if x % 2 == 0:
            # the same sequence can be obtained if an even number of
            # operations are left
            return sequence

        else:
            if n == 2:
                # if an odd number of operations are left for n = 2
                # simply xor the bits with 1
                two_raised_to_p = get_two_to_the_power_p(sequence[i])
                sequence[i] ^= two_raised_to_p
                sequence[j] ^= two_raised_to_p
            else:
                # if x is ≥ 3, the same number can be obtained
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
    """
    Function to test the solution written in get_lexicographically_smallest_sequence()
    A copyable version is  provided at the bottom of this file to test from the console.
    """
    # test cases with n > 2 
    # assert get_lexicographically_smallest_sequence(3, 3, [2, 2, 3]) == [0, 0, 3]
    # assert get_lexicographically_smallest_sequence(3, 5, [4, 8, 16]) == [0, 0, 28]
    # assert get_lexicographically_smallest_sequence(3, 3, [4, 8, 16]) == [0, 0, 28]
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


"""
Sample test case

9
3 3
2 2 3
3 5
4 8 16
3 3
4 8 16
4 4
2 5 5 9
4 6
2 5 5 9
5 4
10 11 12 13 14
2 4
4 16
2 3
4 6
2 4
4 6

"""