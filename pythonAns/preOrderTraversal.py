class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]

        while len(stack) > 0:
            curNode = stack.pop()
            if curNode != None:
                stack.append(curNode.right)
                stack.append(curNode.left)
                result.append(curNode.val)
        return result
