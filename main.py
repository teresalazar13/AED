import time

# Gets values from file
def get_values():
    f = open("dados.csv", "r", encoding='utf-8')
    dictionary = {}
    text = f.read()
    text = text.split("\n")
    list_of_values = []
    for i in range(1, len(text) - 1):
        country = text[i].split(";")
        list_of_values += [country]
        dictionary[country[0][1:-1]] = country[1][1:-1]
    return list_of_values, dictionary


# Menu search
def menu_search(dictionary, list_of_values):
    code = menu_search_by(dictionary)
    # start_time = time.time()
    country, index = binary_search(list_of_values, code)
    # print("--- %s seconds ---" % (time.time() - start_time))
    if country != 0:
        print_values(country)
    else:
        print_errors(0)


# Menu search by
def menu_search_by(dictionary):
    while True:
        print("SEARCH BY:\n"
              "1 - Code\n"
              "2 - Country\n")
        option = input_int(1, 2, "Option: ")
        code = ""
        if option == 1:
            code = input("Code: ")
            return code
        elif option == 2:
            country = input("Country: ")
            try:
                code = dictionary[country]
                return code
            except KeyError:
                print_errors(0)


# Menu
def menu():
    list_of_values, dictionary = get_values()
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = input_int(1, 5, "Option: ")
        if choice == 1:
            menu_search(dictionary, list_of_values)
        elif choice in [2, 3, 4]:
            year = input_int(1960, 2016, "Year: ")
            if choice == 2:
                to_insert = input_float(0.00, 100.00, "Element: ")
                insert(list_of_values, '"' + str(to_insert) + '"', year, dictionary)
            elif choice == 3:
                to_insert = input_float(0.00, 100.00, "New element: ")
                insert(list_of_values, '"' + str(to_insert) + '"', year, dictionary)
            else:
                insert(list_of_values, "", year, dictionary)
        elif choice == 5:
            return
        print()


# Search list_of_values by code
# Divide and conquer, because the codes are in alphabetical order
def binary_search(list_of_values, item):
    if not list_of_values:
        return 0, 0
    middle = len(list_of_values) // 2
    if list_of_values[middle][1][1:-1] == item:
        return list_of_values[middle], middle
    if item < list_of_values[middle][1][1:-1]:
        return binary_search(list_of_values[0:middle], item)
    else:
        return binary_search(list_of_values[middle + 1:], item)


# Supports Insert, Edit or Remove
def insert(list_of_values, to_insert, year, dictionary):
    code = menu_search_by(dictionary)
    # start_time = time.time()
    element, index = binary_search(list_of_values, code)
    # print("--- %s seconds ---" % (time.time() - start_time))
    list_of_values[index][year - 1960 + 2] = to_insert
    refresh_file(list_of_values[index], index)


# Refresh file after list_of_values is changed
def refresh_file(data, index):
    text = ""
    for i in range(len(data) - 1):
        text += str(data[i]) + ";"
    text += str(data[-1]) + "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    content[index + 1] = text
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
