class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self.capacity or n + self._size > self.capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            capacity = int(capacity)
        except ValueError:
            raise ValueError("Wrong capacity")
        else:
            if capacity < 0:
                raise ValueError("Wrong capacity")
            self._capacity = capacity

    @property
    def size(self):
        return self._size
