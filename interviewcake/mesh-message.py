import unittest
from collections import deque

def get_traversal_path(start_node, end_node, previous_node):
    
    traversal = []
    
    node = end_node
    while node != start_node:
        traversal.append(node)
        node = previous_node[node]
    traversal.append(start_node)
    
    return traversal[::-1]

def get_path(graph, start_node, end_node):

    if not graph.get(start_node):
        raise Exception("Start node is not present in the graph")
    if not graph.get(end_node):
        raise Exception("End node is not present in the graph")

    # Find the shortest route in the network between the two users
    nodes = deque([start_node])
    previous_node = {start_node: None}
    
    while nodes:
        current_node = nodes.popleft()
        
        for neighbor_node in graph[current_node]:
            
            # don't visit if the node has already been visited
            if previous_node.get(neighbor_node):
                continue
            
            previous_node[neighbor_node] = current_node
            nodes.append(neighbor_node)
            
            if neighbor_node == end_node:
                return get_traversal_path(start_node, end_node, previous_node)
    
    return None


















# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)