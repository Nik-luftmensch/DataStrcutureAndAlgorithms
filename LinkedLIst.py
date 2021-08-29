class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
            
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            
    def push_back(self,new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
            
    def peek_front(self): # returns first element
        if self.head == None: # checks whether list is empty or not
            print("List is empty")
        else:
            return self.head.data

  
    def peek_back(self): # returns last element
        if self.tail == None: # checks whether list is empty or not
            print("List is empty")
        else:
            return self.tail.data
        
    def pop_front(self):
        if self.head == None: # checks whether list is empty or not
            print("List is empty")
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.data
        
    def pop_back(self): # removes and returns the last element
        if self.tail == None:
            print("List is empty")

        else:
            temp = self.tail
            temp.prev.next = None # removes next pointer referring to old tail
            self.tail = temp.prev # make second to last element the new tail
            temp.prev = None # remove previous pointer referring to new tail
            return temp.data
        
    def insert_after(self, temp_node, new_data): # Inserting a new node after a given node
        if temp_node == None:
            print("Given node is empty")

        if temp_node != None:
            new_node = Node(new_data)
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
            if new_node.next != None:
                new_node.next.prev = new_node
            
            if temp_node == self.tail: # checks whether new node is being added to the last element
                self.tail = new_node # makes new node the new tail
        

  
    def insert_before(self, temp_node, new_data): # Inserting a new node before a given node
        if temp_node == None:
            print("Given node is empty")
        
        if temp_node != None:
            new_node.prev = temp_node.prev
            temp_node.prev = new_node
            new_node.next = temp_node
            if new_node.prev != None:
                new_node.prev.next = new_node
        
            if temp_node == self.head: # checks whether new node is being added before the first element
                self.head = new_node # makes new node the new head