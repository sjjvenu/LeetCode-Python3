# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return sys.maxsize
        minLeft = sys.maxsize
        minRight = sys.maxsize
        
        if root.left != None:
            minLeft = min(self.minDiffInBST(root.left),root.val-root.left.val)
            rLeft = root.left.right
            while rLeft != None:
                minLeft = min(minLeft,root.val-rLeft.val)
                rLeft = rLeft.right
        if root.right != None:
            minRight = min(self.minDiffInBST(root.right),root.right.val-root.val)
            lRight = root.right.left
            while lRight != None:
                minRight = min(minRight,lRight.val-root.val)
                lRight = lRight.left
        
        return min(minLeft,minRight)
            




class Solution2:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        arr = []
        
        def traverse(node):
            arr.append(node.val)
            
            if node.left:
                traverse(node.left)
                
            if node.right:
                traverse(node.right)
        
        traverse(root)
        arr.sort()
        
        dist = float('inf')
        
        for i in range(len(arr)-1):
            dist = min(dist, abs(arr[i] - arr[i+1]))
            
        return dist

