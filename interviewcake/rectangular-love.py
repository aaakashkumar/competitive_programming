# Rectangular Love
# https://www.interviewcake.com/question/python3/rectangular-love?course=fc1&section=general-programming
# @author Akash Kumar

import unittest


def find_overlap(a1, a2, b1, b2):
    """
    Function to calculate the overlap formed by two lines, A and B

    :param a1: The starting point of line A
    :param a2: The ending point of line A
    :param b1: The starting point of line B
    :param b2: The ending point of line B
    :return starting_point, overlap: Returns the starting point of 
    the overlap region, as well as the overlap length. Returns None 
    for both in case there is no overlap
    """
    
    # ensure a1 is the lowest starting point
    if a1 > b1:
        a1, b1 = b1, a1
        a2, b2 = b2, a2
        
    # no overlap
    if a2 < b1:
        return None, None
        
    starting_point, overlap = None, None
        
    # to understand the following, draw some cases!
    if b2 <= a2:
        overlap = b2 - b1
        starting_point = b1
        
    elif b2 > a2:
        overlap = a2 - b1
        starting_point = b1
        
    return starting_point, overlap
        

def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles
    
    overlap_left_x, overlap_width = find_overlap(rect1['left_x'], rect1['left_x']+rect1['width'], 
                                                 rect2['left_x'], rect2['left_x']+rect2['width'])
    
    if overlap_width:
        overlap_bottom_y, overlap_height = find_overlap(rect1['bottom_y'], rect1['bottom_y']+rect1['height'],
                                                        rect2['bottom_y'], rect2['bottom_y']+rect2['height'])
                                                     
        if overlap_height:
            overlap_rectangle = {
                 # Coordinates of bottom-left corner
                'left_x'   : overlap_left_x,
                'bottom_y' : overlap_bottom_y,
            
                # Width and height
                'width'    : overlap_width,
                'height'   : overlap_height
            }
            
            return overlap_rectangle
        
    # return all as None in case there's no overlap
    return {'left_x':None, 'bottom_y':None, 'width':None, 'height':None}


















# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)