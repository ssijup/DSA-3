class Node :
    def __init__(self ,data) :
        self.left = None
        self.data = data
        self.right = None

class Tree :
    def newNode(self ,data) :
        return Node(data)
    
    def insert(self ,node , data) :
        if node is None :
            return self.newNode(data)
        else :
            if data < node.data :
                node.left = self.insert(node.left ,data)
            else :
                node.right = self.insert(node.right ,data)
            return node

    def traverseInorder(self ,root) :
        if root is not None :
            self.traverseInorder(root.left)
            print(root.data,end=" ") 
            self.traverseInorder(root.right)
            # print(root.data,end=" ") 

    def traversePreorder(self ,root) :
        if root is not None :
            print(root.data,end=" ")
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root) :
        if root is not None :
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.data,end=" ")

    
    def heightOfTheTree(self, root) :
        if root is None :
            return -1
        return max(self.heightOfTheTree(root.left) , self.heightOfTheTree(root.right) ) + 1
    
    def levelOrder(self, root) :
        q = []
        q.append(root)
        while len(q) != 0 :
            root = q.pop(0)
            print(root.data, end=" ")
            if root.left is not None :
                q.append(root.left)
            if root.right is not None :
                q.append(root.right)
    
    def isbst(self ,root, l):
        if root is not None :
            # return print("The tree is empty")
            self.isbst(root.left,l)
            l.append(root.data)
            self.isbst(root.right,l)
            # print(l,"gy")
            return l   
         
    def closest(self, root, target):
        clostestValue = root.data
        minDiff = abs(root.data - target )
        while root:
            diff = abs(root.data - target)
            if  diff < minDiff :
                clostestValue = root.data
                minDiff = diff

            if target < root.data :
                root = root.left
            elif target > root.data:
                root = root.right
            else:
                return root.data
            
        return clostestValue

    def deleteANode(self, root, target):
        closeValue = target
        minDiff = abs(root.data - target)
        while root:
            diff = abs(root.data - target)
            if diff < minDiff:
                closeValue = root.data
                minDiff = diff
            if target < root.data :
                root = root.left
            elif target > root.data:
                root = root.right
            else :
                print("The same value")
                return closeValue
        return closeValue

    def deletee(self,root, data):
        if root is None:
            print("1kkkk")
            return None
        if data < root.data:
            print("left")
            root.left = self.deletee(root.left, data)
        elif data > root.data:
            print("right")
            root.right = self.deletee(root.right,  data)
        else : 
            print("else")
            if not root.left and not root.right:
                print("2kkk")
                return None
            if not root.left:
                print(" left The number not found")
                print("1")
                return root.right
            if root.right is None:
                print(" Right The number not found")
                return root.left
            minNode = self.getMinValue(root.right)
            root.data = minNode.data
            root.right = self.deletee(root.right, minNode.data)
        return root


    def getMinValue(self, root):
        while root.left:
            root = root.left
        print(root.data,"kkkkkkkkkkkkkk")
        return root
    
    def getTheMax(self, root):
        while root.right:
             root = root.right
        return root.data


tree=Tree()
root=tree.newNode(111)
print(root.data)
tree.insert(root,22)
tree.insert(root,3)
tree.insert(root,9)
tree.insert(root,5)
tree.insert(root,60)
tree.insert(root,7)
tree.insert(root,8)
tree.insert(root,90)
# print("Traversing Inorder")
# tree.traverseInorder(root)
# print("Traversing Preorder")
# tree.traversePreorder(root)
# print("Traversing Postorder")
# tree.traversePostorder(root)
# print("The height of the tree is :",tree.heightOfTheTree(root))
# print("Level order :")
# tree.levelOrder(root)

l = []
print("The ",tree.isbst(root,l))
for i in range(len(l) - 1) :
    flag = 1
    if l[i] > l[i+1] :
         flag= 0
         break
if flag == 0 :
    print("The tree is not Bst")
else :
    print("The the tree is Bst")

# print()
# k=tree.closest(root, 6)
# print(k)
print()
k=tree.deleteANode(root, 10)
print(k)
tree.deletee(root, 111)
print("op")
tree.traverseInorder(root)
min = tree.getMinValue(root)
print("The minimumvalue in tree is : ",min.data)
max = tree.getTheMax(root)
print("The minimumvalue in tree is : ",max)




    