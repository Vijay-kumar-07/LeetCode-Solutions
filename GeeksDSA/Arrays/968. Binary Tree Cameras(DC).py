# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

# Return the minimum number of cameras needed to monitor all nodes of the tree.

# Input: root = [0,0,null,0,0]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if not node:
                return (0, math.inf)
            l_count, l_state = postorder(node.left)
            r_count, r_state = postorder(node.right)
    
            state = min(l_state, r_state)
            total_cameras = l_count + r_count
    
            if state == 0:
                return (total_cameras + 1, 1)
    
            if state == 1:
                return (total_cameras, 2)
            return (total_cameras, 0)
        dummy = TreeNode(-1, root)
        return postorder(dummy)[0]