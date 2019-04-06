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

class Solution2:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def dfs(node):
            if node == None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
