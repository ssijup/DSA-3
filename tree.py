class Tree:
    def __init__(self, value) :
        self.value = value
        self.childrenn = []
        self.parent = None

    def children(self, val) :
        self.childrenn.append(val)

    def printTree(self, parent=None) :
        if parent:
            print(f"Parent: {parent.value}, Child: {self.value}")
        else:
            print(f"Root: {self.value}")
        # if self.children:
        for i in self.childrenn :
            # print(i.value)
            i.printTree(self)

    def printParent(self):
        for i in self.childrenn:
            print(i.value)

root=Tree("A")
c1= Tree("B")
c2=Tree("C")
c3=Tree("D")
c4=Tree("E")

root.children(c1)
root.children(c2)
# root.children(c3)
# root.children(c4)
c1.children(c3)
c2.children(c4)

root.printTree()
print()
root.printParent()

# arikombandra