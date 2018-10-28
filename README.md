# CS3012

## Lowest Common Ancestor Part 1
The first part of this module consists of providing a solution to the Lowest Common Ancestor problem, assuming the Graph is structured as a "binary tree".
I wrote the solution in Python. As it is my first attempt using Python, the approach taken is inspired from the [geeksforgeeks implementation](https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/). However, the
corresponding unit tests consist of code written fully by myself.

## Lowest Common Ancestor Part 2
For the second part of the project, we were asked to create a new branch, in my case "DAG-implementation" and to change the code so that it works for directed acyclic graphs as well. For this I tried two approaches.

First I aimed to change the initial code as little as possible and to still compute the path from root to each node and then check for the lowest common ancestor. In this case the nodes would have a  list of children as opposed to right/left node. This work for any type of Tree. However it does not work for any type of directed acyclic graph, especially when there's a node with two parents.

Second approach was instead of storing the children of each node, to store the parents and then compute a list of all ancestors of each node. Afterwards the lowest common ancestor would be the closest to the node. This approach proved successful and passed all the test cases the previous approach didn't.
