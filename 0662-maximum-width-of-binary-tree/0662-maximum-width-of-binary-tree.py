# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque([(root,0)])
        mx_width=0
        while queue:
            lv_size=len(queue)
            lv_start=queue[0][1]
            lv_end=queue[-1][1]
            mx_width=max(mx_width,lv_end-lv_start+1)
            for i in range(lv_size):
                node,pos=queue.popleft()
                if node.left:
                    queue.append((node.left,pos*2))
                if node.right:
                    queue.append((node.right,pos*2+1))
        return mx_width