# Gets values from file
def get_values():
    f = open("dados.csv", "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    list_of_values = []
    for i in range(1, len(text) - 1):
        list_of_values += [text[i].split(";")]
    return list_of_values


# Menu
def menu():
    list_of_values = get_values()
    while True:
        print("CHOOSE:\n"
              "1 - Search\n"
              "2 - Insert\n"
              "3 - Edit\n"
              "4 - Remove\n"
              "5 - Exit\n")
        choice = eval(input("Option: "))
        if choice == 1:
            print("SEARCH BY:\n"
                  "1 - Code\n"
                  "2 - Country\n")
            option = eval(input("Option: "))
            if option == 1:
                code = input("Code: ")
                print(binary_search(list_of_values, code))
            elif option == 2:
                country = input("Country: ")
                print(search_by_country(list_of_values, country))
        elif choice in [2, 3, 4]:
            year = eval(input("Year: "))
            if choice == 2:
                to_insert = input("Element: ")
                insert(list_of_values, to_insert, year)
            elif choice == 3:
                to_insert = input("New Element: ")
                insert(list_of_values, to_insert, year)
            else:
                insert(list_of_values, "", year)
        elif choice == 5:
            return


# Search list_of_values by code
# Divide and conquer, because the codes are in alphabetical order
def binary_search(list_of_values, item):
    if not list_of_values:
        return 0
    middle = len(list_of_values)//2
    if list_of_values[middle][1][1:-1] == item:
        return list_of_values[middle], middle
    if item < list_of_values[middle][1][1:-1]:
        return binary_search(list_of_values[0:middle], item)
    else:
        return binary_search(list_of_values[middle + 1:], item)


# Search list_of_values by country
def search_by_country(list_of_values, country):
    for i in range(len(list_of_values)):
        if list_of_values[i][0][1:-1] == country:
            return list_of_values[i], i
    return 0


# Supports Insert, Edit or Remove
def insert(list_of_values, to_insert, year):
    code = input("Code: ")
    element, index = binary_search(list_of_values, code)
    list_of_values[index][year - 1960 + 2] = to_insert
    refresh_file(list_of_values[index], index)


# Refresh file after list_of_values is changed
def refresh_file(data, index):
    text = ""
    for i in range(len(data) - 1):
        text += str(data[i]) + ";"
    text += data[-1] + "\n"

    f = open("dados.csv", "r", encoding='utf-8')
    content = f.readlines()
    f.close()

    content[index + 1] = text
    f = open("dados.csv", "w", encoding='utf-8')
    f.writelines(content)
    f.close()


# Main
if __name__ == '__main__':
    menu()
