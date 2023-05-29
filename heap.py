class Heap :
    def __init__(self, maxCapacity) :
        self.size = 0
        self.maxCapacity = maxCapacity
        self.array = [None]* maxCapacity

    def leftChild(self, i) :
        return (2 * i + 1)
    
    def rightChild(self, i) :
        return (2 * i + 2)
    
    def parent(self , i) : 
        return (i - 1) // 2
    
    def insert(self, val) :
        # if self.size == 0 :
        #     self.array[0] = val
        #     self.size +=1
        #     print("The first val inserted")
        #     return
        if self.size == self.maxCapacity: 
            print("THe heap is full") 
            return
        self.size +=1
        self.array[self.size-1] = val
        print(f"The {val} Inserted sucessfully")
        i = self.size -1
        while i!= 0 and self.array[self.parent(i)] < self.array[i] :
            self.array[self.parent(i)], self.array[i] = self.array[i], self.array[self.parent(i)]
            i = self.parent(i)

    def heapifyDown(self, i) :
        n=i
        rootIndex = i
        leftIndex = self.leftChild(i)
        rightIndex = self.rightChild(i)
        print(leftIndex,rightIndex,"op")
        if leftIndex < self.size and  self.array[leftIndex] > self.array[i] :
            rootIndex = leftIndex
        if rightIndex < self.size and  self.array[rightIndex] > self.array[rootIndex] :
            rootIndex = rightIndex
        if rootIndex != i :
            print(self.array,n,"nnn")
            print(self.array[rootIndex],self.array[i],rootIndex,i,"rootindex,i")
            temp = self.array[i]
            self.array[i] = self.array[rootIndex]
            self.array[rootIndex] = temp
            print(self.array,n,"nnn")
            n +=1
            print()
            # self.array[i], self.array[rootIndex] = self.array[rootIndex], self.array[i]
            self.heapifyDown(rootIndex)

        # print("All done ")
        
    def removeMax(self) :
        if self.isEmpty() :
            print("The heap is Empty")
            return
        root = self.array[0]
        self.array[0] = self.array[self.size -1]
        self.heapifyDown(0)


    def isEmpty(self) :
        if self.size == 0:
            return True
        
    def heapSort(self) :
        self.heapifyDown(0)
        l=self.size -1
        arr=[]

        # for i in range(l // 2 , -1, -1):
        #     self.heapifyDown(i)
        #     print("0")
        print(self.array,"oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        print("Done the for loop")
        for i in range(l , 0, -1) :
            # arr.append(self.array[0])
            self.array[0], self.array[i] = self.array[i], self.array[0]
            # arr.append(self.array.pop())
            self.heapifyDown(0)
        # print(self.array.reverse())
        # print(arr,"hiii")
            

h=Heap(5)
print(h.array)
h.insert(7)
h.insert(0)
h.insert(55)
h.insert(6)
h.insert(88)
print(h.array)
h.heapifyDown(0)
print(h.array)
h.removeMax()
print("After removing max")
print(h.array)
h.heapSort()
print("After sorthing :")
print(h.array)
