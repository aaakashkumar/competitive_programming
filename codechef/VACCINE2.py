# https://www.codechef.com/DEC20B/problems/VACCINE2
# @author Akash Kumar


def get_risk_division(ages):
    low_risk_count = sum(age >= 80 or age <= 9 for age in ages) 
    high_risk_count = len(ages) - low_risk_count
    return high_risk_count, low_risk_count

def get_days_required(ages, day_limit):
    high_risk_count, low_risk_count = get_risk_division(ages)
    return high_risk_count // day_limit + (1 if high_risk_count % day_limit) \
            + low_risk_count // day_limit + (1 if low_risk_count % day_limit)

# input T
test_case_count = int(input())

for _ in range(test_case_count):
    
    # input N and D
    n, day_limit = map(int, input().split())
    # input A
    ages = list(map(int, input().split()))

    if day_limit == 1:
        print(n)
    else:
        print(get_days_required(ages, day_limit))
