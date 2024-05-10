"""
Implement an algorithm for inserting a number into a BST tree, and then write a program which,
for a given number k, checks whether k occurs in such a tree.
"""
from utilities.generator import Generator


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left_side: [None | TreeNode] = None
        self.right_side: [None | TreeNode] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self._root_node: [None | TreeNode] = None

    def insert(self, value: int) -> None:
        if not self._root_node:
            self._root_node = TreeNode(value)  # if the tree is empty, insert the new value
        else:
            self._insert_recursively(self._root_node, value)

    def _insert_recursively(self, root_node: TreeNode, value: int) -> None:
        if value < root_node.value:  # insert on the left side of the root
            if not root_node.left_side:
                root_node.left_side = TreeNode(value)
            else:
                self._insert_recursively(root_node.left_side, value)
        else:  # insert on the right side of the root
            if not root_node.right_side:
                root_node.right_side = TreeNode(value)
            else:
                self._insert_recursively(root_node.right_side, value)

    def search(self, search_number: int) -> bool:
        return self._search_recursively(self._root_node, search_number) if self._root_node else False

    def _search_recursively(self, root_node: [TreeNode | None], search_number: int) -> bool:
        if not root_node:  # empty binary tree
            return False
        if root_node.value == search_number:
            return True
        elif search_number < root_node.value:  # search on the left side of the root
            return self._search_recursively(root_node.left_side, search_number)
        else:  # search on the right side of the root
            return self._search_recursively(root_node.right_side, search_number)


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    input_search_number: int = Generator.generate_random_search_number()
    input_numbers: list = Generator.generate_input_array()

    for number in input_numbers:
        binary_search_tree.insert(number)

    print(60 * "-")
    print(f"Generated random input search number: {input_search_number}")
    print(f"Generated random input numbers: {input_numbers}")
    print(60 * "-")

    if binary_search_tree.search(input_search_number):
        print(f"The number: {input_search_number} exists in the Binary Search Tree.")
    else:
        print(f"The number: {input_search_number} does not exist in the Binary Search Tree.")
    print(60 * "-")
