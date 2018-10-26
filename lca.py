
# Binary tree node.
class Node:

    # Constructor for new binary tree Node.
    def __init__(self,key,children):
        self.key = key
        self.children= []

def addChild(node,child):
    node.children.append(child)

def findPath(root,x,path):
    path.append(root)
    if x.key==root.key:
        return

    for i in root.children:
        findPath(i,x,path)

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
            if i.key==j.key:
                lca = i
    return i.key
