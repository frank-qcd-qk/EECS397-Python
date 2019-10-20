from stack import Stack


class UniqueStack(Stack):
    """
    UniqueStack has the same methods and functionality as Stack, but will only store one
    copy of a particular item at a time.

    If push is called with an item that is already in the UniqueStack, a ValueError should be raised
    with an appropriate error message. (DONE)

    If push is called where item equals None, a TypeError should be raised like in the base class.

    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. New versions of __init__(), push(), and pop() should be sufficient.

    Hint: One option to implement this is to maintain an internal set() alongside the internal list.
    """

    def __init__(self):
        self._stack_items = []

    #! Added value error
    def push(self, item):
        """
        Add item to the stack.

        Raises a TypeError if item equals None.
        """
        if item == None:
            raise TypeError("Stack will not store an object of NoneType.")
        if item in self._stack_items:
            raise ValueError("StackItem already exists in the stack.")
        else:
            self._stack_items.append(item)

    def pop(self):
        """
        If the stack contains at least one item, remove the last
        item that was added to the stack and return it.
        Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items.pop()
        else:
            return None

    def peek(self):
        """
        If the stack contains at least one item, return the value of last
        item that was added to the stack. Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items[-1]
        else:
            return None

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self._stack_items)


class LimitedStack(Stack):
    """
    A LimitedStack has the same methods and functionality as Stack, but will only hold up to a certain
    number of items.

    The __init__ method for LimitedStack should take a single, positive integer as an argument. This will
    be the maximum number of items that the LimitedStack can hold. If push is called with an item and that
    item would go beyond the LimitedStack's capacity, the item is not added to the LimitedStack and a
    LimitedStack.LimitedStackOverflowError should be raised.

    If push is called where item equals None, a TypeError should be raised like in the base class.

    If __init__ is called with a non-integer argument, a TypeError should be raised.
    If __init__ is called with an int <= 0, a ValueError should be raised.

    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. New versions of __init__() and push() should be sufficient.
    """
    class LimitedStackOverflowError(Exception):
        pass

    def __init__(self, length):
        if type(length) is not int:
            raise TypeError("Stack length must be an integer")

        self._length_cap = length

        if self._length_cap <= 0:
            raise ValueError("Stack length cannot be 0 or smaller than 0!")

        self._stack_items = []

    def push(self, item):
        """
        Add item to the stack.

        Raises a TypeError if item equals None.
        """
        if (self._length_cap.length >= self._length_cap):
            raise LimitedStackOverflowError("Stack overflow!")

        if item == None:
            raise TypeError("Stack will not store an object of NoneType.")
        self._stack_items.append(item)

    def pop(self):
        """
        If the stack contains at least one item, remove the last
        item that was added to the stack and return it.
        Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items.pop()
        else:
            return None

    def peek(self):
        """
        If the stack contains at least one item, return the value of last
        item that was added to the stack. Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items[-1]
        else:
            return None

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self._stack_items)

class RotatingStack(LimitedStack):
    """
    A RotatingStack has the same methods and functionality as LimitedStack, but will not raise an
    exception when an item is added that would go beyond the maximum capacity. Instead, the item
    will be added to the stack and then the oldest item from the RotatingStack will be dropped.

    The __init__ method for RotatingStack should take a single, positive integer as an argument. This will
    be the maximum number of items that the RotatingStack can hold. If push is called with an item and that
    item would go beyond the Rotating's capacity, the item will be added to the stack, but only after
    discarding the oldest item in the stack.

    If push is called where item equals None, a TypeError should be raised like in the base class.

    If __init__ is called with a non-integer argument, a TypeError should be raised.
    If __init__ is called with an int <= 0, a ValueError should be raised.

    Define and implement the relevant methods from the base Stack class to enable the behavior
    described above. As long as LimitedStack has properly handled the __init__ method functionality,
    only a new version of push() should be needed.
    """

    def __init__(self, length):
        if type(length) is not int:
            raise TypeError("Stack length must be an integer")

        self._length_cap = length

        if self._length_cap <= 0:
            raise ValueError("Stack length cannot be 0 or smaller than 0!")

        self._stack_items = []

    def push(self, item):
        """
        Add item to the stack.

        Raises a TypeError if item equals None.
        """
        if (len(self._length_cap) >= self._length_cap):
            self._stack_items.pop()

        if item == None:
            raise TypeError("Stack will not store an object of NoneType.")
        self._stack_items.append(item)

    def pop(self):
        """
        If the stack contains at least one item, remove the last
        item that was added to the stack and return it.
        Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items.pop(0)
        else:
            return None

    def peek(self):
        """
        If the stack contains at least one item, return the value of last
        item that was added to the stack. Otherwise, return None.
        """
        if self._stack_items:
            return self._stack_items[-1]
        else:
            return None

    def size(self):
        """
        Return the number of items in the stack.
        """
        return len(self._stack_items)
