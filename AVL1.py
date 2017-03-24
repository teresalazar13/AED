#@source: https://github.com/recluze/python-avl-tree/blob/master/simple_avl.py

outputdebug = False 


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

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node is not None:
            if self.node.key == key: 
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
                        self.node.right.delete(replacement.key)
                    
                self.rebalance()
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
                        
            self.rebalance()
        else: 
            return

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
        Find the smallest valued node in RIGHT child
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
                
    # Search tree by the name of the country                
    def search_tree(self, item):
        if not self.node:
            return 0
        if item == self.node.key[0][1:-1]:
            return self.node.key
        elif item < self.node.key[0][1:-1]:
            return self.node.left.search_tree(item)
        else:
            return self.node.right.search_tree(item)
    '''
    def values_by_year(self, year, mode=1, limit=-1,list_of_values=[]):
        if self.node.left.node:
            self.node.left.values_by_year(year,mode,limit,list_of_values)
        info = self.node.key[2].get_values_year(mode,limit,year)
        if info:
            list_of_values+=[[self.node.key[0]]+[self.node.key[1]]+info]
        if self.node.right.node:
            self.node.right.values_by_year(year,mode,limit,list_of_values)
        return list_of_values'''
    
    def values_by_year(self, year, mode=1, limit=-1):
        if self.node is None:
            return []
        inlist = [] 
        l = self.node.left.values_by_year(year, mode, limit)
        for i in l: 
            inlist.append(i)
        info = self.node.key[2].get_values_year(mode, limit, year)
        if info:            
            inlist.append([self.node.key[0]]+[self.node.key[1]]+info)
        l = self.node.right.values_by_year(year, mode, limit)
        for i in l: 
            inlist.append(i)
        return inlist
    
    '''
       # country_or_code: 0 -> country || 1 -> code
       def edit_tree(self, item, year, to_insert):
           if not self.node:
               return 0
           if item == self.node.key[0][1:-1]:
               self.node.key[2].edit_list(year,to_insert)
               return self.node.key
           elif item < self.node.key[0][1:-1]:
               return edit_tree(self.node.left, item, year, to_insert)
           else:
               return edit_tree(self.node.right, item, year, to_insert)
       
       def remove_tree(self, item, year):
           if not self.node:
               return 0
           if item == self.node.key[0][1:-1]:
               self.node.key[2].remove(year)
               return self.node.key
           elif item < self.node.key[0][1:-1]:
               return remove_tree(self.node.left, item, year)
           else:
               return remove_tree(self.node.right, item, year)        
    '''