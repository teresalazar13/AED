from AVL2 import *


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
            year = j + 1958
            if raw_country[j] != "":
                values.insert([year, float(raw_country[j][1:-1])])
        country = raw_country[0:2]
        country.append(values)
        country.append(i)  # add index of country in file
        main_avl_tree.insert(country)
        convert[country[1][1:-1]] = country[0][1:-1]
    return main_avl_tree, convert


# item = country
def search_tree(tree, item):
    if not tree.node:
        return 0
    if item == tree.node.key[0][1:-1]:
        return tree.node.key
    elif item < tree.node.key[0][1:-1]:
        return search_tree(tree.node.left, item)
    else:
        return search_tree(tree.node.right, item)


# item = year
def search_tree_of_values(tree, item):
    if not tree.node:
        return 0
    if item == tree.node.key[0]:
        return tree.node.key[1]
    elif item < tree.node.key[0]:
        return search_tree_of_values(tree.node.left, item)
    else:
        return search_tree_of_values(tree.node.right, item)


# item = [year, value]
def edit_tree(tree, item):
    if not tree.node:
        tree.insert(item)  # if item is not in tree, insert item
        return 1
    if item[0] == tree.node.key[0]:
        tree.node.key[1] = item[1]
        return tree.node.key
    elif item[0] < tree.node.key[0]:
        return edit_tree(tree.node.left, item)
    else:
        return edit_tree(tree.node.right, item)


# Refreshes file after tree of trees is changed
def refresh_file(item):
    data = [""] * (2016 - 1960 + 1)
    # TO DO -> improve this function
    for i in range(1960, 2017):
        value = search_tree_of_values(item[2], i)
        if value != 0:
            cena = '"' + str(value) + '"'
            print(i, cena)
            data[i - 1960] = '"' + str(value) + '"'
    text = item[0] + ";" + item[1]
    for i in range(len(data) - 1):
        text += str(data[i]) + ";"
    text += str(data[-1]) + "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    # In data[-1] we have the index of the country in the file
    content[item[-1]] = text
    f = open("dados.csv", "w", encoding='utf-8')
    f.writelines(content)
    f.close()


def print_errors(error_number, min=0, max=0):
    if error_number == 0:
        print("Country does not exist")
    elif error_number == 1:
        print("Please insert an int")
    elif error_number == 2:
        print("Can only operate between", min, "and", max)
    elif error_number == 3:
        print("Value not valid")
    elif error_number == 4:
        print("Please insert a float")


# Menu search
def menu_search(dictionary, tree_of_trees):
    country = menu_search_by(dictionary)
    # start_time = time.time()
    item = search_tree(tree_of_trees, country)
    # print("--- %s seconds ---" % (time.time() - start_time))
    if country != 0:
        print(item[0][1:-1], "(", item[1][1:-1], ")")
        item[2].print_values()
    else:
        print_errors(0)


# Menu search by
def menu_search_by(dictionary):
    while True:
        print("SEARCH BY:\n"
              "1 - Code\n"
              "2 - Country\n")
        option = input_int(1, 2, "Option: ")
        if option == 1:
            code = input("Code: ")
            try:
                country = dictionary[code]
                return country
            except KeyError:
                print_errors(0)
        elif option == 2:
            country = input("Country: ")
            return country


def input_int(min, max, string):
    while True:
        try:
            item = int(input(string))
            if min > item or item > max:
                print_errors(2, min, max)
            else:
                return item
        except ValueError:
            print_errors(1)


def input_float(min, max, string):
    while True:
        try:
            item = float(input(string))
            if min > item or item > max:
                print_errors(3, min, max)
            else:
                return item
        except ValueError:
            print_errors(4)


# Menu
def menu():
    tree_of_trees, dictionary = get_trees()
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = input_int(1, 5, "Option: ")
        if choice == 1:
            menu_search(dictionary, tree_of_trees)
        elif choice in [2, 3, 4]:
            country = menu_search_by(dictionary)
            node = search_tree(tree_of_trees, country)
            year = input_int(1960, 2016, "Year: ")
            if choice == 2:
                to_insert = input_float(0.00, 100.00, "Element: ")
                country = edit_tree(node[2], [year, to_insert])
            elif choice == 3:
                to_insert = input_float(0.00, 100.00, "New element: ")
                country = edit_tree(node[2], [year, to_insert])
            else:
                if node != 0:
                    node[2].delete(year)
            if country != 0:
                refresh_file(node)
            else:
                print_errors(0)
        elif choice == 5:
            return
        print()


if __name__ == '__main__':
    menu()
