# https://www.codechef.com/DEC20B/problems/VACCINE2
# @author Akash Kumar


def get_risk_division(ages):
    """
    Function to count the people with high risk and the people with low risk
    :param ages: A list where ages[i] is the age of the ith person
    :return low_risk_count, high_risk_count: two integers
    """

    low_risk_count = sum(age >= 80 or age <= 9 for age in ages) 
    high_risk_count = len(ages) - low_risk_count

    return high_risk_count, low_risk_count

def get_days_required(ages, day_limit):
    """
    Function to count the days required for vaccine distribution
    :param ages: A list where ages[i] is the age of the ith person
    :return: The total number of days require for every person to be vaccinated
    """

    high_risk_count, low_risk_count = get_risk_division(ages)

    return high_risk_count // day_limit + (1 if high_risk_count % day_limit else 0) \
            + low_risk_count // day_limit + (1 if low_risk_count % day_limit else 0)

def main():
    """
    Main driver function for submission
    """

    # input T
    test_case_count = int(input())

    for _ in range(test_case_count):
        
        # input N and D
        n, day_limit = map(int, input().split())
        # input A
        ages = list(map(int, input().split()))

        if day_limit == 1:
            # since only one person can be vaccinated in a single day, 
            # we require as many days as there are people
            print(n)
        else:
            print(get_days_required(ages, day_limit))

def test_get_days_required():
    """
    Function to test the solution written in get_days_required()
    """

    assert get_days_required([10, 20, 30, 40, 50, 60, 90, 80, 100, 1], 1) == 10
    assert get_days_required([9, 80, 27, 72, 79], 2) == 3
    assert get_days_required([5, 90, 30, 70, 75], 10) == 2

    print("All sample test cases ran successfully")

def run(mode='submit'):
    """
    Function to run the function based on whether to test with 
    existing sample cases or to take input from the user
    :param mode: Mode for testing the code, takes either 'submit' or 'test' 
    """

    if mode == 'submit':
        main()
    elif mode=='test':
        test_get_days_required()
    else:
        print("Invalid run mode")


run('test')