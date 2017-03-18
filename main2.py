from AVL1 import *


# Builds a tree from the values of the file
# Each node is a list of the country, code and its values and the index of the country in the file
# Sorted alphabetically by the name of the country
def get_trees():
    f = open("dados.csv", "r", encoding='utf-8')
    dictionary = {}
    text = f.read()
    text = text.split("\n")
    avl_tree = AVLTree()
    for i in range(1, len(text) - 1):
        country = text[i].split(";")
        country.append(i)
        avl_tree.insert(country)
        dictionary[country[1][1:-1]] = country[0][1:-1]
    return avl_tree, dictionary


# Menu search
def menu_search(dictionary, tree):
    country = menu_search_by(dictionary)
    # start_time = time.time()
    country = search_tree(tree, country)
    # print("--- %s seconds ---" % (time.time() - start_time))
    if country != 0:
        print_values(country[:-1])
    else:
        print_errors(0)


# Menu search by
def menu_search_by(dictionary):
    while True:
        print("SEARCH BY:\n"
              "1 - Code\n"
              "2 - Country\n")
        option = input_int(1, 2, "Option: ")
        country = ""
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


# Menu
def menu():
    tree, dictionary = get_trees()
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = input_int(1, 5, "Option: ")
        if choice == 1:
            menu_search(dictionary, tree)
        elif choice in [2, 3, 4]:
            country = menu_search_by(dictionary)
            year = input_int(1960, 2016, "Year: ")
            if choice == 2:
                to_insert = input_float(0.00, 100.00, "Element: ")
                country = edit_tree(tree, country, year, '"' + str(to_insert) + '"')
            elif choice == 3:
                to_insert = input_float(0.00, 100.00, "New element: ")
                country = edit_tree(tree, country, year, '"' + str(to_insert) + '"')
            else:
                country = edit_tree(tree, country, year, "")
            refresh_file(country)
        elif choice == 5:
            return
        print()


# Search tree by the name of the country
def search_tree(tree, item):
    if not tree.node:
        return 0
    if item == tree.node.key[0][1:-1]:
        return tree.node.key
    elif item < tree.node.key[0][1:-1]:
        return search_tree(tree.node.left, item)
    else:
        return search_tree(tree.node.right, item)


# Supports Insert, Edit or Remove
# country_or_code: 0 -> country || 1 -> code
def edit_tree(tree, item, year, to_insert):
    if not tree.node:
        return 0
    if item == tree.node.key[0][1:-1]:
        tree.node.key[year - 1960 + 2] = to_insert
        return tree.node.key
    elif item < tree.node.key[0][1:-1]:
        return edit_tree(tree.node.left, item, year, to_insert)
    else:
        return edit_tree(tree.node.right, item, year, to_insert)


# Refreshes file after tree is changed
def refresh_file(data):
    text = ""
    for i in range(len(data) - 2):
        text += str(data[i]) + ";"
    text += str(data[-2]) + "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    # In data[-1] we have the index of the country in the file
    content[data[-1]] = text
    f = open("dados.csv", "w", encoding='utf-8')
    f.writelines(content)
    f.close()


def print_values(country_list):
    print(country_list[0][1:-1], "(", country_list[1][1:-1], ")")
    for i in range(2, len(country_list)):
        if country_list[i] != "":
            print(i + 1960, ":", country_list[i][1:-1])


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


# Main
if __name__ == '__main__':
    menu()
