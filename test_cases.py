from AVLTree import AVLTree, AVLNode


# Tests:

def create_tree(keys: list):
    tree = AVLTree()
    for key in keys:
        # print(f"tree size: {tree.tree_size}")
        # print(f"inserting: {key}, balance_actions_taken: {tree.insert(key, key)}")
        tree.insert(key, key)
    # tree.display_tree()
    # print("array:", tree.AVL_to_array())

    return tree


# used for testing insert, rotations and AVL to array
def test_tree_creation():
    example_tree_1 = create_tree([1, 2, 3, 4, 5, 6, 7, 8])
    # TREES 2-5 ARE FOR TESTING THE ROTATIONS
    example_tree_2 = create_tree([1, 2, 3])
    example_tree_3 = create_tree([3, 2, 1])
    example_tree_4 = create_tree([3, 1, 2])
    example_tree_5 = create_tree([1, 3, 2])
    example_tree_6 = create_tree([1, 8, 4, 6, 3, 9, 2, 14])
    example_tree_7 = create_tree([7, 3, 11, 1, 5, 6])  # a more complex rotation (kids moving as well)
    example_tree_10 = create_tree([3, 2, 6, 7, 4, 1, 5])
    # example_tree_1.display_tree()
    print(example_tree_1.avl_to_array())


# Remember to test balance actions taken
def test_delete():
    # delete root, only node
    example_tree_1 = create_tree([1])
    print(f"deleting {1}, balance actions: ", example_tree_1.delete(example_tree_1.search(1)))
    print(example_tree_1.avl_to_array())

    # delete root, node with one child
    example_tree_0 = create_tree([1, 2])
    print(f"deleting {1}: ", example_tree_0.delete(example_tree_0.search(1)))
    # example_tree_0.display_tree()
    print(example_tree_0.avl_to_array())

    # delete root, node with 2 children
    example_tree_2 = create_tree([2, 1, 3])
    print("finished creating tree!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"deleting {2}: ", example_tree_2.delete(example_tree_2.search(2)))
    # example_tree_2.display_tree()
    print(example_tree_2.avl_to_array())

    # delete leaf no root
    example_tree_3 = create_tree([2, 1])
    print(f"deleting {1}: ", example_tree_3.delete(example_tree_3.search(1)))
    # example_tree_3.display_tree()
    print(example_tree_3.avl_to_array())

    # delete node with one child no root
    example_tree_4 = create_tree([2, 1, 3, 4])
    print(f"deleting {3}: ", example_tree_4.delete(example_tree_4.search(3)))
    # example_tree_4.display_tree()
    print(example_tree_4.avl_to_array())

    # delete node with 2 children
    example_tree_5 = create_tree([2, 1, 4, 3, 5])
    print(f"deleting {4}: ", example_tree_5.delete(example_tree_5.search(4)))
    # example_tree_5.display_tree()
    print(example_tree_5.avl_to_array())

    # delete node that will cause a rotation
    example_tree_6 = create_tree([2, 1, 3, 4])
    print(f"deleting {1}: ", example_tree_6.delete(example_tree_6.search(1)))
    # example_tree_6.display_tree()
    print(example_tree_6.avl_to_array())

    # Again, delete node that will cause a rotation
    example_tree_7 = create_tree([2, 1, 4, 3])
    print(f"deleting {1}: ", example_tree_7.delete(example_tree_7.search(1)))
    # example_tree_7.display_tree()
    print(example_tree_7.avl_to_array())


def test_join():
    # join 2 empty trees:
    example_tree_0A = create_tree([])
    example_tree_0B = create_tree([])
    example_tree_0A.join(example_tree_0B, 1, 1)
    # example_tree_0A.display_tree()
    print(example_tree_0A.avl_to_array())

    # join 1 empty tree (smaller empty):
    example_tree_1A = create_tree([])
    example_tree_1B = create_tree([2, 3])
    example_tree_1A.join(example_tree_1B, 1, 1)
    # example_tree_1A.display_tree()
    print(example_tree_1A.avl_to_array())

    # join 1 empty tree (bigger empty):
    example_tree_2A = create_tree([1, 2])
    example_tree_2B = create_tree([])
    example_tree_2A.join(example_tree_2B, 3, 3)
    # example_tree_2A.display_tree()
    print(example_tree_2A.avl_to_array())

    # join two trees same height
    example_tree_3A = create_tree([2, 1, 3])
    example_tree_3B = create_tree([6, 5, 7])
    example_tree_3A.join(example_tree_3B, 4, 4)
    # example_tree_3A.display_tree()
    print(example_tree_3A.avl_to_array())

    # join two trees different height
    example_tree_4A = create_tree([2, 1, 3])
    example_tree_4B = create_tree([5])
    example_tree_4A.join(example_tree_4B, 4, 4)
    # example_tree_4A.display_tree()
    print(example_tree_4A.avl_to_array())

    # join two trees that will cause a rotation
    example_tree_4A = create_tree([2])
    example_tree_4B = create_tree([4, 5])
    example_tree_4A.join(example_tree_4B, 3, 3)
    # example_tree_4A.display_tree()
    print(example_tree_4A.avl_to_array())


def test_split():
    # tree with one node
    example_tree_1 = create_tree([1])
    subtree1A, subtree1B = example_tree_1.split(example_tree_1.search(1))
    print("subtree1A:")
    print(subtree1A.avl_to_array())
    print("subtree1B:")
    print(subtree1B.avl_to_array())

    # tree with 2 nodes, split by root.
    example_tree_2 = create_tree([1, 2])
    subtree2A, subtree2B = example_tree_2.split(example_tree_2.search(1))
    print("subtree2A:")
    print(subtree2A.avl_to_array())
    print("subtree2B:")
    print(subtree2B.avl_to_array())

    # tree with 2 nodes, split by leaf
    example_tree_3 = create_tree([1, 2])
    subtree3A, subtree3B = example_tree_3.split(example_tree_3.search(2))
    print("subtree3A:")
    print(subtree3A.avl_to_array())
    print("subtree3B:")
    print(subtree3B.avl_to_array())

    # tree with 3 nodes, split by root
    example_tree_4 = create_tree([2, 1, 3])
    subtree4A, subtree4B = example_tree_4.split(example_tree_4.search(2))
    print("subtree4A:")
    print(subtree4A.avl_to_array())
    print("subtree4B:")
    print(subtree4B.avl_to_array())

    # tree with 3 nodes, split by leaf
    example_tree_5 = create_tree([2, 1, 3])
    subtree5A, subtree5B = example_tree_5.split(example_tree_5.search(1))
    print("subtree5A:")
    print(subtree5A.avl_to_array())
    print("subtree5B:")
    print(subtree5B.avl_to_array())

    # more complex tree
    example_tree_5 = create_tree([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])
    subtree5A, subtree5B = example_tree_5.split(example_tree_5.search(6))
    print("subtree5A:")
    # subtree5A.display_tree()
    print(subtree5A.avl_to_array())
    print("subtree5B:")
    # subtree5B.display_tree()
    print(subtree5B.avl_to_array())


test_split()


