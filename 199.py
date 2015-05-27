class Solution:
    def rightSideView(self, root):
        view = []
        while True:
            view.append( root.val)
            if root.right :
                root = root.right
            elif root.left :
                root = root.left
            if root.left == None and root.right == None :
                break
        return view


