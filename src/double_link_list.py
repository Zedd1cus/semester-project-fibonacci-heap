from math import inf


class ListNode:
    def __init__(self, key, left=None, right=None, parrent=None):
        self.key = key
        self.left = left
        self.right = right
        self.children = DoubleLinkList(parrent=self)
        self.parrent = parrent  # -> Node
        self.order = 0 # кол-во детей этого узла

    def add_at_end(self, nd):
        if nd.key > self.key:
            self.children.set(nd)
            self.order = self.order + 1
            return True
        return False


class DoubleLinkList:
    def __init__(self, parrent = None):
        self.head = None
        self.tale = None
        self._parrent = parrent # Node
        self.num_of_nd = 0

    def set(self, new_node):
        if self.find(new_node.key) is not None:
            return False
        new_node.parrent = self._parrent
        if self.tale is None:
            self.head = new_node
            self.tale = self.head
            self.head.left = self.tale
            self.tale.right = self.head
        else:
            self.tale.right = new_node
            self.head.left = new_node
            new_node.left = self.tale
            self.tale = new_node
            self.tale.right = self.head
        self.num_of_nd += 1
        return True

    def __iter__(self):
        self.iter_node = self.head
        self.cycle = 0
        return self

    def __next__(self):
        if self.iter_node == self.head:
            self.cycle += 1
        if self.cycle == 2 or self.iter_node is None:
            raise StopIteration
        ret_node = self.iter_node
        self.iter_node = self.iter_node.right
        return ret_node

    def find(self, key):
        for node in self:
            if node.key == key:
                return node
        return None

    def change_parrent(self, new_parrent):
        self._parrent = new_parrent
        for node in self:
            node.parrent = self._parrent

    def find_min(self):
        if self.num_of_nd == 0:
            return None
        min_nd = ListNode(inf)
        for node in self:
            if node.key < min_nd.key:
                min_nd = node
        return min_nd

    def remove(self, node):
        if self.find(node.key) is None:
            return False
        if self.num_of_nd == 1:
            self.head = None
            self.tale = None
        elif node == self.head:
            self.tale.right = self.head.right
            self.head.right.left = self.tale
            self.head = self.head.right
        elif node == self.tale:
            self.head.left = self.tale.left
            self.tale.left.right = self.head
            self.tale = self.tale.left
        else:
            lft = node.left
            rht = node.right
            lft.right = rht
            rht.left = lft
        self.num_of_nd -= 1
        return True

