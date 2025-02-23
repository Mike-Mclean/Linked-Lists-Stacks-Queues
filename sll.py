from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        """
        return not self._head.next

    def insert_front(self, value: object) -> None:
        """
        Inserts a new node at the front of the linked list
        """
        if self.is_empty():
            self._head.next = SLNode(value)
        else:
            old_head = self._head.next
            self._head.next = SLNode(value, old_head)

    def insert_back(self, value: object) -> None:
        """
        Inserts a new node at the back of the linked list
        """
        new_node = SLNode(value)
        if self.is_empty():
            self._head.next = new_node
        else:
            node = self._head.next
            while node.next:
                node = node.next
            node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a node with the given value at the given index
        """
        if index < 0 or index > self.length():
            raise SLLException

        if index == 0:
            self.insert_front(value)
        else:
            node = self._head.next
            for _ in range(index - 1):
                node = node.next
            old_node = node.next
            node.next = SLNode(value, old_node)

    def remove_at_index(self, index: int) -> None:
        """
        Removes a node from the list at the given index
        """
        if index < 0 or index > self.length() - 1:
            raise SLLException
        
        node = self._head
        ind = 0
        while ind <= index - 1:
            node = node.next
            ind += 1
        node.next = node.next.next

    def remove(self, value: object) -> bool:
        """
        Removes the first item in the list that has the given value
        """
        node = self._head.next
        index = 0
        while node.value != value:
            if not node.next:
                return False
            else:
                node = node.next
                index += 1
        
        self.remove_at_index(index)
        return True


    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that have the provided value
        """
        cnt = 0
        node = self._head.next
        while node:
            if node.value == value:
                cnt += 1
            node = node.next
        return cnt
            

    def find(self, value: object) -> bool:
        """
        Determines whether the value exists in the list or not. Returns True if the value is in the list
        and False otherwise
        """
        node = self._head.next
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns a new Linked List which that contains the requested number of nodes from the original list
        starting from the given index
        """
        if start_index < 0 or start_index > self.length() - 1 or start_index + size > self.length():
            raise SLLException
        
        node = self._head.next
        ind = 0
        while ind < start_index:
            node = node.next
            ind += 1
        
        new_list = LinkedList()
        count = 0 
        while count < size:
            new_list.insert_back(node.value)
            node = node.next
            count += 1
        
        return new_list
    
    def reverse(self) -> "LinkedList":
        """
        Reverses the Linked List
        """
        current = self._head.next
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self._head.next = prev


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
    
    print("\n# reverse example 1")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    lst.reverse()
    print("Reversed:", lst )