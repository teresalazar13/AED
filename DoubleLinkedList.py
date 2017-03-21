from DoubleNode import DoubleNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add_beginning(self, item):
        temp = DoubleNode(item)
        if (self.head == None):
            self.head = self.tail = temp
        else:
            temp.set_prev(None)
            temp.set_next(self.head)
            self.head.set_prev(temp)
            self.head=temp

    def add_end(self, item):
        if (self.head == None):
            self.head = DoubleNode(item)
            self.tail=self.head
        else:
            current=self.head

            while(current.get_next() != None):
                current = current. get_next()
            current.set_next(DoubleNode(item, None, current))
            self.tail = current.get_next()
        return self

    def get_node(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i=0
        while i<index and currentNode.get_next()!= None:
            currentNode = currentNode.get_next()
            if currentNode == None:
                break
            i=i+1
        return currentNode

    def insert_given_position(self, index, data):
        newNode = DoubleNode(data)
        if self.head == None or index == 0:
            self.add_beginning(data)
        elif index > 0:
            temp = self.get_node(index)
            if temp == None or temp.get_next() == None:
                self.add_end(data)
            else:
                newNode.set_next(temp.get_next())
                newNode.set_prev(temp)
                temp.get_next().set_prev(newNode)
                temp.set_next(newNode)

    def delete_given_position(self, index):
        temp=self.get_node(index)
        if temp is not None:
            print(temp)
            temp.get_prev().set_next(temp.get_next())
            if temp.get_next():
                temp.get_next().set_prev(temp.get_prev())
            temp.set_prev(None)
            temp.set_next(None)
            temp.set_data(None)

    def print_list(self):
        currentNode = self.head
        if currentNode == None:
            return 0
        print(currentNode.get_data())
        while currentNode != None:
            currentNode = currentNode.get_next()
            if currentNode != None:
                print(currentNode.get_data())

    def double_list_length(self):
        currentNode = self.head
        if currentNode == None:
            return 0
        count=1
        currentNode = currentNode.get_next()
        while currentNode != None:
            currentNode = currentNode.get_next()
            count = count + 1
        return count

    def par_length_list(self):
        current = self.head
        while current != None and current.get_next() != None:
            current = current.get_next().get_next()
            if current == None:
                return 1
        return 0

    # Given the country name, finds [country name, acronym, list of values, index in file]
    def find(self, item):
        currentNode = self.head
        while currentNode != None:
            if currentNode.get_data()[0] == item:
                return currentNode.get_data()
            currentNode = currentNode.get_next()
        return
