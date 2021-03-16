# Inorder Successor in BST
# https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1#
# @author Akash Kumar

#User function Template for python3

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''
# returns the inorder successor of the Node x in BST (rooted at 'root')
def inorderSuccessor(root, x):
    """
    Function to find the inorder successor of a node `x` in a tree `root`.
    
    Approach:
    - if x is greater than or equal to the current node, search in its right subtree
    - if x is less than the current node
        - save the current node, because if the right subtree of x is NULL, then the 
          current node would be the inorder successor, and
        - search the left subtree

    :param root: The root of the tree
    :param x: The node whose inorder successor is to be found
    """
    
    parent_that_is_possibly_the_successor = None
    subtree_root = root
    
    while subtree_root:
        if x.data >= subtree_root.data:
            subtree_root = subtree_root.right
        
        else:
            parent_that_is_possibly_the_successor = subtree_root
            subtree_root = subtree_root.left
            
    return parent_that_is_possibly_the_successor

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k = int(input())
        ptr = inorderSuccessor(root, Node(k))
        if ptr is None:
            print(-1)
        else:
            print(ptr.data)
# } Driver Code Ends

"""
Sample test cases
3
2 1 3
3
20 8 22 4 12 N N N N 10 14
8
15 10 16 1 14 N 81 N 8 12 N 63 14
14

Output
-1
10
15
"""