
# Binary tree node.
class Node:

    # Constructor for new binary tree Node.
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

    # Store the node in the path array.
    path.append(root.key)

    # Check whether the Node is the root itself.
    if root.key == node.key:
        return True

    # Check the right and left sub-trees.
    if ((root.left != None and findPath(root.left, path, node)) or
            (root.right!= None and findPath(root.right, path,node))):
        return True

    # Remove root from tree if not present in subtree.
    path.pop()
    return False

# findLCA finds the lowest common ancestor of two nodes in a given binary tree.
def findLCA(root,node1,node2):

    # two lists for storing the paths
    path1 = []
    path2 = []

    # Find the paths, if one of the paths returns false, return -1.
    if (not findPath(root, path1, node1) or not findPath(root, path2, node2)):
        return -1

    # Compare the paths to get the first different value.
    i = 0
    while (i<len(path1) and i<len(path2)):
        if path1[i] != path2[i]:
            break
        i +=1
    return path1[i-1]
