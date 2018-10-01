import pytest
import sys
from lca import Node
from lca import findPath
from lca import findLCA

def test_findPathForRoot():
    node = Node(1)
    path = []
    assert findPath(node,path,node) == True

def test_findPathRandomNode():
    root = Node(1)
    node = Node(2)
    node2 = Node(3)
    root.left = node
    node.left = node2
    path = []
    assert findPath(root,path,node2) == True
    assert path == [1,2,3]

def test_findPathFalse():
    root = Node(1)
    node = Node(2)
    path = []
    assert findPath(root,path,node) == False
    assert path == []

def test_findLCA():
    root = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    root.left = node1
    root.right = node2
    assert findLCA(root,node1,node2) == root.key

def test_findLCANone():
    root = Node(1)
    node1 = Node(2)
    node2 = Node(3)
    root.left = node1
    assert findLCA(root,node1,node2) == -1

def test_findLCANotRoot():
    root = Node(1)
    lca = Node(2)
    node1 = Node(3)
    node2 = Node(2)
    root.left = lca
    lca.left = node1
    lca.right = node2
    assert findLCA(root,node1,node2) == lca.key
