'''
class node:
    def __init__(self,data):
        self.data = None
        self.left = None
        self.right = None
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

def height(root):
        if root is None:
             return 0 
        l = height(root.left)
        r = height(root.right)
        return 1+max(l,r)

def diameter(root):
    if root if None:
        return 0
    l = height(root.left)
    r = height(root.right)
    d = l+r+2
    d_l = diameter(root.left)
    d_r = diameter(root.right)
    return max(d,d_l,d_r)

print(diameter(root))
'''