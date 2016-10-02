# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.


# Name: Brennon Lee
# On my honor as a University of Colorado Student, this code was entirely written by myself with no unauthorized help.

class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):
        if (self.key == None):
            self = key_to_insert
        else:
            if(key_to_insert < self.key):
                #insert on left
                if (self.left == None):
                    self.left = Node(key_to_insert)
                else:
                    return (self.left.insert(key_to_insert))
            elif(key_to_insert > self.key):
                #insert on right
                if (self.right == None):
                    self.right = Node(key_to_insert)
                else:
                    return (self.right.insert(key_to_insert))
            else:
                return

    def inorder_traversal(self, ret_list):
        print("self is: ", self.key)
        if (self == None):
            print("is none falling in here?")
            return

        if (self.left != None):
            self.left.inorder_traversal(ret_list)

        ret_list.append(self.key)

        if (self.right != None):
            self.right.inorder_traversal(ret_list)

        return ret_list

    def get_depth(self):
        depth = 0
        left = 0
        right = 0
        if (self != None):
            if (self.left != None):
                left = self.left.get_depth()
            if(self.right != None):
                right = self.right.get_depth()
            depth = 1 + max(left, right)
            return depth
        else:
            return depth

    def key_exists(self, key_to_find):
        if (key_to_find == self.key):
            return True
        else:
            if (key_to_find < self.key and self.left):
                #search left
                return (self.left.key_exists(key_to_find))
            elif (key_to_find > self.key and self.right):
                #search right
                return (self.right.key_exists(key_to_find))
            else:
                return False

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')
