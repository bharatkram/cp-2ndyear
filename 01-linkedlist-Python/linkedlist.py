"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # Your code goes here
        if self.head == None:
            self.head = new_element
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        current = self.head
        while position != 1:
            current = current.next
            if current == None:
                return None
            position -= 1
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        ele = self.get_position(position - 1)
        new_element.next = ele.next
        ele.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        if self.head.value == value:
            self.head = self.head.next
            return
        past = self.head
        ele = past.next
        if ele == None:
            return
        while ele.value != value:
            if ele.next == None:
                return
            past = ele
            ele = ele.next
        past.next = ele.next
