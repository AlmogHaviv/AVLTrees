from AVLTree import AVLTree, AVLNode
def test_do_10000_insertions_and_deletions():
    avl_tree = AVLTree()
    for i in range(10000):
        print(i)
        avl_tree.insert(i, "num" + str(i))

    # Check tree size after insertions

    for i in range(10000):
        print(i)
        avl_tree.delete(avl_tree.get_root())


test_do_10000_insertions_and_deletions()