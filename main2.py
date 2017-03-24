from AVL1 import *
from LinkedList import *


# Builds a tree from the values of the file
# Each node is a list of the country, code and its values and the index of the country in the file
# Sorted alphabetically by the name of the country

# Menu
def menu():
    tree, dictionary = get_tree()
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = input_int(1, 5, "Option: ")
        if choice == 1:
            search(tree, dictionary)
        elif choice in [2, 3, 4]:
            country = get_country_values(tree, dictionary)
            if country != 0:
                year = input_int(1960, 2016, "Year: ")
                if choice == 2:
                    to_insert = input_float(0.00, 100.00, "Element: ")
                    if country[2].insert(year, to_insert) != 0:
                        country[2].print_list()
                        refresh_file(country)
                    else:
                        print_errors(5)
                elif choice == 3:
                    to_insert = input_float(0.00, 100.00, "New element: ")
                    if country[2].edit(year, to_insert) != 0:
                        country[2].print_list()
                        refresh_file(country)
                    else:
                        print_errors(6)
                else:
                    if country[2].remove(year) != 0:
                        country[2].print_list()
                        refresh_file(country)
                    else:
                        print_errors(7)
        else:
            return


def search(tree, dictionary):
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
        country_info = get_country_values(tree, dictionary)
        if country_info != 0:
            if option == 1:
                country_info[2].print_list()
            elif option == 2:
                year = input_int(1960, 2016, "Year: ")
                value = country_info[2].get_value_of_year(year)
                if value != -1:
                    print("Value:", value)
                else:
                    print("There's no information about that specific year")
            elif option == 3:
                value = input_float(0.0, 100.0, "Value: ")
                option = greater_smaller_equal(value)
                values = country_info[2].get_years_with_filter(value, option)
                if not values:
                    print("No years found with those specifications")
                else:
                    for v in values:
                        print(v[0], ":", v[1])
    if option in [4, 5]:
        year = input_int(1960, 2016, "Year: ")
        if option == 4:
            values = tree.values_by_year(year)
        else:
            value = input_float(0.0, 100.0, "Value: ")
            option = greater_smaller_equal(value)
            values = tree.values_by_year(year, option, value)
        if not values:
            print("No values found in this year")
        for v in values:
            print(v[0][1:-1], "(", v[1][1:-1], "):", v[3])
    else:
        return


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


def greater_smaller_equal(value):
    print("1 - Greater than", value,
          "\n2 - Smaller than", value,
          "\n3 - Equal to", value)
    return input_int(1, 3, "Option: ")


def get_tree():
    f = open("dados.csv", "r", encoding='utf-8')
    dictionary = {}
    text = f.read()
    text = text.split("\n")
    avl_tree = AVLTree()
    for i in range(1, len(text) - 1):
        raw_country = text[i].split(";")
        country = [raw_country[0], raw_country[1], LinkedList(), i]
        for j in range(2, len(raw_country)):
            if raw_country[-j+1] != "":
                country[2].add([2016 - j + 2, float(raw_country[-j+1][1:-1])])
        avl_tree.insert(country)
        dictionary[country[1][1:-1]] = country[0][1:-1]
    return avl_tree, dictionary


# Menu search
def get_country_values(tree, dictionary):
    country_name = menu_search_by(dictionary)
    # start_time = time.time()
    country_info = tree.search_tree(country_name)
    # print("--- %s seconds ---" % (time.time() - start_time))
    if not country_info:
        print_errors(0)
    return country_info


# Refreshes file after tree is changed
def refresh_file(data):
    text = data[0] + ";" + data[1]
    node = data[2].head
    for i in range(1960, 2017):
        text += ";"
        if node and node.get_data()[0] == i:
            text += '"' + str(node.get_data()[1]) + '"'
            node = node.get_next()
    text += "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    # In data[-1] we have the index of the country in the file
    content[data[-1]] = text
    f = open("dados.csv", "w", encoding='utf-8')
    f.writelines(content)
    f.close()


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


# Main
if __name__ == '__main__':
    menu()
