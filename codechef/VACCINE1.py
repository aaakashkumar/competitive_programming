# https://www.codechef.com/DEC20B/problems/VACCINE1
# @author Akash Kumar

import math

def get_days_required(d1, v1, d2, v2, p):

    days_required = 0

    if d1 == d2:
        if d1 == 1:
            return math.ceil(p/(v1+v2)) 
        else:
            return (d1-1) + math.ceil(p/(v1+v2))

    else:
        if d2 < d1:
            d1, d2 = d2, d1
            v1, v2 = v2, v1
        
        days_required = d1 - 1

        if (d2-d1) * v1 >= p:
            return days_required + math.ceil(p / v1)

        days_required += d2-d1
        p -= (d2-d1) * (v1)

        return days_required + math.ceil(p/(v1+v2))


def test_get_days_required():

    assert get_days_required(1, 2, 1, 3, 14) == 3
    assert get_days_required(5, 4, 2, 10, 100) == 9
    assert get_days_required(5, 4, 3, 2, 1) == 3

    print("All sample test cases ran successfully")


# # uncomment this line and comment the  input lines for testing
# test_get_days_required()

d1, v1, d2, v2, p = map(int, input().split())
print(get_days_required(d1, v1, d2, v2, p))

