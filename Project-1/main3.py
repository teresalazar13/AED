from AVL2 import *
import time


# AVL Tree of countries. Each node has a list: [Country, Code, AVL Tree of values, index in file]
# Main AVL Tree sorted alphabetically
# In the AVL Tree of values, each node is a list: [year, value of year]
# AVL Tree of Values sorted by year

# Menu
def menu():
    # start_time = time.time()
    tree_of_trees, dictionary = get_trees()
    # print("--- %s seconds ---" % (time.time() - start_time))
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = input_int(1, 5, "Option: ")
        if choice == 1:
            search(dictionary, tree_of_trees)
        elif choice in [2, 3, 4]:
            node = get_country_values(tree_of_trees, dictionary)
            if node != 0:
                year = input_int(1960, 2016, "Year: ")
                if choice == 2:
                    to_insert = input_float(0.00, 100.00, "Element: ")
                    # start_time = time.time()
                    operation = node[2].insert_tree([year, to_insert])
                    # print("--- %s seconds ---" % (time.time() - start_time))
                    if operation == 0:
                        print_errors(5)
                    else:
                        node[2].print_values()
                        refresh_file(node)
                elif choice == 3:
                    to_insert = input_float(0.00, 100.00, "New element: ")
                    start_time = time.time()
                    operation = node[2].edit_tree([year, to_insert])
                    print("--- %s seconds ---" % (time.time() - start_time))
                    if operation == 0:
                        print_errors(6)
                    else:
                        node[2].print_values()
                        refresh_file(node)
                else:
                    # The method delete checks if element is in tree. We print the values anyway
                    start_time = time.time()
                    node[2].delete(year)
                    print("--- %s seconds ---" % (time.time() - start_time))
                    node[2].print_values()
                    refresh_file(node)
        else:
            return


# Menu search
def search(dictionary, tree_of_trees):
    print("Search options:\n"
          "option - (inputs) - description\n"
          "1 - (Code|Country) - Get all values of a country\n"
          "2 - (Code|Country, Year) - Get value of a specific year in a country\n"
          "3 - (Code|Country, Value) - Get years that are >,< or = than a value in a country\n"
          "4 - (Year) - Get values of a year of all countries\n"
          "5 - (Value, Year) - Get all countries that have a value >, < or = in a year\n"
          "6 - Back")
    option = input_int(1, 6, "Option: ")
    if option in [1, 2, 3]:
        country_info = get_country_values(tree_of_trees, dictionary)
        if country_info != 0:
            if option == 1:
                country_info[2].print_values()
            elif option == 2:
                year = input_int(1960, 2016, "Year: ")
                # start_time = time.time()
                value = country_info[2].search_tree_of_values(year)
                # print("--- %s seconds ---" % (time.time() - start_time))
                if value != 0:
                    print("Value:", value)
                else:
                    print("There's no information about that specific year")
            elif option == 3:
                value = input_float(0.0, 100.0, "Value: ")
                option = greater_smaller_equal(value)
                # start_time = time.time()
                values = country_info[2].get_years_with_filter(value, option, [])
                # print("--- %s seconds ---" % (time.time() - start_time))
                if not values:
                    print("No years found with those specifications")
                else:
                    for v in values:
                        print(v[0], ":", v[1])
    elif option in [4, 5]:
        year = input_int(1960, 2016, "Year: ")
        if option == 4:
            # start_time = time.time()
            values = tree_of_trees.get_values_by_year(year, [])
            # print("--- %s seconds ---" % (time.time() - start_time))
        else:
            value = input_float(0.0, 100.0, "Value: ")
            option = greater_smaller_equal(value)
            # start_time = time.time()
            values = tree_of_trees.get_countries_with_filter(year, option, value, [])
            # print("--- %s seconds ---" % (time.time() - start_time))
        if not values:
            print("No values found in this year")
        for v in values:
            print(v[0][1:-1], "-", v[1])
    else:
        return


# Returns the code of a country
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


# Menu greater, smaller or equal
def greater_smaller_equal(value):
    print("1 - Greater than", value,
          "\n2 - Smaller than", value,
          "\n3 - Equal to", value)
    return input_int(1, 3, "Option: ")


# Returns country_info = [Country Name, acronym, AVL tree of values, index in file]
def get_country_values(tree_of_trees, dictionary):
    country_name = menu_search_by(dictionary)
    start_time = time.time()
    country_info = tree_of_trees.search_tree(country_name)  # Node in Main AVL Tree
    print("--- %s seconds ---" % (time.time() - start_time))
    if country_info:
        return country_info
    else:
        print_errors(0)
        return 0


# Reads file and stores data in tree of trees
def get_trees():
    f = open("dados.csv", "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    main_avl_tree = AVLTree()  # Create the main AVL Tree
    convert = {}  # Create dictionary to convert Codes into Countries
    for i in range(1, len(text) - 1):
        raw_country = text[i].split(";")
        values = AVLTree()  # Create an AVL Tree for each country
        for j in range(2, len(raw_country)):
            year = j + 1958
            if raw_country[j] != "":
                values.insert([year, float(raw_country[j][1:-1])])
        country = [raw_country[0], raw_country[1], values, i]
        main_avl_tree.insert(country)
        convert[country[1][1:-1]] = country[0][1:-1]
    return main_avl_tree, convert


# Updates file given [country name, acronym, list of values, index in file], after tree of trees is changed
def refresh_file(item):
    data = [""] * (2016 - 1960 + 1)
    for i in range(1960, 2017):
        value = item[2].search_tree_of_values(i)
        if value != 0:
            data[i - 1960] = '"' + str(value) + '"'
    text = item[0] + ";" + item[1] + ";"

    for i in range(len(data) - 1):
        text += str(data[i]) + ";"
    text += str(data[-1]) + "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    # In item[-1] we have the index of the country in the file
    content[item[-1]] = text
    f = open("dados.csv", "w", encoding='utf-8')
    f.writelines(content)
    f.close()


# Protection for int inputs
def input_int(min_value, max_value, string):
    while True:
        try:
            item = int(input(string))
            if min_value > item or item > max_value:
                print_errors(2, min_value, max_value)
            else:
                return item
        except ValueError:
            print_errors(1)


# Protection for float inputs
def input_float(min_value, max_value, string):
    while True:
        try:
            item = float(input(string))
            if min_value > item or item > max_value:
                print_errors(3, min_value, max_value)
            else:
                return item
        except ValueError:
            print_errors(4)


# Given the error iD (optional: min_value and max_value), prints an error
def print_errors(error_number, min_value=0, max_value=0):
    if error_number == 0:
        print("Country does not exist")
    elif error_number == 1:
        print("Please insert an int")
    elif error_number == 2:
        print("Can only operate between", min_value, "and", max_value)
    elif error_number == 3:
        print("Value not valid")
    elif error_number == 4:
        print("Please insert a float")
    elif error_number == 5:
        print("Could not insert. Value already exists in this year.")
    elif error_number == 6:
        print("Could not edit. Value doesn't exist in this year.")
    elif error_number == 7:
        print("Could not remove. Value doesn't exist in this year.")


if __name__ == '__main__':
    menu()
