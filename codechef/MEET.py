# Chef and Meetings
# https://www.codechef.com/FEB21C/problems/MEET
# @author Akash Kumar


def get_original_time(p):
    hours = []
    minutes = []

    current_index = 0
    while p[current_index] != ':':
        hours.append(p[current_index])
        current_index += 1
    
    current_index += 1
    while p[current_index] != ' ':
        minutes.append(p[current_index])
        current_index += 1

    hours = int("".join(hours))
    minutes = int("".join(minutes))

    if p[-2] == 'P' and hours != 12:
        hours += 12
    elif p[-2] == 'A' and hours == 12:
        hours = 0
        
    return hours * 3600 + minutes * 60

def get_friends_time(s):
    lower_hours = []
    lower_minutes = []
    current_index = 0

    while s[current_index] != ':':
        lower_hours.append(s[current_index])
        current_index += 1
    
    current_index += 1
    while s[current_index] != ' ':
        lower_minutes.append(s[current_index])
        current_index += 1

    lower_hours = int("".join(lower_hours))
    lower_minutes = int("".join(lower_minutes))

    if s[6] == 'P' and lower_hours != 12:
        lower_hours += 12
    elif s[6] == 'A' and lower_hours == 12:
        lower_hours = 0

    lower_slot_seconds = lower_hours * 3600 + lower_minutes * 60

    higher_hours = []
    higher_minutes = []
    current_index += 4

    while s[current_index] != ':':
        higher_hours.append(s[current_index])
        current_index += 1
    
    current_index += 1
    while s[current_index] != ' ':
        higher_minutes.append(s[current_index])
        current_index += 1

    higher_hours = int("".join(higher_hours))
    higher_minutes = int("".join(higher_minutes))

    if s[-2] == 'P' and higher_hours != 12:
        higher_hours += 12
    elif s[-2] == 'A' and higher_hours == 12:
        higher_hours = 0

    higher_slot_seconds = higher_hours * 3600 + higher_minutes * 60

    return lower_slot_seconds, higher_slot_seconds


test_case_count = int(input())

for test_case_number in range(test_case_count):
    friend_availability = []

    p = input()
    scheduled_time_seconds = get_original_time(p)
    # print(scheduled_time_seconds)

    n = int(input())

    for friend_count in range(n):
        friend_timings = input()
        friend_slot_start, friend_slot_end = get_friends_time(friend_timings)

        # print(friend_slot_start, friend_slot_end)

        if scheduled_time_seconds >= friend_slot_start and scheduled_time_seconds <= friend_slot_end:
            friend_availability.append('1')
        else:
            friend_availability.append('0')

    print("".join(friend_availability))