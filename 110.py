class TreeNode:
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def treeDepth (self, root):
        if root == None :
            return -1
        ldepth = self.treeDepth (root.left)
        rdepth = self.treeDepth (root.right)
        if ldepth > rdepth :
            return ldepth + 1
        else :
            return rdepth + 1

    def isBalanced (self, root):
        if root == None :
            return True
        ldepth = self.treeDepth(root.left)
        rdepth = self.treeDepth(root.right)
        if ldepth - rdepth > 1 or rdepth - ldepth > 1 :
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

s = Solution ()

root = TreeNode (1)
root.right= TreeNode (2)
root.left = TreeNode (2)
root.left.left = TreeNode (3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode (4)
root.right.right.right = TreeNode (4)

print s.treeDepth(root)
print s.isBalanced(root)


