# https://www.codechef.com/DEC20B/problems/VACCINE1
# @author Akash Kumar

import math

def get_days_required(d1, v1, d2, v2, p):
    """
    Funcation to calculate the days required to produce p vaccines 
    as per the problem statent.
    :param d1: The day at which Company A starts producing vaccines
    :param v2: Number of vaccines Company A can produce in a day
    :param d2: The day at which Company B starts producing vaccines
    :param v2: Number of vaccines Company B can produce in a day
    :param p: Number of vaccines to be produced
    :return days_required: The number of days required to produce p vaccines
    """

    days_required = 0

    if d1 == d2:
        if d1 == 1:
            # in case both companies start producing vaccines on day 1
            # simply return the number of days required to produce together
            return math.ceil(p/(v1+v2)) 

        else:
            # in case they start after x days
            # add x to the number of days required to produce together
            return (d1-1) + math.ceil(p/(v1+v2))

    else:
        if d2 < d1:
            # d1 will contain the smaller value of d, 
            # i.e., the company that starts first
            d1, d2 = d2, d1
            v1, v2 = v2, v1
        
        # add the days on which no vaccines were produced
        days_required = d1 - 1

        # in case that p vaccines can be produced by company A itself
        # before company B starts producing vaccines
        if (d2-d1) * v1 >= p:
            return days_required + math.ceil(p / v1)

        # cover the days required and vaccines produced by company A
        # in case both company A and B are required
        days_required += d2-d1
        p -= (d2-d1) * (v1)

        # return the total amount of work required together
        return days_required + math.ceil(p/(v1+v2))


def test_get_days_required():
    """
    Function to test the solution function, get_days_required()
    """

    assert get_days_required(1, 2, 1, 3, 14) == 3
    assert get_days_required(5, 4, 2, 10, 100) == 9
    assert get_days_required(5, 4, 3, 2, 1) == 3

    print("All sample test cases ran successfully")


# # uncomment this line and comment the  input lines for testing
# test_get_days_required()

# take input and print the result
d1, v1, d2, v2, p = map(int, input().split())
print(get_days_required(d1, v1, d2, v2, p))

