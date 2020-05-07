
from tad_list import List
from nodes import SingleListNode

class SinglyLinkedList(List):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    def size(self):
        return self.count

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        return self.head.get_element()
    
    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException
    def get(self, position):
        node = self.head
        for i in range(position):
            node = node.get_next()
        return node.get_element()
    
    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        node = self.head
        for i in range(self.size):
            if node.get_element() == element:
                return i
            node = node.get_next()
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
            node = self.head
            if node.get_element() == element:
                node = node.set_element()
            return node.get_element()

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element): 
        node = self.tail
        if node.get_element() == element:
            node = node.set_element()
        return node.get_element()

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        node = self.head
        for i in range(position):
            if node.get_element() == element:
                insert_first()
                return i
            elif node.get_element() != element:
                node = node.get_next()
            elif node.get_next == position:
                insert_last()
                return i
        return node.get_element()

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
    
    # Removes all elements from the list.
    def make_empty(self):

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
            


       
    




    

        
    


    