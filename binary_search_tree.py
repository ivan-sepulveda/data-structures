
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self, starting_value=None):
        if starting_value:
            self.root = Node(starting_value)
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

    def _iterative_insert(self, value):
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

    def list_nodes(self, root, traversal=1):
        """ Args:
            listed_nodes: idk
            nodes: Meant
            root: current node
            traversal (int): The requested order, In-order by default.
                traversal =  1  --> In-order
                traversal =  0  --> Pre-order
                traversal = -1  --> Post-order"""

        listed_nodes = []
        current_node = root

        if current_node is not None:
            if traversal:

                listed_nodes += self.list_nodes(current_node.left)

                if current_node.value is not None:
                    listed_nodes += [current_node.value]

                listed_nodes += self.list_nodes(current_node.right)

        return listed_nodes

    def balance(self):
        print("Balancing BST")

        if self.root is not None:
            ordered_nodes = self.list_nodes(self.root, traversal=1)
            print("\n\tOrdered nodes:\n\t{}".format(ordered_nodes))

            median_index = self.size // 2
            median_value = ordered_nodes[median_index]

            print("median_index = {}".format(median_index))
            print("median_value = {}".format(median_value))

            balanced_bst = BinarySearchTree(median_value)

            ordered_nodes.remove(median_value)

            for value in ordered_nodes:
                print("Inserting into balance: {}".format(value))
                balanced_bst.insert(value)


integers_to_add = [50, 25, 3, 42, 60, 75, 120]

recursive_bst = BinarySearchTree()
iterative_bst = BinarySearchTree()

bst = recursive_bst

for val in integers_to_add:
    recursive_bst.insert(val)
    iterative_bst.insert(val, recursive=False)


bst.balance()




