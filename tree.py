"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""
from node import Node


class Tree:
    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    - swap(subtree_a, subtree_b): Swap the position of the subtrees.
    """

    def __init__(self, root):
        """
        Initialises the tree with a root node.
        :param root: the root node.
        """
        self.root = root

    def put(self, node, child):
        node.add_child(child)

    """
        Inserts a node into the tree. Adds `child` to `node`.
        :param node: The node currently in the tree.
        :param child: The child to add to the tree.
        """

    # TODO implement me.

    def flatten(self, node):
        cursor = node.parent
        node.key = self.helper(node)
        node.children = []

        while cursor is not None:
            for item in cursor.children:
                if item.subtree_value > cursor.subtree_value:
                    cursor.subtree_value = item.subtree_value
            cursor = cursor.parent

        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes.

        :param node: The root of the subtree to flatten.



        Example

           A(5)
           / \
         B(3) C(6)
         /    |  \
        D(2) E(3) F(6)

        flatten(C)

           A(5)
           / \
         B(3) C(15)
         /
        D(2)

        """
        # TODO implement me.

    def swap(self, subtree_a, subtree_b):

        if subtree_a in subtree_b.children or subtree_b in subtree_a.children:
            return

        temp1 = subtree_a.parent
        temp2 = subtree_b.parent

        subtree_a.parent.children.remove(subtree_a)
        subtree_b.parent.children.remove(subtree_b)

        subtree_a.parent = temp2
        subtree_b.parent = temp1

        self.revert(subtree_a)
        self.revert(subtree_b)

        subtree_a.parent.add_child(subtree_a)
        subtree_b.parent.add_child(subtree_b)
        self.bubble(subtree_a)
        self.bubble(subtree_b)

        """
        Swap subtree A with subtree B
        :param subtree_a: The root node of subtree_a.
        :param subtree_b: The root node of subtree_b.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """

    # TODO implement me.

    def helper(self, Node):
        for item in Node.children:
            self.helper(item)
            Node.key += item.key
            Node.subtree_value = Node.key

        return (Node.key)

    def revert(self, node):
        cursor = node.parent
        while cursor is not None:
            for child in cursor.children:
                cursor.subtree_value = cursor.key
            cursor = cursor.parent

    def bubble(self, node):
        cursor = node.parent
        while cursor is not None:
            for child in cursor.children:
                if cursor.subtree_value < child.subtree_value:
                    cursor.subtree_value = child.subtree_value
            cursor = cursor.parent


def main():
    print("m")


if __name__ == '__main__':
    main()









