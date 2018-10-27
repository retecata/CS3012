import pytest
import sys
from lca import Node
from lca import findPath
from lca import addChild
from lca import findLCA

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

    path = []
    # When a path exists.
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

    path = []
    # When a path exists.
    assert findLCA(node,node1,node6) == 0
    assert findLCA(node,node3,node6) == 2
    assert findLCA(node,node,node6) == 0
