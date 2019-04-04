class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.result = 0
        self.distributing(root)
        return self.result

    def distributing(self, node):
        if node == None:
            return 0
        left = self.distributing(node.left)
        self.result += abs(left)
        node.val += left

        right = self.distributing(node.right)
        self.result += abs(right)
        node.val += right
        return node.val - 1
