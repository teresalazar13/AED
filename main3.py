from AVL import *


def get_trees():
    f = open("dados.csv", "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    main_avl_tree = AVLTree()
    convert = {}
    for i in range(1, len(text) - 1):
        raw_country = text[i].split(";")
        values = AVLTree()
        for j in range(2, len(raw_country)):
            year = j + 1960
            if raw_country[j] != "":
                values.insert([year, float(raw_country[j][1:-1])])
        country = raw_country[0:2]
        country.append(values)
        main_avl_tree.insert(country)
        convert[country[1][1:-1]] = country[0][1:-1]
    return main_avl_tree, convert


def search_tree(tree, item):
    if not tree.node:
        return 0
    if item == tree.node.key[0][1:-1]:
        return tree.node.key[2]
    elif item < tree.node.key[0][1:-1]:
        return search_tree(tree.node.left, item)
    else:
        return search_tree(tree.node.right, item)


# item = [year, value]
def edit_tree(tree, item):
    if not tree.node:
        return 0
    if item[0] == tree.node.key[0]:
        tree.node.key[1] = item[1]
        return tree.node.key
    elif item[0] < tree.node.key[0]:
        return edit_tree(tree.node.left, item)
    else:
        return edit_tree(tree.node.right, item)


def remove_item(tree, item):
    if not tree.node:
        return 0
    if item[0] == tree.node.key[0]:
        tree.delete(item[0])
        return 1
    elif item[0] < tree.node.key[0]:
        return edit_tree(tree.node.left, item)
    else:
        return edit_tree(tree.node.right, item)

if __name__ == '__main__':
    tree_of_trees, convert = get_trees()
    # country = convert["PRT"]
    # search_tree(tree_of_trees, country).display()

    # INSERT
    tree_of_values = search_tree(tree_of_trees, "Portugal")
    if tree_of_values != 0:
        edit_tree(tree_of_values, [2012, 100.0])
        tree_of_values.display()

    # REMOVE
    tree_of_values = search_tree(tree_of_trees, "Portugal")
    if tree_of_values != 0:
        tree_of_values.delete(2012)
        tree_of_values.display()
