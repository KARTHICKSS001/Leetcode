class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traveral(curr):
            if not curr:
                return
            traveral(curr.left)
            ans.append(curr.val)
            traveral(curr.right)

        traveral(root)
        return ans      
