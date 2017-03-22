from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data()[0], "-", current_node.get_data()[1])
            current_node = current_node.get_next()

    def print_value_of_year(self, year):
        current_node = self.head
        while current_node and current_node.get_data()[0] < year:
            current_node = current_node.get_next()
        if current_node and current_node.get_data()[0] == year:  # If the next node has the year we are searching
            print(year, "-", current_node.get_data()[1])
        else:  # If the next year is bigger, we have to insert the node in the middle
            print("There's no information about that specific year")

    def print_years_with_filter(self, value, relate):
        current_node = self.head
        # <
        if relate == 1:
            while current_node:
                if current_node.get_data()[1] < value:
                    print(current_node.get_data()[0], "-", current_node.get_data()[0])
                current_node = current_node.get_next()
        # >
        elif relate == 2:
            while current_node:
                if current_node.get_data()[1] > value:
                    print(current_node.get_data()[0], "-", current_node.get_data()[0])
                current_node = current_node.get_next()
        # =
        else:
            while current_node:
                if current_node.get_data()[1] == value:
                    print(current_node.get_data()[0])
                current_node = current_node.get_next()

    def remove_list(self, year):
        current_node = self.head
        if not current_node:
            return 0
        while current_node.get_next() and current_node.get_next().get_data()[0] < year:
            current_node = current_node.get_next()
        if current_node.get_next() and current_node.get_next().get_data()[0] == year:
            current_node.set_next(current_node.get_next().get_next())
        else:
            return 0

    # Edits the node and the list remains sorted
    def edit(self, year, value):
        current_node = self.head
        while current_node and current_node.get_data()[0] < year:
            current_node = current_node.get_next()
        if current_node and current_node.get_data()[0] == year:  # If the next node has the year we are searching
            current_node.set_data([year, value])
        else:  # If the next year is bigger, we have to insert the node in the middle
            return 0

    # Insert the node and the list remains sorted
    # Returns 0 if the node with the year already existed
    def insert(self, year, value):
        if self.is_empty():
            self.add([year, value])
            return 1
        node = self.head
        while node.get_next() and node.get_next().get_data()[0] < year:
            node = node.get_next()
        if not node.get_next():  # If the next node does no exist
            node.set_next(Node([year, value]))
        elif node.get_next().get_data()[0] == year:  # If the node with the year already existed, return 0
            return 0
        else:  # Insert the node and the list remains sorted
            temp = Node([year, value])
            temp.set_next(node.get_next())
            node.set_next(temp)

    # Returns string in the format g.e ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"100";;;;;;;;;;"100";;;;;;;;;;"100";;"10";;;;
    def get_country_values_as_string(self):
        text = ""
        current_node = self.head
        for i in range(1960, 2017):
            if current_node and current_node.get_data()[0] == i:
                text += '"' + str(current_node.get_data()[1]) + '";'
                current_node = current_node.get_next()
            else:
                text += ";"
        return text
