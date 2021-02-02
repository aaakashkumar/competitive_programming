# Top Scores
# https://www.interviewcake.com/question/python3/top-scores?course=fc1&section=hashing-and-hash-tables
# @author Akash Kumar


import unittest


def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time
    score_occurrence_counts = [0] * (highest_possible_score+1)
    
    for score in unsorted_scores:
        score_occurrence_counts[score] += 1
        
    sorted_scores = []
    for score in range(len(score_occurrence_counts)-1, 0, -1):
        for score_count in range(score_occurrence_counts[score]):
            sorted_scores.append(score)
            

    return sorted_scores


















# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)