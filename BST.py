class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, value):
        if self.value:
            if value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:                               
                    self.right.add(value)
            elif value <= self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add(value)
        else:
            self.value = value
            
    def search(self, value, parent=None):
        if value > self.value:
            if self.right is None:
                return None, None
            return self.right.search(value, self)
        elif value < self.value:
            if self.left is None:
                return None, None
            return self.left.search(value, self)
        else:
            return self, parent

    def delete(self, value):
        node, parent = self.search(value)
        if node.left is None and node.right:
            parent.left = node.right
        elif node.left and node.right is None:
            parent.right = node.left
        elif node.left and node.right:
            
        else:
            if parent:
                if parent.left and parent.left.value == node.value:
                    parent.left == None
                elif parent.right and parent.right.value == node.value:
                    parent.right == None
            else:
                self.
            



    def printN(self):
        print(self.value)
    def printR(self):
        print(self.right.value)
    def printL(self):
        print(self.left.value)


root = Node(8)
root.add(9)
root.add(1)
root.add(10)

print(root.search(10)[0].value)

root.printN()
root.printR()
root.printL()
