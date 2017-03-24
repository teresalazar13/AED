from DoubleLinkedList import DoubleLinkedList
from LinkedList import LinkedList


# TODO - Double linked list - in the search function check if value is closer to the begginning or the end
# Double Linked List. Each node has [Country Name, acronym, linked list with values, index in file]
# Linked list with values. Each node has [year, value]. When there is no info about the year, there's no node
# Gets values from file

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
            search(double_linked_list, dictionary)
        elif choice in [2, 3, 4]:
            country = get_country_values(double_linked_list, dictionary)
            if country != 0:
                year = input_int(1960, 2016, "Year: ")
                if choice == 2:
                    to_insert = input_float(0.00, 100.00, "Element: ")
                    if country[2].insert(year, to_insert) == 0:
                        print_errors(5)
                    else:
                        country[2].print_list()
                        refresh_file(country)
                elif choice == 3:
                    to_insert = input_float(0.00, 100.00, "New element: ")
                    if country[2].edit(year, to_insert) == 0:
                        print_errors(6)
                    else:
                        country[2].print_list()
                        refresh_file(country)
                else:
                    if country[2].remove_list(year) != 0:
                        country[2].print_list()
                        refresh_file(country)
                    else:
                        print_errors(7)
        else:
            return


def search(double_linked_list, dictionary):
    print("Search options:\n"
          "option - (inputs) - description\n"
          "1 - (Code|Country) - Get all values of a country\n"
          "2 - (Code|Country, Year) - Get value of a specific year in a country\n"
          "3 - (Code|Country, Value) - Get years that are >, < or = than a value in a country\n"
          "4 - (Year) - Get values of a year of all countries\n"
          "5 - (Value, Year) - Get all countries that have a value >, < or = in a year\n")
    option = input_int(1, 6, "Option: ")
    if option in [1, 2, 3]:
        country_info = get_country_values(double_linked_list, dictionary)
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
    else:
        year = input_int(1960, 2016, "Year: ")
        if option == 4:
            values = double_linked_list.get_values_of_a_year_of_all_countries(year)
            if not values:
                print("No values found with those specifications")
            else:
                for i in range(len(values)):
                    print(values[i][0], "-", values[i][1])
        else:
            value = input_float(0.0, 100.0, "Value: ")
            option = greater_smaller_equal(value)
            countries = double_linked_list.get_countries_with_filters(value, year, option)
            if not countries:
                print("No countries found with those specifications")
            else:
                for c in countries:
                    print(c)


# Returns the name of a country
def menu_search_by(dictionary):
    while True:
        print("Find by:\n"
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


def get_double_linked_list_from_file():
    f = open("dados.csv", "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    list_of_countries = DoubleLinkedList()
    dictionary = {}
    for i in range(len(text) - 2, 0, -1):
        country = text[i].split(";")
        list_of_values = LinkedList()
        year = 2016
        for j in range(len(country) - 1, 1, -1):
            value = country[j][1:-1]
            if value:
                list_of_values.add(([year, float(value)]))
            year -= 1
        list_of_countries.add_beginning([country[0][1:-1], country[1][1:-1], list_of_values, i])
        dictionary[country[1][1:-1]] = country[0][1:-1]
    return list_of_countries, dictionary


# Returns country_info = [Country Name, acronym, linked list with values, index in file]
def get_country_values(double_linked_list, dictionary):
    country_name = menu_search_by(dictionary)
    country_info = double_linked_list.find(country_name)
    if country_info:
        return country_info
    else:
        print_errors(0)
        return 0


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
    elif error_number == 5:
        print("Could not insert. Value already exists in this year.")
    elif error_number == 6:
        print("Could not edit. Value doesn't exist in this year.")
    elif error_number == 7:
        print("Could not remove. Value doesn't exist in this year.")


# Main
if __name__ == '__main__':
    menu()
