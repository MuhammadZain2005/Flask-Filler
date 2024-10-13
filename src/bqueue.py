class BoundedQueue:
    # Creates a new empty queue:
    def __init__(self, capacity):
        assert isinstance(capacity, int), (
                'Error: Type error: %s' % (type(capacity)))
        assert capacity >= 0, 'Error: Illegal capacity: %d' % capacity
        self.__items = []
        self.__capacity = capacity


    # Adds a new item to the back of the queue, and returns nothing
    def enqueue(self, item):
        if self.isFull():
            raise Exception('Error: Queue is full')
        self.__items.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)

    # Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items[0]

    # Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        return len(self.__items) == 0

        # Returns True if the queue is full, and False otherwise:

    def isFull(self):
        return len(self.__items) == self.__capacity

    # Returns the number of items in the queue:
    def size(self):
        return len(self.__items)

        # Returns the capacity of the queue:

    def capacity(self):
        return self.__capacity

    # Removes all items from the queue, and sets the size to 0
    # clear() should not change the capacity
    def clear(self):
        self.__items = []

    # Returns a string representation of the queue:
    def __str__(self):
        str_exp = ""
        for item in self.__items:
            str_exp += (str(item) + " ")
        return str_exp

    # Returns a string representation of the object bounded queue:
    def __repr__(self):
        return str(self) + " Max=" + str(self.__capacity)
