import unittest
import avl_template_new


class TestAVLTree(unittest.TestCase):

    def test_insert_and_search(self):
        avl_tree = avl_template_new.AVLTree()

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
        avl_tree = avl_template_new.AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(3, "three")
        avl_tree.insert(2, "two")
        avl_tree.insert(1, "one")

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "two")
        self.assertEqual(avl_tree.root.get_left().get_value(), "one")
        self.assertEqual(avl_tree.root.get_right().get_value(), "three")

    def test_avl_insert_rebalance2(self):
        avl_tree = avl_template_new.AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(6, "six")
        avl_tree.insert(7, "seven")
        avl_tree.insert(8, "eight")

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "seven")
        self.assertEqual(avl_tree.root.get_left().get_value(), "six")
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")
    
    def test_avl_insert_rebalance3(self):
        avl_tree = avl_template_new.AVLTree()

        # Insert nodes into the AVL tree to test rebalancing
        avl_tree.insert(6, "six")
        avl_tree.insert(8, "eight")
        avl_tree.insert(7, "seven")
        

        # Check that the AVL tree is balanced after insertions
        self.assertEqual(avl_tree.root.get_value(), "seven")
        self.assertEqual(avl_tree.root.get_left().get_value(), "six")
        self.assertEqual(avl_tree.root.get_right().get_value(), "eight")

    def test_avl_insert_rebalance4(self):
            avl_tree = avl_template_new.AVLTree()

            # Insert nodes into the AVL tree to test rebalancing
            avl_tree.insert(8, "eight")
            avl_tree.insert(6, "six")
            avl_tree.insert(7, "seven")
            

            # Check that the AVL tree is balanced after insertions
            self.assertEqual(avl_tree.root.get_value(), "seven")
            self.assertEqual(avl_tree.root.get_left().get_value(), "six")
            self.assertEqual(avl_tree.root.get_right().get_value(), "eight")


    

if __name__ == '__main__':
   unittest.main()