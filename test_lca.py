import pytest
import sys
from lca import Node
from lca import findPath
from lca import addChild
from lca import addParent
from lca import findLCA
from lca import findLCADAG

def test_findPathForRoot():
    node = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    addChild(node,node1)
    addChild(node,node2)
    addChild(node2,node3)

    path = []
    # When a path exists.
    assert findPath(node,node3,path) == True

    # When there's no path.
    path = []
    assert findPath(node,node4,path) == False

def test_findPathForRandomNode():
    node = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    addChild(node,node1)
    addChild(node,node2)
    addChild(node2,node3)

    path = []
    # When a path exists.
    assert findPath(node2,node3,path) == True

    # When there's no path.
    path = []
    assert findPath(node1,node4,path) == False

def test_findLCA():
    node = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    addChild(node,node1)
    addChild(node,node2)
    addChild(node2,node3)
    addChild(node2,node4)

    assert findLCA(node,node4,node3) == 3

def test_findLCANonBinaryTree():
    node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    addChild(node,node1)
    addChild(node,node2)
    addChild(node2,node3)
    addChild(node2,node4)
    addChild(node2,node5)
    addChild(node4,node6)

    assert findLCA(node,node1,node6) == 0
    assert findLCA(node,node3,node6) == 2
    assert findLCA(node,node,node6) == 0

def test_findLCALoop():
    node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    addChild(node,node1)
    addChild(node1,node5)
    addChild(node1,node2)
    addChild(node2,node3)
    addChild(node3,node4)
    addChild(node5,node6)
    addChild(node6,node4)

    assert findLCA(node,node1,node5) == 1
    assert findLCA(node,node3,node6) == 1
    assert findLCA(node,node4,node6) == 6
    #assert findLCA(node,node3,node4) == 3 - this implementation does not work for dag

def test_findLCAParents():
    node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    addParent(node6, node5)
    addParent(node5, node1)
    addParent(node4, node6)
    addParent(node4, node3)
    addParent(node3, node2)
    addParent(node2, node1)
    addParent(node1, node)

    assert findLCADAG(node,node1,node5) == 1
    assert findLCADAG(node,node3,node6) == 1
    assert findLCADAG(node,node4,node6) == 6
    assert findLCADAG(node,node3,node4) == 3
