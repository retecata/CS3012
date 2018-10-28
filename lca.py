
# Binary tree node.
class Node:

    # Constructor for new binary tree Node.
    def __init__(self,key):
        self.key = key
        self.children = []
        self.parents = []

def addChild(node,child):
    node.children.append(child)

def addParent(node,parent):
    node.parents.append(parent)

# findPath computes the path from the root to a node.
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

# findAncestors computers all the ancestors of a given node.
def findAncestors(root,node,ancestors):
    ancestors.append(node.key)
    if(node.key==root.key):
        return

    for i in node.parents:
        findAncestors(root,i,ancestors)

# findLCADAG is the approach that works for both non-binary trees and DAGs.
def findLCADAG(root,node1,node2):
    if root is None:
        return False

    ancestors = []
    ancestors2 = []
    findAncestors(root,node1,ancestors)
    findAncestors(root,node2,ancestors2)
    for i in ancestors:
        for j in ancestors2:
            if i== j:
                return i

# findLCA is the approach that works for non-binary trees, but it doesn't work for any graph where a node has more than one parent.
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
            #print("%d %d:",i.key,j.key)
            if i.key==j.key:
                lca = i.key
    return lca
