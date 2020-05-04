def pprint_tree(node, _prefix="", _last=True):
    print(_prefix, "`- " if _last else "|- ", node.value, sep="")
    _prefix += "   " if _last else "|  "
    child_count = 0
    kids = []
    for node in [node.left, node.right]:
        if node is not None:
            child_count += 1
            kids.append(node)
    for i, child in enumerate(kids):
        _last = i == (child_count - 1)
        if child is not None:
            pprint_tree(child, _prefix, _last)


class Node:
    """Node: The components of a Binary Search Tree, sometimes referred to as leaves.

    Args:
        value (int): An integer value to assign to this Node instance.

    Attributes:
        left (int): Number of valid nodes in our BST (valid meaning Nodes's value is equal to an integer, not 'None').
        right (Node): The first/top Node in our BST.
        value (Node): The first/top Node in our BST.

    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.children = [self.left, self.right]


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
                root.left = Node(value)
                self.size += 1
            else:
                self._recursive_insert(root=root.left, value=value)
        else:
            if not root.right:
                root.right = Node(value)
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
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right


    def list_nodes(self, traversal=1):
        """ Args:
            root: current node
            traversal (int): The requested order, In-order by default.
                traversal =  1  --> In-order
                traversal =  0  --> Pre-order
                traversal = -1  --> Post-order"""

        if not self.root:
            return []
        else:
            return self._list_nodes(self.root, traversal=traversal)

    def _list_nodes(self, root, traversal):
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

        if root is None:
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


recursive_bst = BinarySearchTree()
iterative_bst = BinarySearchTree()

unordered_integers = [50, 25, 3, 42, 60, 120, 75]
ascending_integers = sorted(unordered_integers.copy())
descending_integers = ascending_integers.copy()[::-1]

print("\n\n")

print("=================================================================")
print("recursive_bst: {}".format(recursive_bst.list_nodes()))
print("bst.find(50)\n\tExpected: {}\n\tActual: {}".format(False, recursive_bst.find(50)))
print("Inserting unordered_integers into recursive_bst")

for val in ascending_integers:
    recursive_bst.insert(val)

print("recursive_bst: {}".format(recursive_bst.list_nodes(recursive_bst.root)))
print("bst.find(50)\n\tExpected: {}\n\tActual: {}".format(True, recursive_bst.find(50)))

print("\n")

print("iterative_bst: {}".format(iterative_bst.list_nodes()))
print("bst.find(50)\n\tExpected: {}\n\tActual: {}".format(False, iterative_bst.find(50)))

print("Inserting unordered_integers into iterative_bst")

for val in ascending_integers:
    iterative_bst.insert(val)

print("iterative_bst: {}".format(iterative_bst.list_nodes(iterative_bst.root)))

print("bst.find(50)\n\tExpected: {}\n\tActual: {}".format(True, iterative_bst.find(50)))
print("=================================================================")
print("\n")


"""
print("\n\n\n")


print("=================================================================")
print("Recursive BST (Before Balancing):")
pprint_tree(recursive_bst.root)
print("\t\nHeight: {}".format(recursive_bst.height()))
print("\n")
print("Recursive BST (After Balancing):")
recursive_bst = recursive_bst.get_balanced()
pprint_tree(recursive_bst.root)
print("\t\nHeight: {}".format(recursive_bst.height()))
print("=================================================================")

print("\n\n\n")

print("=================================================================")
print("Iterative BST (Before Balancing):")
pprint_tree(iterative_bst.root)
print("\t\nHeight: {}".format(iterative_bst.height()))
print("\n")
print("Iterative BST (After Balancing):")
iterative_bst = iterative_bst.get_balanced()
pprint_tree(iterative_bst.root)
print("\t\nHeight: {}".format(iterative_bst.height()))
print("=================================================================")
print("\n")

"""




