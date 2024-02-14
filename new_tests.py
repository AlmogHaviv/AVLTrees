from avl_template_new import AVLTree, AVLNode

AVLNode.__repr__ = lambda self: str(self.get_key())

class tests:
    # These functions do the actual testing
    @staticmethod
    def testInsertDelete():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]
        
        # test RL rotation
        testHelper.insert_array(tree, keys[0:5])
        testHelper.assert_neighbors(tree, 7, 4, 11, 5)

        # test LR rotation
        testHelper.insert_array(tree, keys[5:6]) # insert 15
        testHelper.assert_neighbors(tree, 15, None, None, 6)
        testHelper.assert_neighbors(tree, 23, 15, 30, 6)
        testHelper.assert_neighbors(tree, 11, 7, 23, 6)
        testHelper.assert_neighbors(tree, 7, 4, None,6)
        testHelper.test_root(tree, 11)
        
        # test L rotation
        testHelper.insert_array(tree, keys[6:8]) # insert 40, 43
        testHelper.assert_neighbors(tree, 40, 30, 43,8)
        testHelper.assert_neighbors(tree, 23, 15, 40,8)
        
        # testHelper R rotation
        testHelper.insert_array(tree, keys[8:10]) # insert 2, 1
        testHelper.assert_neighbors(tree, 4, 2, 7,10)
        testHelper.assert_neighbors(tree, 2, 1, None,10)
        testHelper.assert_neighbors(tree, 7, None, None,10)
        testHelper.assert_neighbors(tree, 11, 4, 23,10)
        testHelper.test_root(tree, 11)
        
        # test deletions
        testHelper.test_deletion(tree, 1, 2)
        testHelper.assert_neighbors(tree, 4, 2, 7,9)
        testHelper.assert_neighbors(tree, 2, None, None,9)
        testHelper.assert_neighbors(tree, 7, None, None,9)
        testHelper.assert_neighbors(tree, 11, 4, 23,9)
        testHelper.test_root(tree, 11)
        
        testHelper.test_deletion(tree, 2, 0)
        testHelper.assert_neighbors(tree, 4, None, 7,8)
        testHelper.assert_neighbors(tree, 7, None, None,8)
        testHelper.assert_neighbors(tree, 11, 4, 23,8)
        testHelper.test_root(tree, 11)
        
        # test L rotation
        testHelper.test_deletion(tree, 7, 2)
        testHelper.assert_neighbors(tree, 11, 4, 15,7)
        testHelper.assert_neighbors(tree, 23, 11, 40,7)
        testHelper.test_root(tree, 23)
        
        testHelper.test_deletion(tree, 23, 1)
        testHelper.assert_neighbors(tree, 30, 11, 40,6)
        testHelper.assert_neighbors(tree, 11, 4, 15,6)
        testHelper.assert_neighbors(tree, 40, None, 43,6)
        
        # TODO: test deleting node with no successor
        # TODO: empty the tree and test to see everything is correct
        
    @staticmethod
    def test_avl_to_array():
        tree = AVLTree()

        keys = [23, 4, 30, 11, 7, 15, 40, 43, 2, 1]
        testHelper.insert_array(tree, keys)

        testHelper.test_avl2array(tree, keys)
        
    @staticmethod
    def test_join():
        tree_tuple = testHelper.test_join_helper([4, 2, 5], 
                                                 [20, 22, 16, 18, 14], 
                                                 10, 
                                                 10,
                                                 2)
        for tree in tree_tuple:
            #  tests for trees [4, 2, 5] and [20, 22, 16, 18, 14]
            #  balancing should be called on node c and node x
            testHelper.test_root(tree, 10)
            testHelper.assert_neighbors(tree, 10, 4, 20, 9)
            testHelper.assert_neighbors(tree, 4, 2, 5, 9)
            testHelper.assert_neighbors(tree, 20, 16, 22, 9)
            testHelper.assert_neighbors(tree, 16, 14, 18, 9)

        tree_tuple = testHelper.test_join_helper([4, 2, 5], 
                                                 [20, 22, 16],
                                                 10, 
                                                 10,
                                                 1)
        for tree in tree_tuple:
            testHelper.test_root(tree, 10)
            testHelper.assert_neighbors(tree, 10, 4, 20, 7)
            testHelper.assert_neighbors(tree, 20, 16, 22, 7)
            testHelper.assert_neighbors(tree, 4, 2, 5, 7)
        
        tree_tuple = testHelper.test_join_helper([],
                                                 [],
                                                 10,
                                                 10,
                                                 1)
        
        for tree in tree_tuple:
            testHelper.test_root(tree, 10)
            testHelper.assert_neighbors(tree, 10, None, None, 1)
            
        tree_tuple = testHelper.test_join_helper([12],
                                                 [],
                                                 10,
                                                 10,
                                                 2)
        
        for tree in tree_tuple:
            testHelper.test_root(tree, 12)
            testHelper.assert_neighbors(tree, 12, 10, None, 2)
            
    @staticmethod
    def test_split():
        
        t1, t2 = testHelper.test_split_helper([20], 20)
        
        assert t1.get_root() is None and t2.get_root() is None, \
            f"Splitting a tree with only one node did not return two empty trees"

        t1, t2 = testHelper.test_split_helper([20, 10, 12, 8, 9, 25, 23, 27],
                                              12)
        
        testHelper.assert_neighbors(t1, 9, 8, 10, 3)
        testHelper.assert_neighbors(t2, 23, 20, 25, 4)
        testHelper.assert_neighbors(t2, 25, None, 27, 4)
        
        t1, t2 = testHelper.test_split_helper([20, 10, 12, 8, 9, 25, 23, 27],
                                25)
        # add tests
        
    
class testHelper:
    # Helper functions for tests class. No need to use any of them.
    @staticmethod
    def assert_neighbors(tree, node_key, left_key, right_key, size):
        node = tree.search(node_key)
        search_right_key = tree.search(right_key) if right_key is not None else None
        search_left_key = tree.search(left_key) if left_key is not None else None
        right_result = search_right_key.get_key() if search_right_key is not None else None
        left_result = search_left_key.get_key() if search_left_key is not None else None
        node_right = node.get_right().get_key() if node is not None else None
        node_left = node.get_left().get_key() if node is not None else None

        assert node_right is right_result, \
            f"Checking neighbors for {node_key}, right neighbor is {node_right} but search returned something else when searching for key {right_key}"
        assert node_left is left_result, \
            f"Checking neighbors for {node_key}, left neighbor is {node_left} but search returned something else when searching for key {left_key}"
        assert tree.size()==size, \
            f"Expected tree size to be {size} but got {tree.size()} instead"
        print('oogabooga')
        
    @staticmethod
    def insert_array(tree, key_array):
        for key in key_array:
            tree.insert(key, key)
            
    @staticmethod
    def test_deletion(tree, deletion_key, num_balancing_actions):
        deletion_node = tree.search(deletion_key)
        check_balancing_actions = tree.delete(deletion_node)

        assert tree.search(deletion_key) is None, \
            f"Deleting {deletion_key}, searching for deleted key did not return None"
        assert check_balancing_actions == num_balancing_actions, \
            f"Deleting {deletion_key}, deletion returned {check_balancing_actions} balancing actions instead of {num_balancing_actions}"
    
    @staticmethod
    def test_root(tree, root_key):
        assert tree.get_root() is tree.search(root_key), \
            f"Root is {tree.get_root()}, but search returned something else when searching for expected root key {root_key}"    
    
    """
    @param tree: tree to test
    @param tree_keys_array: Array with all keys present in the tree
    """
    @staticmethod
    def test_avl2array(tree, tree_keys_array):

        expectedArray = [(key, key) for key in sorted(tree_keys_array)] # tests.insert_array uses the key as a value, so we do the same here
        avl_to_array_result = tree.avl_to_array()

        assert expectedArray == avl_to_array_result, \
            f"Expected avl_to_array() to return \n{expectedArray}\nbut got\n{avl_to_array_result}"

    """
    tests joining two trees in either order (tree1 to tree2 or tree2 to tree1)
    @param key_array1: keys in one of the trees
    @param key_array2: keys in one of the trees
    @returns: a tuple of trees where the first tree was joined in one order and the second was joined in another
    """
    @staticmethod
    def test_join_helper(key_array1, key_array2, joiningNodeKey, joiningNodeValue, expectedDiff):
        tree1 = AVLTree()
        tree2 = AVLTree()

        testHelper.insert_array(tree1, key_array1)
        testHelper.insert_array(tree2, key_array2)
        
        actualDiff = tree1.join(tree2, joiningNodeKey, joiningNodeValue)
        assert actualDiff == expectedDiff, \
            f"Expected join to return {expectedDiff} but got {actualDiff} instead"

        tree1_flip_order = AVLTree()
        tree2_flip_order = AVLTree()

        testHelper.insert_array(tree1_flip_order, key_array2)
        testHelper.insert_array(tree2_flip_order, key_array1)
        
        actualDiff = tree1_flip_order.join(tree2_flip_order, joiningNodeKey, joiningNodeValue)
        assert actualDiff == expectedDiff, \
            f"With flipped order of trees in join, expected join to return {expectedDiff} but got {actualDiff} instead"

        return [tree1, tree1_flip_order]

    """splits a tree with keys key_array by split_node_key, throws error
    if split_node_key is not in key_array and wasn't found in the tree
    """
    @staticmethod
    def test_split_helper(key_array, split_node_key):
        tree = AVLTree()
        testHelper.insert_array(tree, key_array)
        split_node_key = tree.search(split_node_key)
        
        assert split_node_key is not None, \
            f"Key {split_node_key} was not found by search"
        
        return tree.split(split_node_key)