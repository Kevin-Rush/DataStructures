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
        if Node is not None:
            child_count = node.count_children()      # so I need to make this ...?

        if child_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else: 
                self.value = None
                
                
        elif child_count == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                self.left = n.left
                self.right = n.right
                self.value = n.value
        
        else:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left 
            node.value = successor.value
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def count_children(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def print_tree(self):
        
        if self.left:
            self.left.print_tree()
        print (self.value)
        if self.right:
            self.right.print_tree()

    def addList(self, list):
        for i in list:
            self.add(i)
        
    def compare_trees(self, node):
        if node is None:
            return False
        elif self.value != node.value:
            return False
        result = True
        if self.left is None:
            if node.left:
                return False
        else:
            result = self.left.compare_trees(node.left)
        if result is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            result = self.right.compare_trees(node.right)
        return result

root = Node(8)
root.addList([3,10])
root2 = Node(8)
root.addList([3,11])

print(root.compare_trees(root2))

#root.print_tree()
