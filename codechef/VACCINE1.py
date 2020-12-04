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

        days_required += d2-d1
        p -= (d2-d1) * (v1)

        return days_required + math.ceil(p/(v1+v2))


d1, v1, d2, v2, p = map(int, input().split())
print(get_days_required(d1, v1, d2, v2, p))

