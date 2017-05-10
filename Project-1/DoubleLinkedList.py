from DoubleNode import DoubleNode


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_beginning(self, item):
        temp = DoubleNode(item)
        if self.head is None:
            self.head = self.tail = temp
        else:
            temp.set_prev(None)
            temp.set_next(self.head)
            self.head.set_prev(temp)
            self.head = temp

    def add_end(self, item):
        if self.head is None:
            self.head = DoubleNode(item)
            self.tail = self.head
        else:
            current = self.head
            while current.get_next() is not None:
                current = current. get_next()
            current.set_next(DoubleNode(item, None, current))
            self.tail = current.get_next()
        return self

    def get_node(self, index):
        current_node = self.head
        if current_node is None:
            return None
        i = 0
        while i < index and current_node.get_next() is not None:
            current_node = current_node.get_next()
            if current_node is None:
                break
            i += 1
        return current_node

    def insert_given_position(self, index, data):
        new_node = DoubleNode(data)
        if self.head is None or index == 0:
            self.add_beginning(data)
        elif index > 0:
            temp = self.get_node(index)
            if temp is None or temp.get_next() is None:
                self.add_end(data)
            else:
                new_node.set_next(temp.get_next())
                new_node.set_prev(temp)
                temp.get_next().set_prev(new_node)
                temp.set_next(new_node)

    def delete_given_position(self, index):
        temp = self.get_node(index)
        if temp is not None:
            print(temp)
            temp.get_prev().set_next(temp.get_next())
            if temp.get_next():
                temp.get_next().set_prev(temp.get_prev())
            temp.set_prev(None)
            temp.set_next(None)
            temp.set_data(None)

    def print_list(self):
        current_node = self.head
        if current_node is None:
            return 0
        print(current_node.get_data())
        while current_node is not None:
            current_node = current_node.get_next()
            if current_node is not None:
                print(current_node.get_data())

    def double_list_length(self):
        current_node = self.head
        if current_node is None:
            return 0
        count = 1
        current_node = current_node.get_next()
        while current_node is not None:
            current_node = current_node.get_next()
            count += 1
        return count

    def par_length_list(self):
        current = self.head
        while current is not None and current.get_next() is not None:
            current = current.get_next().get_next()
            if current is None:
                return 1
        return 0

    # Given the code, starts to search from the beginning or the end
    def find(self, code):
        if code < "M":
            return self.find_beg(code)
        else:
            return self.find_backwards(code)

    # Given the code name, finds [country name, acronym, list of values, index in file]. Starts in the beginning
    # of the list
    def find_beg(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.get_data()[1] == item:
                return current_node.get_data()
            current_node = current_node.get_next()
        return

    # Given the code name, finds [country name, acronym, list of values, index in file]. Starts in the end
    # of the list
    def find_backwards(self, item):
        current_node = self.tail
        while current_node is not None:
            if current_node.get_data()[1] == item:
                return current_node.get_data()
            current_node = current_node.get_prev()
        return

    def get_values_of_a_year_of_all_countries(self, year):
        list_of_values = []
        current_node = self.head
        while current_node is not None:
            value = current_node.get_data()[2].get_value_of_year(year)
            if value != -1:
                list_of_values.append([current_node.get_data()[0], value])
            current_node = current_node.get_next()
        return list_of_values

    def get_countries_with_filters(self, value, year, relate):
        list_of_values = []
        current_node = self.head
        if relate == 1:
            while current_node is not None:
                value_node = current_node.get_data()[2].get_value_of_year(year)
                if value_node > value:
                    list_of_values.append(current_node.get_data()[0])
                current_node = current_node.get_next()
            return list_of_values
        elif relate == 2:
            while current_node is not None:
                value_node = current_node.get_data()[2].get_value_of_year(year)
                if value_node < value:
                    list_of_values.append(current_node.get_data()[0])
                current_node = current_node.get_next()
            return list_of_values
        else:
            while current_node is not None:
                value_node = current_node.get_data()[2].get_value_of_year(year)
                if value_node == value:
                    list_of_values.append(current_node.get_data()[0])
                current_node = current_node.get_next()
            return list_of_values
