from avl_template_new import AVLTree
import random


def main():
    for i in range(1, 11):
        exp = 1000*(2**i)
        exp_avl1, exp_avl2 = build_avl(exp)
        random_num = random.randint(1, exp)
        x = exp_avl1.search(random_num)
        print()
        print("----------part 1----------")
        print()
        print(i)
        exp_avl1.split(x)
        print()
        print("----------part 2----------")
        print()
        max_x = exp_avl2.max(exp_avl2.root.left)
        print(i)
        exp_avl2.split(max_x)


def build_avl(i):
    new_tree = AVLTree()
    new_tree2 = AVLTree()

    # Generate a list of numbers from 1 to i
    numbers = list(range(1, i + 1))

    # Shuffle the list of numbers randomly
    random.shuffle(numbers)

    # Insert each number into the AVL tree
    for num in numbers:
        new_tree.insert(num, num)
        new_tree2.insert(num, num)
    return new_tree, new_tree2


if __name__ == '__main__':
    main()
