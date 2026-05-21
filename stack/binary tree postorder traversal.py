class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traversal(curr):
            if not curr:
                return
            traversal(curr.left)
            traversal(curr.right)
            ans.append(curr.val)
        
        traversal(root)
        return ans
      
