# username - almoghaviv
# id1      - 207298720
# name1    - Almog Haviv
# id2      - 322539651
# name2    - tal9


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1  # Balance factor

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
        if self.is_real_node():
            return self.value
        return None

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node
        if self.right is None:
            self.height = 1 + self.left.height
        else:
            self.height = 1 + max(self.left.height, self.right.height)

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node
        if self.left is None:
            self.height = 1 + self.right.height
        else:
            self.height = 1 + max(self.left.height, self.right.height)

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node
        #if self.key < node.key:
        #   node.left = self
        #else:
        #    node.right = self
    # node.height = 1 + max(node.left.height, node.right.height)

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

    def set_height(self, h: object) -> object:
        self.height = h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.height != -1:
            return True
        return False


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.size = 0

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        node = self.root
        while node is not None:  # as long node is not a virtual node do:
            if node.key == key:  # found it!
                return node.value
            elif node.key > key:  # its in the right subtree
                node = node.left
            else:  # its in the left subtree
                node = node.right
        return None  # not found

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        parent_node, height = self.insert_bst(key, val)
        while parent_node is not None:
            BF = self.compute_bf(parent_node)
            if abs(BF) < 2 and parent_node.height == height:
                return 0
            elif abs(BF) < 2 and parent_node.height != height:
                parent_node = parent_node.parent
            else:
                if parent_node.right is not None:
                    BF_child = self.compute_bf(parent_node.right)
                    if BF_child == -1:
                        self.left_rotation(parent_node, parent_node.right)
                        return 1
                    else:
                        self.right_rotation()
                        self.left_rotation()
                        return 2
                else:
                    BF_child = self.compute_bf(parent_node.left)
                    if BF_child == -1:
                        self.left_rotation()
                        self.right_rotation()
                        return 2
                    else:
                        self.right_rotation()
                        return 1


    def insert_bst(self, key, val):
        parent = None  # this will be the parent of the new node
        node = self.root
        height = -1
        while node is not None:  # keep descending the tree
            parent = node
            if key < node.key:  # the node should be in the left subtree
                node = node.left
            else:  # the node should be in the right subtree
                node = node.right

        if parent is None:  # was an empty tree, need to update root
            self.root = AVLNode(key, val)
            self.root.set_height(0)  # set the height of the new root
        elif key < parent.key:
            height = parent.height
            parent.left = AVLNode(key, val)
            parent.left.set_parent(parent)  # set the parent of the new left child
        else:
            height = parent.height
            parent.right = AVLNode(key, val)
            parent.right.set_parent(parent)  # set the parent of the new right child

        self.size += 1  # increase the size of the tree
        return parent, height


    def compute_bf(self, node):
        if node.left is None and node.right is None:
            BF = 0
        if node.left is None:
            BF = -1 - node.right.height

        BF = node.left.height - node.right.height
        return BF


    def left_rotation(self, node1, node2):
        if node1 is self.root:
            self.root = node2

        else:
            # Set the parent of node2 to be the same as the parent of node1
             node2.parent = node1.parent

            # Update the right child of the parent of node1 to be node2
             node2.parent.right = node2

        # Set the left child of node2 to be node1
        node2.left = node1

        # Update the parent of node1 to be node2
        node1.parent = node2

        # Set the right child of node1 to be the left child of node2
        node1.right = node2.left

        # Update the parent of the left child of node2 to be node1
        node2.left.parent = node1

    def right_rotation(self, node1, node2):
        if node1 is self.root:
            self.root = node2

        else:
            # Set the parent of node2 to be the same as the parent of node1
            node2.parent = node1.parent

            # Update the left child of the parent of node1 to be node2
            node1.parent.left = node2

        # Update the parent of node1 to be node2
        node1.parent = node2

        # Set the right child of node2 to be node1
        node2.right = node1

        # Set the left child of node1 to be the right child of node2
        node1.left = node2.right

        # Update the parent of the right child of node2 to be node1
        node2.right.parent = node1

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        return -1

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """splits the dictionary at the i'th index

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None

    """joins self with key and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree2
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree2, key, val):
        return None

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return None
