#@source: https://github.com/recluze/python-avl-tree/blob/master/simple_avl.py
# Some changes made
outputdebug = False 


def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return 2
    else:
        return 3


def debug(msg):
    if outputdebug:
        print(msg)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 


class AVLTree:
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return self.height == 0
        
    def rebalance(self):
        """
        Rebalance a particular (sub)tree
        """
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()
            
    def rrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' right')
        a = self.node
        b = self.node.left.node
        t = b.right.node
        
        self.node = b
        b.right.node = a
        a.left.node = t

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' left')
        a = self.node
        b = self.node.right.node
        t = b.left.node
        
        self.node = b
        b.left.node = a
        a.right.node = t

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse: 
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse: 
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0

    def logical_predecessor(self, node):
        """
        Find the biggest valued node in LEFT child
        """
        node = node.left.node 
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        """
        Find the smallese valued node in RIGHT child
        """
        node = node.right.node  
        if node is not None:  # just a sanity check
            
            while node.left is not None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node is None:
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self is None or self.node is None:
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()
        
    def inorder_traverse(self):
        if self.node is None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):
        """
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        """
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if self.node is not None:
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.left is not None:
                self.node.right.display(level + 1, '>')

    # Inserts element in tree
    def insert(self, key):
        tree = self.node
        new_node = Node(key)
        if tree is None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        elif key[0] < tree.key[0]:
            self.node.left.insert(key)
        elif key[0] > tree.key[0]:
            self.node.right.insert(key)
        else:
            debug("Key [" + str(key) + "] already in tree.")
        self.rebalance()

    # Deletes year and value in tree. If the node does not exist informs user
    def delete(self, key):
        if self.node is not None:
            if self.node.key[0] == key:
                debug("Deleting ... " + str(key))
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement is not None:  # sanity check
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key
                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key[0])
                self.print_values()
                self.rebalance()
                return
            elif key < self.node.key[0]:
                self.node.left.delete(key)
            elif key > self.node.key[0]:
                self.node.right.delete(key)
            self.rebalance()
        else:
            print("Could not remove. Value doesn't exist in this year.")
            return 0

    # Print years and values of a country
    def print_values(self):
        if not self.node:
            return
        if self.node.left:
            self.node.left.print_values()
        print(self.node.key[0], "-", self.node.key[1])
        if self.node.right:
            self.node.right.print_values()

    # Search tree of countries by the name of the country
    # item = country
    def search_tree(self, item):
        if not self.node:
            return 0
        if item == self.node.key[0][1:-1]:
            return self.node.key
        elif item < self.node.key[0][1:-1]:
            return self.node.left.search_tree(item)
        else:
            return self.node.right.search_tree(item)

    # Search tree of values by the year
    # item = year
    def search_tree_of_values(self, item):
        if not self.node:
            return 0
        if item == self.node.key[0]:
            return self.node.key[1]
        elif item < self.node.key[0]:
            return self.node.left.search_tree_of_values(item)
        else:
            return self.node.right.search_tree_of_values(item)

    # Insert year, value
    # item = [year, value]
    def insert_tree(self, item):
        if not self.node:
            self.insert(item)  # if item is not in tree, insert item
            return 1
        if item[0] == self.node.key[0]:
            return 0  # if item is in tree, print error
        elif item[0] < self.node.key[0]:
            return self.node.left.insert_tree(item)
        else:
            return self.node.right.insert_tree(item)

    # Edit year, value
    # item = [year, value]
    def edit_tree(self, item):
        if not self.node:
            return 0  # if item is not in tree, print error
        if item[0] == self.node.key[0]:
            self.node.key[1] = item[1]  # if item is in tree, edit it
            return 1
        elif item[0] < self.node.key[0]:
            return self.node.left.edit_tree(item)
        else:
            return self.node.right.edit_tree(item)

    # Get years that are >,< or = than a value in a country
    def get_years_with_filter(self, value, option, list_of_years_and_values):
        if not self.node:
            return list_of_years_and_values
        if compare(self.node.key[1], value) == option:
            list_of_years_and_values.append(self.node.key)
        left = self.node.left.get_years_with_filter(value, option, list_of_years_and_values)
        right = self.node.right.get_years_with_filter(value, option, list_of_years_and_values)
        return left and right

    # Get values of a year of all countries
    def get_values_by_year(self, year, values):
        if not self.node:
            return values
        value = self.node.key[2].search_tree_of_values(year)
        if value != 0:
            values.append([self.node.key[0], self.node.key[2].search_tree_of_values(year)])
        left = self.node.left.get_values_by_year(year, values)
        right = self.node.right.get_values_by_year(year, values)
        return left and right

    # Get all countries that have a value >, < or = in a year
    def get_countries_with_filter(self, year, option, value_to_compare, values):
        if not self.node:
            return values
        value = self.node.key[2].search_tree_of_values(year)
        if value != 0 and compare(value, value_to_compare) == option:
            values.append([self.node.key[0], self.node.key[2].search_tree_of_values(year)])
        left = self.node.left.get_countries_with_filter(year, option, value_to_compare, values)
        right = self.node.right.get_countries_with_filter(year, option, value_to_compare, values)
        return left and right
