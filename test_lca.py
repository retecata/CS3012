import pytest
import sys
from lca import Node
from lca import findPath

def test_findPathForRoot():
    node = Node(1)
    path = []
    assert findPath(node,path,node) == True
