class BST():
    #BST have a starting node and then send the lower value to the left and the greater values to the right
    def __init__(self):
        self.root = Node(None)

    def add(self, value):
        if root.getValue() == None:
            self.root.setValue = value
        else:
            if value > self.root.getValue():
                pass
        return
    def remove(self, value):
        return
    def search(self, value):
        return
    def getRoot(self):
        return self.root

class Node:

    def __init__(self, value):
        self.value = value
        self.left = Node(None)
        self.right = Node(None)

    def setValue (self, value):
        self.value = value

    def getValue(self):
        return self.value

    def addLeft(self, val):
        left = Node(val)

    def addRight(self, val):
        right = Node(val)

    def getLeft(self):
        return self.left.getValue

    def getRight(self):
        return self.right.getValue
