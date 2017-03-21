import time
from DoubleLinkedList import DoubleLinkedList
from LinkedList import LinkedList


# Double Linked List. Each node has [Country Name, acronym, linked list with values, index in file]
# Gets values from file
def get_double_linked_list_from_file():
    f = open("dados.csv", "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    list_of_countries = DoubleLinkedList()
    dictionary = {}
    for i in range(len(text) - 2, 0, -1):
        country = text[i].split(";")
        list_of_values = LinkedList()
        for j in range(len(country) - 1, 1, -1):
            value = country[j][1:-1]
            if value:
                list_of_values.add(float(value))
            else:
                list_of_values.add("")
        list_of_countries.add_beginning([country[0][1:-1], country[1][1:-1], list_of_values, i])
        dictionary[country[1][1:-1]] = country[0][1:-1]
    return list_of_countries, dictionary


# Menu
def menu():
    double_linked_list, dictionary = get_double_linked_list_from_file()
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = input_int(1, 5, "Option: ")
        if choice == 1:
            menu_search(double_linked_list, dictionary)
        elif choice in [2, 3, 4]:
            year = input_int(1960, 2016, "Year: ")
            if choice == 2:
                to_insert = input_float(0.00, 100.00, "Element: ")
                edit_country(double_linked_list, to_insert, year, dictionary)
            elif choice == 3:
                to_insert = input_float(0.00, 100.00, "New element: ")
                edit_country(double_linked_list, to_insert, year, dictionary)
            else:
                edit_country(double_linked_list, "", year, dictionary)
        elif choice == 5:
            return


# Menu search
def menu_search(double_linked_list, dictionary):
    country_name = menu_search_by(dictionary)
    country_info = double_linked_list.find(country_name)
    if country_info:
        country_info[2].print_list()
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


# Supports Insert, Edit or Remove
# Searches through double linked list to get country -> [country name, acronym, list of values, index in file]
def edit_country(double_linked_list, value_to_insert, year, dictionary):
    country_name = menu_search_by(dictionary)
    country_info = double_linked_list.find(country_name)
    if country_info:
        country_info[2].edit(year, value_to_insert)
        refresh_file(country_info)
    else:
        print_errors(0)


# Refresh file given [country name, acronym, list of values, index in file]
def refresh_file(country_info):
    text = '"' + country_info[0] + '";"' + country_info[1] + '";'
    text += country_info[2].get_country_values_as_string()[:-1] + "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    content[country_info[-1]] = text
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


# Main
if __name__ == '__main__':
    menu()
