# username1 - almoghaviv
# id1      - 207298720
# name1    - Almog Haviv
# username2 - tal9
# id2      - 322539651
# name2    - Tal Cohen


"""A class representing a node in an AVL tree"""


class AVLNode(object):  # all the methods time complexity in this class : O(1)
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param value: data of your node
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child
    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right

    """returns the parent 
    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the value
    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value  # if the node is virtual it's value is None

    """returns the key
    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key  # if the node is virtual it's key is None

    """returns the height
    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height  # if the node is virtual it's height is -1

    """sets left child
    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node

    """sets right child
    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node

    """sets parent
    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node

    """sets key
    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key

    """sets value
    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value

    """sets the balance factor of the node
    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h

    """returns whether self is not a virtual node 
    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.height == -1:
            return False
        return True


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.root = AVLNode(None, None)
        self.size = 0

    """ 
    Searches for a value in the dictionary corresponding to the key.
    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: the AVLNode corresponding to key or None if key is not found.
    """

    def search(self, key):  # time complexity : O(log(n))
        # Start the search from the root of the AVL tree
        node = self.root

        # Iterate until reaching a virtual node
        while node.is_real_node():
            # If the current node's key matches the search key, return the node
            if node.key == key:
                return node
            # If the search key is smaller than the current node's key, search in the left subtree
            elif node.key > key:
                node = node.left
            # If the search key is greater than the current node's key, search in the right subtree
            else:
                node = node.right

        # If the search key is not found, return None
        return None

    """
    Inserts val at position i in the dictionary.

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of the item to be inserted into self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operations due to AVL rebalancing
    """

    def insert(self, key, val):  # time complexity : O(log(n))
        # Insert the key and value into the AVL tree
        self.root = self.insert_to_bst(self.root, None, key, val)

        # Increment the size of the AVL tree
        self.size += 1

        # Search for the newly inserted node
        node = self.search(key)
        parent_node = node.parent

        # If the inserted node is the root, no rebalancing needed
        if parent_node is None:
            return 0

        # Perform AVL rebalancing if needed and return the number of rebalancing operations
        return self.check_if_rotation_needed_and_do(parent_node, True)

    """
    Helper function that inserts a node into the binary search tree without changing heights.

    @type root: AVLNode
    @param root: the root node of the binary search tree
    @type parent: AVLNode
    @param parent: the parent node of the current root
    @type key: int
    @param key: key of the item to be inserted into the binary search tree
    @type val: any
    @param val: the value of the item
    @rtype: AVLNode
    @returns: the root of the binary search tree after insertion
    """

    def insert_to_bst(self, root, parent, key, val):  # time complexity : O(log(n))
        # Stop condition - if the root is a virtual node
        if not root.is_real_node():
            # Create a new node with the given key and value
            node = insert_new_node(key, val)
            node.parent = parent
            return node
        # If the key is less than the root's key, insert into the left subtree
        if key < root.key:
            root.left = self.insert_to_bst(root.left, root, key, val)
        # If the key is greater than or equal to the root's key, insert into the right subtree
        else:
            root.right = self.insert_to_bst(root.right, root, key, val)
        # Return the root of the subtree after insertion
        return root

    """ Compute current node's height"""

    def compute_height(self, node):  # time complexity : O(1)
        return 1 + max(node.left.height, node.right.height)

    """ Compute node's balance factor """

    def compute_bf(self, node):  # time complexity : O(1)
        BF = node.left.height - node.right.height
        return BF

    """
    Check if rotation is needed and perform rotation if necessary.

    @type parent_node: AVLNode
    @param parent_node: the parent node of the current node
    @type insert: bool
    @param insert: flag indicating whether this is an insertion operation
    @rtype: int
    @returns: the number of rebalancing operations performed
    """

    def check_if_rotation_needed_and_do(self, parent_node, insert):  # time complexity : O(log(n))

        res = 0  # Counter for rebalancing operations

        # Perform AVL rebalancing
        while parent_node is not None:
            # Calculate the balance factor and current height of the parent node
            BF = self.compute_bf(parent_node)
            curr_height = self.compute_height(parent_node)

            # Check if rebalancing is needed
            if abs(BF) < 2 and parent_node.height == curr_height:
                # No rebalancing needed, return the total number of rebalancing operations
                return res
            elif abs(BF) < 2 and parent_node.height != curr_height:
                # Adjust parent height and continue rebalancing
                parent_node.height = curr_height
                parent_node = parent_node.parent
                res += 1
            else:
                # Rebalancing needed, perform rotation and update res
                father = parent_node.parent
                res += self.rotating_for_balance(parent_node)
                parent_node = father
                if insert:
                    return res

        # Return the total number of rebalancing operations
        return res

    """ Doing the full cycle of rotation """

    def rotating_for_balance(self, parent_node):  # time complexity : O(1)
        # Rebalancing needed
        if self.compute_bf(parent_node) == -2:
            BF_child = self.compute_bf(parent_node.right)
            if BF_child == 1:
                # Perform right and left rotations
                self.right_rotation(parent_node.right, parent_node.right.left)
                self.left_rotation(parent_node, parent_node.right)
                return 2
            else:
                # Perform left rotation
                self.left_rotation(parent_node, parent_node.right)
                return 1
        else:
            BF_child = self.compute_bf(parent_node.left)
            if BF_child == -1:
                # Perform left and right rotations
                self.left_rotation(parent_node.left, parent_node.left.right)
                self.right_rotation(parent_node, parent_node.left)
                return 2
            else:
                # Perform right rotation
                self.right_rotation(parent_node, parent_node.left)
                return 1

    """ Doing a left rotation for fixing after insert / delete"""

    def left_rotation(self, B, A):  # time complexity : O(1)
        # Perform the left rotation
        B.right = A.left
        B.right.parent = B
        A.left = B
        A.parent = B.parent

        # Update parent references
        if A.parent is None:
            # If A is now the root node, update the root reference
            self.root = A
        elif A.parent.key < A.key:
            # If A is on the right side of its parent, update the right child reference of the parent
            A.parent.right = A
        else:
            # If A is on the left side of its parent, update the left child reference of the parent
            A.parent.left = A

        # Update parent reference of B to A
        B.parent = A

        # Recalculate and update heights
        B.height = self.compute_height(B)
        A.height = self.compute_height(A)

    """ Doing a right rotation for fixing after insert / delete"""

    def right_rotation(self, B, A):  # time complexity : O(1)
        # Perform the right rotation
        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent

        # Update parent references
        if A.parent is None:
            # If A is now the root node, update the root reference
            self.root = A
        elif A.parent.key < A.key:
            # If A is on the right side of its parent, update the right child reference of the parent
            A.parent.right = A
        else:
            # If A is on the left side of its parent, update the left child reference of the parent
            A.parent.left = A

        # Update parent reference of B to A
        B.parent = A

        # Recalculate and update heights
        B.height = self.compute_height(B)
        A.height = self.compute_height(A)

    """
    Deletes node from the dictionary.

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operations due to AVL rebalancing
    """

    def delete(self, node):  # time complexity : O(log(n))
        # Dealing with deleting the root
        if self.size == 1:
            self.root = AVLNode(None, None)
            self.size = 0
            return 0
        # Delete the node from the AVL tree and get the parent node of the deleted node
        parent_node = self.delete_bst(node)

        # Decrease the size of the AVL tree
        self.size -= 1

        # Perform AVL rebalancing if needed and return the number of rebalancing operations
        return self.check_if_rotation_needed_and_do(parent_node, False)

    """
    Delete from the binary search tree without changing heights.

    @type node: AVLNode
    @param node: The node to be deleted from the binary search tree.
    @rtype: AVLNode
    @returns: The parent node of the deleted node, or None if the root was deleted.
    """

    def delete_bst(self, node):  # time complexity : O(log(n))
        # Get the parent node of the node to be deleted
        father = node.parent

        # Case: Node is a leaf (has no children)
        if not node.right.is_real_node() and not node.left.is_real_node():
            # If the node is a right child, remove it from its parent's right
            if self.im_right_child(node):
                father.right = AVLNode(None, None)
                father.right.parent = father
            # If the node is a left child, remove it from its parent's left
            else:
                father.left = AVLNode(None, None)
                father.left.parent = father
            return father

        # Case: Node has only one child (either left or right)
        elif not node.right.is_real_node():
            if self.im_right_child(node):
                # If the node is a right child, replace it with its left child
                if father is None:
                    self.root = node.left
                    return None
                father.right = node.left
                father.left.parent = father
            else:
                # If the node is a left child, replace it with its left child
                if father is None:
                    self.root = node.left
                    return None
                father.left = node.left
                father.left.parent = father
            return father

        elif not node.left.is_real_node():
            if self.im_right_child(node):
                # If the node is a right child, replace it with its right child
                if father is None:
                    self.root = node.right
                father.right = node.right
                father.right.parent = father
            else:
                # If the node is a left child, replace it with its right child
                if father is None:
                    self.root = node.right
                father.left = node.right
                father.left.parent = father
            return father

        # Case: Node has two children
        else:
            # Find the successor node
            successor_node = self.successor(node)

            father = self.delete_bst(successor_node)
            if father is node:
                return self.replace_for_delete(node, successor_node)
            a = self.replace_for_delete(node, successor_node)
            # Delete the successor node recursively
            return father

    """ Check if the given node is the right child of its parent """

    def im_right_child(self, node):  # time complexity : O(1)
        if node.key >= node.parent.key:
            return True
        return False

    """ finds node's successor """

    def successor(self, node):  # time complexity : O(log(n))
        # If the node has a right child, return the minimum node in the right subtree
        if node.right.is_real_node:
            return self.min(node.right)
        # Otherwise, traverse up the tree until finding a parent node that is not the right child of its parent
        father = node.parent
        while father is not None and self.im_right_child(node):
            node = father
            father = father.parent
        # Return the parent node, which is the successor of the original node
        return father

    """ finds the node with the minimum key in node's subtree """

    def min(self, node):  # time complexity : O(log(n))
        # Traverse down the left subtree until reaching the minimum node (the leftmost node)
        while node.left.is_real_node():
            node = node.left
        # Return the minimum node found
        return node

    """ Replace a node during deletion in the binary search tree. """

    def replace_for_delete(self, node, successor):  # time complexity : O(1)
        # Set the parent, right child, left child, and height of the successor node
        successor.parent = node.parent
        successor.right = node.right
        successor.left = node.left
        successor.height = node.height

        # Update the root of the AVL tree if the parent of the successor node is None
        if successor.parent is None:
            self.root = successor
        # Update the right child of the parent of the successor node if it's a right child
        elif self.im_right_child(successor):
            successor.parent.right = successor
        # Update the left child of the parent of the successor node if it's a left child
        else:
            successor.parent.left = successor

        # Return the successor node after replacing the deleted node
        return successor

    """
    Returns an array representing the dictionary.

    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    """

    def avl_to_array(self):  # time complexity : O(n)
        # Initialize an empty list to store the elements of the AVL tree
        arr = []

        # Recursively convert the AVL tree to an array
        return self.rec_avl_to_array(self.root, arr)

    ''' Recursively traverse the AVL tree and append elements to the array. '''

    def rec_avl_to_array(self, node, arr):  # time complexity : O(n)
        # Base case: if the node is a virtual node, return None
        if not node.is_real_node():
            return None

        # Traverse the left subtree recursively
        self.rec_avl_to_array(node.left, arr)

        # Append the current node's key and value to the array
        arr.append((node.key, node.value))

        # Traverse the right subtree recursively
        self.rec_avl_to_array(node.right, arr)

        return arr

    """
    Returns the number of items in the dictionary.

    @rtype: int
    @returns: the number of items in the dictionary
    """

    def size(self):  # time complexity : O(1)
        return self.size

    """
    Splits the dictionary at the i'th index.

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):  # time complexity : O(log(n))

        # Create two empty AVL trees to store the split trees
        tree1 = AVLTree()
        tree2 = AVLTree()

        # Assign the left subtree of the given node to tree1
        tree1.root = node.left
        tree1.root.parent = None

        # Assign the right subtree of the given node to tree2
        tree2.root = node.right
        tree2.root.parent = None

        # Store the split trees in a list
        res = [tree1, tree2]

        # Traverse up the tree from the given node and split each parent node accordingly
        father = node.parent
        while father is not None:
            # Create a new AVL tree to join with tree1 or tree2 based on the parent's key
            tree_join = AVLTree()
            if father.key < node.key:
                tree_join.root = father.left
                tree_join.root.parent = None
                tree1.join(tree_join, father.key, father.value)
            else:
                tree_join.root = father.right
                tree_join.root.parent = None
                tree2.join(tree_join, father.key, father.value)
            father = father.parent

        # Return the list containing the two split AVL trees
        return res

    """
    Joins self with key and another AVLTree.

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separating self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):  # time complexity : O(the absolute value of the difference between the height +1)
        # Calculate the absolute height difference between the two trees
        res = abs(tree2.root.height - self.root.height) + 1
        self.size = 1 + tree2.size + self.size

        # If self is empty, assign tree2 to self
        if self.root.key is None:
            tree2.insert(key, val)
            self.root = tree2.root

        # If tree2 is empty, insert key and val into self
        elif tree2.root.key is None:
            self.insert(key, val)

        # If key is less than the root key of tree2, join self to the left of tree2
        elif self.root.key < tree2.root.key:
            self.join_avl(self, tree2, key, val)

        # Otherwise, join tree2 to the left of self
        else:
            self.join_avl(tree2, self, key, val)

        # Return the absolute height difference
        return res

    """ Joins two AVL trees. """

    def join_avl(self, tree1, tree2, key, val):
        # time complexity : O(the absolute value of the difference between the height +1)

        # Determine which tree has a greater height
        if tree2.root.height >= tree1.root.height:
            # If tree2 has a greater height, join tree1 to the left of tree2
            picked_node = tree2.root
            h = tree1.root.height
            while picked_node.height > h:
                picked_node = picked_node.left
            node_x = insert_new_node(key, val)
            node_x.left = tree1.root
            node_x.left.parent = node_x
            node_x.right = picked_node
            node_x.parent = picked_node.parent
            picked_node.parent = node_x
            if node_x.parent is None:
                self.root = node_x
            else:
                node_x.parent.left = node_x
                self.root = tree2.root
            node_x.height = self.compute_height(node_x)
            num = self.check_if_rotation_needed_and_do(node_x.parent, False)
        else:
            # If tree1 has a greater height, join tree2 to the right of tree1
            picked_node = tree1.root
            h = tree2.root.height
            while picked_node.height > h:
                picked_node = picked_node.right
            node_x = insert_new_node(key, val)
            node_x.right = tree2.root
            node_x.right.parent = node_x
            node_x.left = picked_node
            node_x.parent = picked_node.parent
            picked_node.parent = node_x
            node_x.parent.right = node_x
            self.root = tree1.root
            node_x.height = self.compute_height(node_x)
            num = self.check_if_rotation_needed_and_do(node_x.parent, False)

    """
    Returns the root of the tree representing the dictionary.

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):  # time complexity : O(1)
        return self.root


""" Creating a function for a new node in an AVL tree """


def insert_new_node(key, val):  # time complexity : O(1)
    # Creating placeholder nodes for the left and right children of the new node
    child_right = AVLNode(None, None)
    child_left = AVLNode(None, None)

    # Creating the actual node with the given key and value
    real_node = AVLNode(key, val)
    real_node.height = 0

    # Assigning the placeholder nodes as left and right children of the actual node
    real_node.left = child_left
    real_node.right = child_right

    # Updating parent references for the placeholder nodes to point to the actual node
    child_right.parent = real_node
    child_left.parent = real_node

    # Returning the newly created node
    return real_node
