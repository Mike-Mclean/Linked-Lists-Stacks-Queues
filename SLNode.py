class SLNode:
    """
    Singly Linked List Node class
    """
    def __init__(self, value: object, next=None) -> None:
        self.value = value
        self.next = next
