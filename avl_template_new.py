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
    @param key: key for your node to be searched according to
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

    """returns the key
    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """
    def get_key(self):
        return self.key

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
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        node = self.root
        while node.is_real_node():  # as long node is not a virtual node do:
            if node.key == key:  # found it!
                return node
            elif node.key > key:  # it's in the right subtree
                node = node.left
            else:  # it's in the left subtree
                node = node.right
        return None  # not found

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
    def insert(self, key, val):
        # Insert the key and value into the AVL tree
        self.root = self.insert_to_bst(self.root, None, key, val)

        # Search for the newly inserted node
        node = self.search(key)
        parent_node = node.parent
        
		# Increment the size of the dictionary
        self.size += 1
        
		# dealing with root node
        if parent_node is None:
            return 0
      
        # Perform AVL rebalancing
        while parent_node is not None:
            BF = self.compute_bf(parent_node)
            curr_height = self.compute_height(parent_node)
            if abs(BF) < 2 and parent_node.height == curr_height:
                # No rebalancing needed
                return 0
            elif abs(BF) < 2 and parent_node.height != curr_height:
                # Adjust parent height and continue rebalancing
                parent_node.height = curr_height
                parent_node = parent_node.parent
                if parent_node is None:
                    return 0
            else:
                return self.rotating_for_balance(parent_node)

    # Recursive option for inserting a node without changing heights
    def insert_to_bst(self, root, parent, key, val):
        # Stop condition - if a child is imaginary
        if not root.is_real_node():
            node = insert_new_node(key, val)
            node.parent = parent
            return node

        if key < root.key:
            root.left = self.insert_to_bst(root.left, root, key, val)
        else:
            root.right = self.insert_to_bst(root.right, root, key, val)

        return root

    # Compute current height
    def compute_height(self, node):
        return 1 + max(node.left.height, node.right.height)

    # Compute balance factor
    def compute_bf(self, node):
        BF = node.left.height - node.right.height
        return BF
    
	# Doing the full cycle of rotation for while - loop
    def rotating_for_balance(self, parent_node):
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


    # Doing rhe left rotation for insert/delete
    def left_rotation(self, B, A):
        B.right = A.left
        B.right.parent = B
        A.left = B 
        A.parent = B.parent
        if A.parent is None:
            self.root = A
        elif A.parent.key < A.key:
            A.parent.right = A
        else:
            A.parent.left = A
        B.parent = A
        
		# setting the heights
        B.height = self.compute_height(B)
        A.height = self.compute_height(A)
        
	# Doing rhe right rotation for insert/delete
    def right_rotation(self, B, A):
        B.left = A.right
        B.left.parent = B
        A.right = B 
        A.parent = B.parent
        if A.parent is None:
            self.root = A
        elif A.parent.key < A.key:
            A.parent.right = A
        else:
            A.parent.left = A
        B.parent = A
 
		# setting the heights
        B.height = self.compute_height(B)
        A.height = self.compute_height(A)

    """
    Deletes node from the dictionary.

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operations due to AVL rebalancing
    """
    def delete(self, node):
        parent_node = self.delete_bst(node)
        self.size -= 1
        if parent_node is None:
            return 0
        res = 0
        # Perform AVL rebalancing
        while parent_node is not None:
            BF = self.compute_bf(parent_node)
            curr_height = self.compute_height(parent_node)
            if abs(BF) < 2 and parent_node.height == curr_height:
                # No rebalancing needed
                return res
            elif abs(BF) < 2 and parent_node.height != curr_height:
                # Adjust parent height and continue rebalancing
                parent_node.height = curr_height
                parent_node = parent_node.parent
                
            else:
                res += self.rotating_for_balance(parent_node)
                parent_node = parent_node.parent
                
        return res
    # delete from bst without changing heights
    def delete_bst(self, node):
        father = node.parent
        # if the node is leaf
        if not node.right.is_real_node() and not node.left.is_real_node():
            # if the node is root
            if father is None:
                self.root = AVLNode(None, None)
                return None

            if self.im_right_child(node):
                father.right = AVLNode(None, None)
                father.right.parent = father
    
            else:
                father.left = AVLNode(None, None)
                father.left.parent = father
            return father
        
        # if the node have only one child
        elif not node.right.is_real_node():
           if self.im_right_child(node):
                if father is None:
                    self.root = node.left
                    return None
                father.right = node.left
                father.left.parent = father
           else:
               if father is None:
                   self.root = node.left
                   return None
               father.left = node.left
               father.left.parent = father
           return father
        
        elif not node.left.is_real_node():
            if self.im_right_child(node):
                if father is None:
                    self.root = node.right
                father.right = node.right
                father.right.parent = father
            else:
                if father is None:
                    self.root = node.right
                father.left = node.right
                father.left.parent = father
            return father
        
        # the node have 2 children
        else:
            successor_node = self.successor(node)
            node.key = successor_node.key
            node.value = successor_node.value
            return self.delete_bst(successor_node)

       

    def im_right_child (self, node):
        if node.key >= node.parent.key:
            return True
        return False




    def successor(self, node):
        if node.right.is_real_node:
            return self.min(node.right)
        father = node.parent
        while father is not None and self.im_right_child(node):
            node = father
            father = father.parent
        return father


    def min(self,node):
        while node.left.is_real_node():
            node= node.left
        return node


    """
    Returns an array representing the dictionary.

    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    """
    def avl_to_array(self):
        return None

    """
    Returns the number of items in the dictionary.

    @rtype: int
    @returns: the number of items in the dictionary
    """
    def size(self):
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
    def split(self, node):
        return None

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
    def join(self, tree2, key, val):
        return None

    """
    Returns the root of the tree representing the dictionary.

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """
    def get_root(self):
        return self.root


# Creating a function for a new node in an AVL tree
def insert_new_node(key, val):
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
