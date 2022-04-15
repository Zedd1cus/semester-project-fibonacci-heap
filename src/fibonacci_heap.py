import math
from double_link_list import DoubleLinkList, ListNode

class FibonacciHeap:

    def __init__(self):
        self.trees = DoubleLinkList()
        self.least = None # Min
        self.count = 0 # кол-во корневых узлов
        self.max_order = 0

    def insert(self, key):
        new_tree = ListNode(key)
        self.trees.set(new_tree)
        if (self.least is None or key < self.least.key):
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self):
        if self.least is None:
            return None
        return self.least.key

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.set(child) # 1
            self.trees.remove(smallest) # 1
            if self.trees.num_of_nd == 0:
                self.least = None
            else:
                self.least = self.trees.head
                self._consolidate()
            self.count = self.count - 1
            return smallest.key

    def _consolidate(self): # log_n + n
        aux = (self.max_order + self.count-1) * [None] # массив размера - сумма
        while self.trees.num_of_nd != 0:
            x = self.trees.head
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1 # кол-во детей +1 тк опустили y, теперь его нужно сливать с узлами порядка order+1
            aux[order] = x
        self.least = None
        for k in aux:
            if k is not None:
                self.trees.set(k)
                if (self.least is None
                        or k.key < self.least.key):
                    self.least = k

    @property
    def max_order(self):
        max_order = -math.inf
        for node in self.trees:
            if node.order < max_order:
                max_order = node.order
        return max_order

    def union(self, other): # 1
        if self.count == 0:
            self.count = other.count
            self.trees.tale = other.trees.tale
            self.trees.head = other.trees.head
            self.least = other.least
        elif other.count != 0:
            if self.least.key > other.least.key:
                self.least = other.least
            self.trees.tale.right = other.trees.head
            other.trees.head.left = self.trees.tale
            other.trees.tale.right = self.trees.head
            self.trees.head.left = other.trees.tale
            self.trees.tale = other.trees.tale
            self.count += other.count

if __name__ == '__main__':
    fheap = FibonacciHeap()

    print('Menu')
    print('insert <data>')
    print('min get')
    print('min extract')
    print('quit')

    while True:
        do = input('What would you like to do? ').split()

        operation = do[0].strip().lower()
        if operation == 'insert':
            data = int(do[1])
            fheap.insert(data)
        elif operation == 'min':
            suboperation = do[1].strip().lower()
            if suboperation == 'get':
                print('Minimum value: {}'.format(fheap.get_min()))
            elif suboperation == 'extract':
                print('Minimum value removed: {}'.format(fheap.extract_min()))

        elif operation == 'quit':
            break