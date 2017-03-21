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

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_list(self):
        current_node = self.head
        i = 0
        while current_node is not None:
            if current_node.get_data() != "":
                print(i + 1960, "-", current_node.get_data())
            current_node = current_node.get_next()
            i += 1

    # Given the year, changes the value
    def edit(self, year, value_to_insert):
        current_node = self.head
        i = 0
        while current_node is not None:
            if i + 1960 == year:
                current_node.set_data(value_to_insert)
                return 1
            current_node = current_node.get_next()
            i += 1
        return 0

    # Returns string in the format g.e ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"100";;;;;;;;;;"100";;;;;;;;;;"100";;"10";;;;
    def get_country_values_as_string(self):
        text = ""
        current_node = self.head
        while current_node is not None:
            if current_node.get_data():
                text += '"' + str(current_node.get_data()) + '";'
            else:
                text += ";"
            current_node = current_node.get_next()
        return text
