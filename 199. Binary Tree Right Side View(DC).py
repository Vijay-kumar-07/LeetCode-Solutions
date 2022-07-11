# Question:

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]
        
        def dfs(node =root,level=1):
            if not node: return
            
            if len(ans) < level: 
                ans.append(node.val)
            dfs(node.right,level+1)         #  <--- right first
            dfs(node.left ,level+1)         #  <--- then left

            return 

        dfs()
        return ans

