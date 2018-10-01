
#Binary tree node
class Node:

    #Constructor for new binary tree Node
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# findPath looks for the path from the root node to the given node.
# It stores the path into an array. If the path doesn't exist, it returns
# false, otherwise true.
def findPath(root,path,node):
    if root is None:
        return False

    #store the node in the path array.
    path.append(root.key)

    #Check whether the Node is the root itself.
    if root.key == node.key:
        return True

    #Check the right and left sub-trees.
    if((root.left!=None and findPath(root.left,path,node)) or (root.right!=None
        and findPath(root.right,path,node))):
        return True

    #remove root from tree if not present in subtree
    path.pop()
    return False
