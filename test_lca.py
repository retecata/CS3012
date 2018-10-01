import pytest
import sys
from lca import Node
from lca import findPath

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
