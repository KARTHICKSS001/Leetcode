class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traversal(curr):
            if not curr:
                return
            ans.append(curr.val)
            traversal(curr.left)
            traversal(curr.right)
        traversal(root)
        return ans
