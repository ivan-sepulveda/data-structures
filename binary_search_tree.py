import random

class Node:
    """Node: The components of a Binary Search Tree, sometimes referred to as leaves.

    Args:
        value (int): An integer value to assign to this Node instance.

    Attributes:
        left (int): Number of valid nodes in our BST (valid meaning Nodes's value is equal to an integer, not 'None').
        right (Node): The first/top Node in our BST.
        value (Node): The first/top Node in our BST.

    """
    def __init__(self, value, parent=None):
        self.left, self.right, self.parent = None, None, parent
        self.value = value


class BinarySearchTree:
    """Binary Search Tree.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        starting_value (int): Human readable string describing the exception.

    Attributes:
        size (int): Number of valid nodes in our BST (valid meaning Nodes's value is equal to an integer, not 'None').
        root (Node): The first/top Node in our BST.

    """
    def __init__(self, starting_value=None):
        if isinstance(starting_value, int):
            self.root = Node(starting_value)
            self.size = 1
        elif isinstance(starting_value, Node):  # TODO: Error Handling for starting_value.value < 0
            self.root = starting_value.value
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def length(self):
        return self.size

    def min(self, recursive=True, return_value=False):
        if not self.root:
            return None
        elif recursive:
            return self._min(self.root, True, return_value=return_value)
        elif not recursive:
            return self._min(self.root, False, return_value=return_value)

    def _min(self, root, recursive=True, return_value=False):
        if not root:
            return None
        elif recursive:
            if root.left:
                return self._min(root.left, return_value=return_value)
            else:
                return root

    def pprint_tree(self, _prefix="", _last=True):
        if not self.root:
            return
        self._pprint_tree(self.root, _prefix, _last)

    def _pprint_tree(self, node, _prefix="", _last=True):
        if not self.root:
            return
        try:
            print(_prefix, "`- " if _last else "|- ", node.value, sep="")
        except AttributeError:
            print("This node is bad: {}".format(node))
        _prefix += "   " if _last else "|  "
        child_count = 0
        kids = []
        for node in [node.right, node.left]:
            if node is not None:
                child_count += 1
                kids.append(node)
        for i, child in enumerate(kids):
            _last = i == (child_count - 1)
            if child is not None:
                self._pprint_tree(child, _prefix, _last)

    def print_tree(self, traversal=1):
        """Allows user to print this tree in any of the following orders.
            In-order (Left, Root, Right)
            Pre-order (Root, Left, Right)
            Post-order (Left, Right, Root)

        Args:
            traversal (int): The requested print order, In-order by default.
                traversal =  1  --> In-order
                traversal =  0  --> Pre-order
                traversal = -1  --> Post-order
        """
        if self.root is not None:
            if traversal:
                self._print_tree_in_order(self.root)
            elif not traversal:
                self._print_tree_pre_order(self.root)
            else:
                self._print_tree_post_order(self.root)

    def _print_tree_in_order(self, current_node):  # Private Method
        if current_node is not None:
            self._print_tree_in_order(current_node.left)
            print(current_node.value)
            self._print_tree_in_order(current_node.right)

    def _print_tree_pre_order(self, current_node):  # Private Method
        if current_node is not None:
            print(current_node.value)
            self._print_tree_pre_order(current_node.left)
            self._print_tree_pre_order(current_node.right)

    def _print_tree_post_order(self, current_node):  # Private Method
        if current_node is not None:
            self._print_tree_post_order(current_node.left)
            self._print_tree_post_order(current_node.right)
            print(current_node.value)

    def insert(self, value, recursive=True):
        """print("Insert function has been called:"
              "\n\t value = {0}"
              "\n\t method = {1}"
              .format(value, "recursion" if recursive else "iterative"))"""
        if not self.root:
            self.root = Node(value)
        else:
            if recursive:
                self._recursive_insert(self.root, value)
            else:  # Iterative
                self._iterative_insert(value)

    def _recursive_insert(self, root, value):
        if value < root.value:
            if not root.left:
                root.left = Node(value, parent=root)
                self.size += 1
            else:
                self._recursive_insert(root=root.left, value=value)
        else:
            if not root.right:
                root.right = Node(value, parent=root)
                self.size += 1
            else:
                self._recursive_insert(root=root.right, value=value)

    def _iterative_insert(self, value):  # Private
        """

        Args:
            value (int): Value to insert

        """
        if isinstance(value, Node):
            value = value.value

        current = self.root

        while current:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    current.right.parent = current
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    current.right.parent = current
                    break
                else:
                    current = current.right

    def get_level(self, level_requested):
        """ Args:
            level_requested (int): The requested level (nodes at this height)"""

        if not self.root:
            return []
        else:
            return self._get_level(self.root, level_requested, current_level=1)

    def _get_level(self, root, level_requested, current_level=0):
        """ Args:
            traversal (int): The requested order, In-order by default.
                traversal =  1  --> In-order
                traversal =  0  --> Pre-order
                traversal = -1  --> Post-order"""

        if not self.root:
            return []
        elif not root:
            return []
        elif current_level == level_requested:
            return [root.value]
        elif current_level < level_requested:
            left_results = self._get_level(root.left, level_requested=level_requested, current_level=current_level+1)
            right_results = self._get_level(root.right, level_requested=level_requested, current_level=current_level+1)
            return left_results + right_results

    def list_nodes(self, traversal=1):
        """ Args:
            traversal (int): The requested order, In-order by default.
                traversal =  1  --> In-order
                traversal =  0  --> Pre-order
                traversal = -1  --> Post-order"""

        if not self.root:
            return []
        else:
            return self._list_nodes(self.root, traversal=traversal)

    def _list_nodes(self, root, traversal=1):
        listed_nodes, current_node = [], root

        if current_node is not None:
            if traversal:
                listed_nodes += self._list_nodes(root=current_node.left, traversal=traversal)
                if current_node.value is not None:
                    listed_nodes += [current_node.value]

                listed_nodes += self._list_nodes(root=current_node.right, traversal=traversal)

        return listed_nodes

    def _insert_array(self, array):
        if array:
            try:
                sorted_array = sorted([value for value in set(array)]).copy()

                median_index = len(sorted_array) // 2
                median_value = sorted_array[len(sorted_array) // 2]

                left_of_median = sorted_array[:median_index]
                right_of_median = sorted_array[median_index + 1:]

                self.insert(median_value)
                self._insert_array(left_of_median)
                self._insert_array(right_of_median)
            except IndexError:
                pass

    def get_balanced(self):
        """
        Returns:
            balanced_bst: A minimum height (balanced) BST with same Nodes as the instance this method is called on.
        """
        if self.root is not None:
            balanced_bst = BinarySearchTree()
            balanced_bst._insert_array(self.list_nodes(self.root))

            return balanced_bst

    def height(self):
        if self.root is None:
            return 0
        return self._height(self.root)

    def _height(self, root):

        if not root:
            return 0

        height_of_left_subtree, height_of_right_subtree = 0, 0

        if root.left:
            height_of_left_subtree += self._height(root.left)
        if root.right:
            height_of_right_subtree += self._height(root.right)

        return 1 + max(height_of_left_subtree, height_of_right_subtree)

    def find(self, value_searched):
        if not self.root:
            return False
        else:
            return self._find(self.root, value_searched)

    def _find(self, root, value_searched):
        if not root:
            return False
        elif value_searched == root.value:
            return True
        elif value_searched < root.value:
            return self._find(root.left, value_searched)
        else:
            return self._find(root.right, value_searched)

    def find_successor(self):
        if not self.root:
            return None
        else:
            return self._find_successor(self.root)

    def _find_successor(self, root):
        if not root:
            return None
        elif root.right:
            r = self._min(root.right, recursive=True, return_value=False)
            print("_find_successor: returning ", r)
            return r

    def remove(self, value_to_remove):
        if not self.root:
            return False
        elif not self.find(value_to_remove):
            return False
        else:
            return self._remove(self.root, value_to_remove)

    def _remove(self, root, value_to_remove):
        if not root:
            return False

        elif value_to_remove == root.value:
            # Case 1: Root has no children. Just set node to None
            if root.left is None and root.right is None:
                if root.value == self.root.value:
                    self.root = None
                else:  # Need the else condition because we don't want to call on parents that don't exist.
                    if root.value < root.parent.value:
                        root.parent.left = None
                    else:
                        root.parent.right = None
                return True

            elif (root.left and not root.right) or (root.right and not root.left):
                # Case 2a: Root has only one subtree
                child = root.left if root.left is not None else root.right
                if root == self.root:
                    self.root = child
                else:
                    child.parent = root.parent
                    if child.value > root.parent.value:
                        root.parent.right = child
                    else:
                        root.parent.left = child


            elif root.left and root.right:  # Case 3: Root hss two children
                if not root.right.left:  # Case 3a: Right Subtree has no left branch
                    root.value = root.right.value
                    root.right = root.right.right
                    self._remove(root.right, value_to_remove)
                else:  # Case 3b: Need to find successor (smallest element in right subtree), swap, and delete
                    successor = self._find_successor(root)
                    root.value = successor.value

                    if successor.value < successor.parent.value:
                        successor.parent.left = None
                    else:
                        successor.parent.right = None
                    successor.parent = None

        elif value_to_remove < root.value:
            return self._remove(root.left, value_to_remove)
        else:
            return self._remove(root.right, value_to_remove)


recursive_bst = BinarySearchTree()
iterative_bst = BinarySearchTree()

add_in_this_order = [50, 30, 70, 10, 5, 7, 40, 39, 38, 45, 80, 90, 75]
remove_in_this_order = [7, 10, 70, 30, 38, 50, 75, 80, 90, 5, 39, 45, 40]




for i in range(1):  # range(2):
    tree, tree_type = (recursive_bst, "recursive_bst") if i == 0 else (iterative_bst, "iterative")
    print("\n=================================================================")
    print("{0}: {1}".format(tree_type, tree.list_nodes()))
    print("=================================================================")

    print("\nEmpty Tree\n")
    tree.pprint_tree(tree.root)

    for elem in add_in_this_order:
        tree.insert(elem)

    print("\nFull Tree\n")
    tree.pprint_tree()

    last_removed = -1
    for elem in remove_in_this_order[:13]:
        last_removed = elem

        print("\nBefore removing {}\n".format(last_removed))
        tree.pprint_tree()

        tree.remove(elem)

        print("\nAfter removing {}\n".format(last_removed))
        tree.pprint_tree()







