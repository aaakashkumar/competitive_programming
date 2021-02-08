
t = int(input())

for test_case_count in range(t):
    n = int(input())
    s = input()

    funny_word_list = list()
    funny_word_set = set()

    intermediate_str = []
    for index, character in enumerate(s):   # O(n)
        if index == len(s)-1:
            intermediate_str.append(character)
        if character == " " or index == len(s)-1:
            intermediate_str = ''.join(intermediate_str)
            funny_word_list.append(intermediate_str)
            funny_word_set.add(intermediate_str)
            intermediate_str = []
        else:
            intermediate_str.append(character)

    good_team_name_count = 0
    for i in range(len(funny_word_list)-1): # O(n^2)
        for j in range(i+1, len(funny_word_list)):
            if funny_word_list[i][0] == funny_word_list[j][0]:
                continue

            if (funny_word_list[i][0] + funny_word_list[j][1:] not in funny_word_set) and \
                (funny_word_list[j][0] + funny_word_list[i][1:] not in funny_word_set):
                good_team_name_count += 2

    print(good_team_name_count)

