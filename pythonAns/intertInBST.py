class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        self.insertNode(root, val)
        return root

    def insertNode(self, node, value):
        if node.val > value:
            if node.left == None:
                node.left = TreeNode(value)
                return
            else:
                return self.insertNode(node.left, value)
        else:
            if (node.right == None):
                node.right = TreeNode(value)
                return
            else:
                return self.insertNode(node.right, value)
