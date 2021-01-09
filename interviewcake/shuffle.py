# https://www.interviewcake.com/question/python3/shuffle?course=fc1&section=greedy
# @author Akash Kumar
# This is a semi-famous algorithm known as the Fisher-Yates shuffle 
# (sometimes called the Knuth shuffle).

import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    if len(the_list) <= 1:
        return the_list

    # Shuffle the input in place
    for i in range(len(the_list)):
        shuffle_index = get_random(i, len(the_list)-1)

        if i != shuffle_index:
            the_list[i], the_list[shuffle_index] = the_list[shuffle_index], the_list[i]

    return the_list


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)

