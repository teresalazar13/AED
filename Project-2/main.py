import Task_1_NearestNeighbour
import Task_2_KelpHart
import Task_2_NearestNeighbour
import glob, os


# Protection for int inputs
def input_int(min_value, max_value, string):
    while True:
        try:
            item = int(input(string))
            if min_value > item or item > max_value:
                print_errors(0, min_value, max_value)
            else:
                return item
        except ValueError:
            print_errors(0, min_value, max_value)


# Given the error iD (optional: min_value and max_value), prints an error
def print_errors(error_number, min_value=0, max_value=0):
    if error_number == 0:
        print("Please insert a number in the range[", min_value, ",", max_value, "]")


def operate(task, algorithm, option):
    python_file = return_python_file(task, algorithm)
    if option == 1:
        filename = select_map(task)
        if filename:
            Task_2_KelpHart.read_map(filename)
            # getattr(python_file, read_map)(*args, **filename)
        else:
            print("No map found.")
    elif option == 2:
        number_of_cities = input_int(1, 10000, "Please write number of cities: ")
        Task_2_KelpHart.generate_map(number_of_cities)
    elif option == 3:
        filename = select_map(task)
        graph = Task_1_NearestNeighbour.read_map(filename)
        Task_2_KelpHart.find_shortest_path(graph)
    else:
        Task_2_KelpHart.maximum_number_of_cities_in_less_than_30_minutes()


def return_python_file(task, algorithm):
    if task == 1:
        if algorithm == 1:
            return "Task_1_NearestNeighbour"
    else:
        if algorithm == 1:
            return "Task_2_KelpHart"
        elif algorithm == 2:
            return "Task_2_NearestNeighbour"


def select_map(task):
    counter = 1
    files = []
    for file in glob.glob("*.txt"):
        if int(file[7]) == task:
            files.append(file)
            print(counter, "-", file)
            counter += 1
    if files:
        filename = files[input_int(1, counter, "Select Map: ") - 1]
        return filename
    return None


def menu():
    while True:
        task = input_int(1, 2, "Which Task do you want to check? ")
        if task == 1:
            algorithm = input_int(1, 1, "Select algorithm:\n"
                                        "1 - Nearest Neighbour\n")
        elif task == 2:
            algorithm = input_int(1, 2, "Select algorithm:\n"
                                        "1 - Kelp Hart\n"
                                        "2 - Nearest Neighbour\n")
        option = input_int(1, 4, "What do you wanto to do:\n"
                               "1 - Read Map\n"
                               "2 - Generate Map\n"
                               "3 - Print shortest path of a map\n"
                               "4 - Find maximum number of cities that the program can find the shortest path in less "
                               "than 30 minutes\n")
        operate(task, algorithm, option)


if __name__ == '__main__':
    menu()
