from SLNode import SLNode

class StackException(Exception):
    """
    Custom exception to be used by Stack class
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds a new node to the top of the stack
        """
        temp = self._head
        self._head = SLNode(value)
        self._head.next = temp

    def pop(self) -> object:
        """
        Removes the element at the top of the stack and returns it.
        """
        if not self.is_empty():
            val = self._head.value
            self._head = self._head.next
            return val
        else:
            raise StackException


    def top(self) -> object:
        """
        REturns the top element from the stack without removing it
        """
        if not self.is_empty():
            return self._head.value
        else:
            raise StackException

if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
