"""
https://leetcode.com/problems/invert-binary-tree/

11/5/2022

--- PROMPT ---
Given the root of a binary tree, invert the tree, and return its root.

** will require recursion to complete


--- LESSONS ---
Explanation
https://favtutor.com/blogs/invert-binary-tree



"""


# --- MY SOLUTION ---
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if (root == None): 
            return
        else: 
    
            # temp = root  
            # swap the pointers in this node. Temp used to allow the swap to occur
            temp = root.left  
            root.left = root.right  
            root.right = temp  

            # recursive calls
            self.invertTree(root.left)  
            self.invertTree(root.right)  

            return root

# --- PSUEDOCODE ---
"""
Primary logic:
- need to be able to switch the left and the right pointers
- need to return the root of the adjusted element
  thinking of something like hint = root = TreeNode





"""
# --- TEST ---

# print InOrder binary tree traversal.
def print_tree(node) : 
  
    if (node == None):  
        return
          
    print_tree(node.left)  
    print node.val,
    print_tree(node.right)  


root = TreeNode(2)  
root.left = TreeNode(1)  
root.right = TreeNode(4)  
root.right.left = TreeNode(3)  
root.right.right = TreeNode(5)  
# Print inorder traversal of the input tree
print("Inorder traversal of the constructed tree is")  
print_tree(root)  


# --- ALT SOLN by others ---
