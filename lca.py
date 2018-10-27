
# Binary tree node.
class Node:

    # Constructor for new binary tree Node.
    def __init__(self,key):
        self.key = key
        self.children = []

def addChild(node,child):
    node.children.append(child)

def findPath(root,x,path):
    path.append(root)
    if x.key==root.key:
        return True

    for i in root.children:
        if findPath(i,x,path):
            return True

    # Remove root from tree if not present in subtree.
    path.pop()
    return False        


def findLCA(root,node1,node2):
    if root is None:
        return False
    path1 = []
    path2 = []
    findPath(root,node1,path1)
    findPath(root,node2,path2)
    lca =0;
    for i in path1:
        for j in path2:
            print("%d %d:",i.key,j.key)
            if i.key==j.key:
                lca = i.key
    return lca
