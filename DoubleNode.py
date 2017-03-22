class DoubleNode:
    def __init__(self, init_data=None, next=None, prev=None):
        self.data = init_data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def has_next(self):
        return self.next is not None

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev is not None
