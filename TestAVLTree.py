import unittest
from AVLTree import AVLTree, AVLNode



class TestAVLTree(unittest.TestCase):

    def test_insert_and_search(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")
        avl_tree.insert(2, "two")
        avl_tree.insert(4, "four")

        # Search for values in the AVL tree
        self.assertEqual(avl_tree.search(5).value, "five")
        self.assertEqual(avl_tree.search(3).value, "three")
        self.assertEqual(avl_tree.search(7).value, "seven")
        self.assertEqual(avl_tree.search(2).value, "two")
        self.assertEqual(avl_tree.search(4).value, "four")

        # Search for a non-existing value
        self.assertIsNone(avl_tree.search(6))

    def test_avl_insert_rebalance(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(3, "three")
        avl_tree.insert(2, "two")
        avl_tree.insert(1, "one")

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "two")
        self.assertEqual(avl_tree.root.get_left().get_value(), "one")
        self.assertEqual(avl_tree.root.get_right().get_value(), "three")

    def test_avl_insert_rebalance2(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(6, "six")
        avl_tree.insert(7, "seven")
        avl_tree.insert(8, "eight")

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "seven")
        self.assertEqual(avl_tree.root.get_left().get_value(), "six")
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")

    def test_avl_insert_rebalance3(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(6, "six")
        avl_tree.insert(8, "eight")
        avl_tree.insert(7, "seven")

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "seven")
        self.assertEqual(avl_tree.root.get_left().get_value(), "six")
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")

    def test_avl_insert_rebalance4(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(1, "eight")
        avl_tree.insert(2, "six")
        res = avl_tree.insert(3, "seven")
        self.assertEqual(res, 2)
        # Check that the AVL tree is balanced after insertions


    def test_avl_insert_rebalance5(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(8, "eight")
        avl_tree.insert(6, "six")
        avl_tree.insert(7, "seven")

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "seven")
        self.assertEqual(avl_tree.root.get_left().get_value(), "six")
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")

    def test_avl_insert_rebalance_large_tree(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        nodes = [(i, str(i)) for i in range(1, 11)]  # Inserting numbers 1 to 100
        for key, value in nodes:
            avl_tree.insert(key, value)

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "4")  # Root should be the middle element
        self.assertEqual(avl_tree.root.get_left().get_value(), "2")  # Left child of root
        self.assertEqual(avl_tree.root.get_right().get_value(), "8")  # Right child of root

        # Check some specific nodes to ensure correct insertion and balancing
        self.assertEqual(avl_tree.search(1).value, "1")
        self.assertEqual(avl_tree.search(5).value, "5")
        self.assertEqual(avl_tree.search(7).value, "7")

    def test_avl_delete_leaf_node(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")

        # Delete a leaf node
        avl_tree.delete(avl_tree.search(3))

        # Check that the node has been deleted
        self.assertIsNone(avl_tree.search(3))

    def test_avl_delete_node_with_one_child(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")
        avl_tree.insert(6, "six")

        # Delete a node with one child
        avl_tree.delete(avl_tree.search(7))

        # Check that the node has been deleted and the child node is connected to the parent
        self.assertIsNone(avl_tree.search(7))
        self.assertEqual(avl_tree.root.get_right().get_value(), "six")

    def test_avl_delete_node_with_two_children(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(5, "five")
        avl_tree.insert(3, "three")
        avl_tree.insert(7, "seven")
        avl_tree.insert(6, "six")
        avl_tree.insert(8, "eight")

        # Delete a node with two children
        avl_tree.delete(avl_tree.search(7))

        # Check that the node has been deleted and the successor node has taken its place
        self.assertIsNone(avl_tree.search(7))
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")
        self.assertEqual(avl_tree.root.get_right().get_left().get_value(), "six")

    def test_avl_delete_leaf_node_ten(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        nodes = [(i, str(i)) for i in range(1, 11)]  # Inserting numbers 1 to 10
        for key, value in nodes:
            avl_tree.insert(key, value)

        # Delete a leaf node
        avl_tree.delete(avl_tree.search(10))

        # Check that the node has been deleted
        self.assertIsNone(avl_tree.search(10))

    def test_avl_delete_node_with_one_child_ten(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        nodes = [(i, str(i)) for i in range(1, 11)]  # Inserting numbers 1 to 10
        for key, value in nodes:
            avl_tree.insert(key, value)

        # Delete a node with one child
        avl_tree.delete(avl_tree.search(9))

        # Check that the node has been deleted and the child node is connected to the parent
        self.assertIsNone(avl_tree.search(9))
        self.assertEqual(avl_tree.root.get_value(), "4")
        self.assertEqual(avl_tree.root.right.right.get_value(), "10")
        self.assertEqual(avl_tree.root.right.get_value(), "8")

    def test_avl_delete_node_with_two_children_ten(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(15, "15")
        avl_tree.insert(8, "8")
        avl_tree.insert(22, "22")
        avl_tree.insert(4, "4")
        avl_tree.insert(20, "20")
        avl_tree.insert(11, "11")
        avl_tree.insert(24, "24")
        avl_tree.insert(2, "2")
        avl_tree.insert(18, "18")
        avl_tree.insert(12, "12")
        avl_tree.insert(9, "9")
        avl_tree.insert(13, "13")

        # Delete a node with two children
        ans = avl_tree.delete(avl_tree.search(11))

        # Check that the node has been deleted and the successor node has taken its place
        self.assertIsNone(avl_tree.search(11))
        self.assertEqual(avl_tree.root.get_value(), "15")
        self.assertEqual(avl_tree.root.get_left().get_value(), "8")
        self.assertEqual(avl_tree.root.get_left().get_right().get_value(), "12")
        self.assertEqual(avl_tree.root.get_right().get_right().get_value(), "24")
        self.assertEqual(avl_tree.root.get_left().get_right().get_right().get_value(), "13")
        self.assertEqual(ans, 3)

    def test_avl_delete_node_with_two_rotations(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        avl_tree.insert(15, "15")
        avl_tree.insert(8, "8")
        avl_tree.insert(22, "22")
        avl_tree.insert(4, "4")
        avl_tree.insert(20, "20")
        avl_tree.insert(11, "11")
        avl_tree.insert(24, "24")
        avl_tree.insert(2, "2")
        avl_tree.insert(18, "18")
        avl_tree.insert(12, "12")
        avl_tree.insert(9, "9")
        avl_tree.insert(13, "13")

        # Delete a node with two children
        avl_tree.delete(avl_tree.search(24))

        # Check that the node has been deleted and the successor node has taken its place
        self.assertIsNone(avl_tree.search(24))
        self.assertEqual(avl_tree.root.get_value(), "11")
        self.assertEqual(avl_tree.root.get_left().get_value(), "8")
        self.assertEqual(avl_tree.root.get_right().get_right().get_value(), "20")

    def test_avl_avl_to_array(self):
        avl_tree = AVLTree()

        # Insert nodes into the AVL tree
        nodes = [(i, str(i)) for i in range(1, 11)]  # Inserting numbers 1 to 10
        for key, value in nodes:
            avl_tree.insert(key, value)

        # Delete a node with two children
        arr = avl_tree.avl_to_array()

        # Check that the node has been deleted and the successor node has taken its place
        self.assertEqual(arr, nodes)

    def test_join(self):
        # Create two AVL trees
        tree1 = AVLTree()
        tree2 = AVLTree()

        # Insert some nodes into the AVL trees
        tree1.insert(3, "three")
        tree1.insert(5, "five")
        tree1.insert(7, "seven")

        tree2.insert(10, "ten")
        tree2.insert(12, "twelve")
        tree2.insert(15, "fifteen")

        # Join tree1 with tree2
        height_difference = tree1.join(tree2, 8, "eight")

        # Check if the join operation was successful
        self.assertEqual(height_difference, 1)
        self.assertEqual(tree1.root.get_value(), "eight")

    def test_join1(self):
        avl_tree1 = AVLTree()
        avl_tree2 = AVLTree()

        # Insert nodes into the AVL tree
        nodes1 = [(i, str(i)) for i in range(1, 3)]  # Inserting numbers 1 to 10
        for key, value in nodes1:
            avl_tree1.insert(key, value)

        nodes2 = [(i, str(i)) for i in range(4, 12)]  # Inserting numbers 1 to 10
        for key, value in nodes2:
            avl_tree2.insert(key, value)

        res = avl_tree1.join(avl_tree2, 3, "3")

        # Check that the node has been deleted and the successor node has taken its place
        self.assertEqual(res, 3)
        self.assertEqual(avl_tree1.root.get_value(), "7")
        self.assertEqual(avl_tree1.root.right.get_value(), "9")
        self.assertEqual(avl_tree1.root.left.get_value(), "3")
        self.assertEqual(avl_tree1.root.left.right.get_value(), "5")
        self.assertEqual(avl_tree1.root.left.left.get_value(), "1")
    def test_join2(self):
        # Create two AVL trees
        tree1 = AVLTree()
        tree2 = AVLTree()

        # Insert some nodes into the AVL trees
        tree1.insert(2, "2")


        tree2.insert(5, "5")
        tree2.insert(4, "4")


        # Join tree1 with tree2
        height_difference = tree1.join(tree2, 3, "3")

        # Check if the join operation was successful
        self.assertEqual(height_difference, 2)
        self.assertEqual(tree1.root.get_value(), "3")
        self.assertEqual(tree1.root.left.get_value(), "2")
        self.assertEqual(tree1.root.right.get_key(), 5)
        self.assertEqual(tree1.root.right.left.get_value(), "4")



    def test_split1(self):
        tree1 = AVLTree()

        # Insert nodes into the AVL tree
        tree1.insert(4, "4")
        tree1.insert(2, "2")
        tree1.insert(5, "5")
        tree1.insert(1, "1")
        tree1.insert(3, "3")
        x = tree1.search(3)

        res = tree1.split(x)

        # Check that the node has been deleted and the successor node has taken its place
        self.assertEqual(res[0].root.key, 1)
        self.assertEqual(res[1].root.key, 5)
        self.assertEqual(res[0].root.right.key, 2)
        self.assertEqual(res[1].root.left.key, 4)

    def test_split2(self):
        tree1 = AVLTree()

        # Insert nodes into the AVL tree
        tree1.insert(6, "4")
        tree1.insert(2, "2")
        tree1.insert(8, "5")
        tree1.insert(1, "1")
        tree1.insert(4, "3")
        tree1.insert(7, "4")
        tree1.insert(9, "2")
        tree1.insert(3, "5")
        tree1.insert(5, "1")
        x = tree1.search(4)

        res = tree1.split(x)

        # Check that the node has been deleted and the successor node has taken its place
        self.assertEqual(res[0].root.key, 2)
        self.assertEqual(res[1].root.key, 8)
        self.assertEqual(res[0].root.right.key, 3)
        self.assertEqual(res[0].root.left.key, 1)
        self.assertEqual(res[1].root.left.key, 6)
        self.assertEqual(res[1].root.right.key, 9)


if __name__ == '__main__':
    unittest.main()
