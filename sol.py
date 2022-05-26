# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        next_level = [root]

        i = 0

        Flag = True

        while Flag:

            i = i + 1

            level_content = []

            next_next_level = []

            for node in next_level:

                if (node == None):
                    continue

                level_content.append(node.val)

                next_next_level.append(node.left)
                next_next_level.append(node.right)

            next_level = next_next_level

            if len(level_content) == 0:
                break

            if (i % 2 == 0):
                level_content = level_content[::-1]

            res.append(level_content)

        return res
