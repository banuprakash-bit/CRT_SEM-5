class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

def lca(root, p, q):
    if root is None:
        return None
    if root.data == p or root.data == q:
        return root.data
    l = lca(root.left,p,q)
    r = lca(root.right,p,q)
    if l and r:
        return root.data
    return l if l else r
print(lca(root,4,5))