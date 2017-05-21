import Task_1_NearestNeighbour
import Task_2_KelpHart
import Task_2_NearestNeighbour
import Task_2_BranchAndBound
import glob
import random


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


def print_file(filename):
    f = open(filename, "r", encoding='utf-8')
    text = f.read()
    text = text.split("\n")
    for i in range(len(text)):
        print(text[i])
    f.close()


def generate_map_1(number_of_cities):
    distances = get_distances(number_of_cities, 1)
    filename = "Tarefa_1_" + str(number_of_cities) + ".txt"
    f = open(filename, "w", encoding='utf-8')
    string = "start in C0\n"
    counter = 0
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if j > i:
                string += "C" + str(i) + ",C" + str(j) + "," + str(distances[counter]) + "\n"
                counter += 1
    f.write(string)
    f.close()


def generate_map_2(number_of_cities):
    distances = get_distances(number_of_cities, 2)
    filename = "Tarefa_2_" + str(number_of_cities) + ".txt"
    f = open(filename, "w", encoding='utf-8')
    string = "start in C0\n"
    counter = 0
    for i in range(number_of_cities):
        for j in range(number_of_cities):
            if i != j:
                string += "C" + str(i) + ",C" + str(j) + "," + str(distances[counter]) + "\n"
                counter += 1
    f.write(string)
    f.close()


# Creates array of distances
def get_distances(n, task):
    if task == 2:
        range_of_distances = n * n - n
    if task == 1:
        range_of_distances = n * (n - 1) // 2
    distances = []
    for i in range(5, range_of_distances + 10):
        distances.append(i*5)
    random.shuffle(distances)
    return distances


def operate(task, algorithm, option):
    python_file = return_python_file(task, algorithm)

    if option == 1:
        filename = select_map(task)
        if filename:
            graph = getattr(globals()[python_file], 'read_map')(filename)
            getattr(globals()[python_file], 'print_map')(graph)
            see_the_file = input_int(0, 1, "Do you wish to see the file? (1-yes, 0-no): ")
            if see_the_file:
                print_file(filename)
        else:
            print("No map found")

    elif option == 2:
        number_of_cities = input_int(1, 10000, "Please write number of cities: ")
        graph, ignore = getattr(globals()[python_file], 'generate_map')(number_of_cities)
        filename = "Tarefa_" + str(task) + "_" + str(number_of_cities) + ".txt"
        print(filename, "was created")
        see_the_map = input_int(0, 1, "Do you wish to see the graph? (1-yes, 0-no): ")
        if see_the_map:
            getattr(globals()[python_file], 'print_map')(graph)
        see_the_file = input_int(0, 1, "Do you wish to see the file? (1-yes, 0-no): ")
        if see_the_file:
            print_file(filename)

    elif option == 3:
        filename = select_map(task)
        if filename:
            graph = getattr(globals()[python_file], 'read_map')(filename)
            getattr(globals()[python_file], 'find_shortest_path')(graph)
        else:
            print("No map found")

    elif option == 4:
        getattr(globals()[python_file], 'maximum_number_of_cities_in_less_than_30_minutes')()

    else:
        number_of_cities = input_int(1, 10000, "Please write number of cities: ")
        if task == 1:
            generate_map_1(number_of_cities)
        else:
            generate_map_2(number_of_cities)


def return_python_file(task, algorithm):
    if task == 1:
        if algorithm == 1:
            return "Task_1_NearestNeighbour"
    else:
        if algorithm == 1:
            return "Task_2_KelpHart"
        elif algorithm == 2:
            return "Task_2_NearestNeighbour"
        elif algorithm == 3:
            return "Task_2_BranchAndBound"


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
        task = input_int(0, 2, "Select Task:\n"
                               "1 - Task 1\n"
                               "2 - Task 2\n"
                               "0 - Return\n")
        if task != 0:
            algorithm = 0
            if task == 1:
                algorithm = input_int(0, 1, "Select algorithm:\n"
                                            "1 - Nearest Neighbour\n"
                                            "0 - Back\n")
            elif task == 2:
                algorithm = input_int(0, 3, "Select algorithm:\n"
                                            "1 - Kelp Hart\n"
                                            "2 - Nearest Neighbour\n"
                                            "3 - Branch and Bound\n"
                                            "0 - Back\n")
            if algorithm != 0:
                option = input_int(0, 5, "What do you want to do:\n"
                                         "1 - Read Map\n"
                                         "2 - Generate Map\n"
                                         "3 - Print shortest path of a map\n"
                                         "4 - Find maximum number of cities that the program can find the shortest path"
                                         " in less than 30 minutes\n"
                                         "5 - Generate map without generating graph\n"
                                         "0 - Back\n")
                if option != 0:
                    operate(task, algorithm, option)
        else:
            print("Thank you")
            return


if __name__ == '__main__':
    menu()

"""Do you just need an ordered sequence of items? Go for a list.
Do you just need to know whether or not you've already got a particular value, but without ordering (and you don't need
to store duplicates)? Use a set.
Do you need to associate values with keys, so you can look them up efficiently (by key) later on? Use a dictionary."""
