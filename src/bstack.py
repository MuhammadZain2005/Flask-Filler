class BoundedStack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def push(self, item):
        if len(self.items) >= self.capacity:
            raise Exception("Stack overflow: cannot push to a full stack")
        self.items.append(item)

    def is_sealed(self):
        # Checks if the top 3 elements are the same, indicating the flask is sealed
        if self.size() < 3:
            return False
        return len(set(self.items[-3:])) == 1

    def reversed_items(self):
        return self.items[::-1]

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek an empty stack")
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def __str__(self):
        return ' '.join(str(item) for item in self.items) + ' '

    def clear(self):
        self.items = []

    def isFull(self):
        return len(self.items) == self.capacity
