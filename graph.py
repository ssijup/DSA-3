class Graph :
    def __init__(self) :
        self.adjacentList = {}
        self.numOfNode = 0
    
    def addVertex(self,x) :
        if x in self.adjacentList.keys() :
            print("The is already present")
            return
        self.adjacentList[x] = []
        self.numOfNode +=1
        print(f"The node added sucessfullyn{x}")

    def printGraph(self) :
        for i in self.adjacentList :
            print(i, ":" ,self.adjacentList[i])

    def addEdge(self, n1, n2) :
        if n1 in self.adjacentList.keys() and n2 in self.adjacentList.keys() :
            self.adjacentList[n1].append(n2)
            self.adjacentList[n2].append(n1)

    def removeEdge(self, n1, n2) :
        if n1 in self.adjacentList.keys() and n2 in self.adjacentList.keys() :
            try:
                self.adjacentList[n1].remove(n2)
                self.adjacentList[n2].remove(n1)
                print("Removed edge")
            except ValueError:
                pass

    def removeVerticex(self, x) :
        if x in self.adjacentList.keys() :
            for i in self.adjacentList[x] :
                self.adjacentList[i].remove(x)
            del self.adjacentList[x]
            print("Removed Vertex ducessfully")

    def countOfEdges(self) :
        c=0
        for i in self.adjacentList :
            c += len(self.adjacentList[i])
        count = c // 2
        print("count :", count)

    def bfs(self, vex) :
        self.verticex = {}
        for i in self.adjacentList :
            self.verticex[i] = False
        queue = []
        self.verticex[vex] = True
        queue.append(vex)
        while queue :
            node = queue.pop(0)
            print(node,"visited")
            for i in self.adjacentList[node] :
                if not self.verticex[i] :
                    queue.append(i)
                    self.verticex[i] = True
        
    def dfs(self, vex) :
        self.vertex = {}
        for i in self.adjacentList :
            self.vertex[i] = False
        self.dfsHelper(vex,self.vertex)

    def dfsHelper(self, vex, vertex) :
        self.vertex[vex] = True
        print(vex, "Dfs visited")
        for i in self.adjacentList :
            if self.vertex[i] != True :
                # self.vertex[i] = True
                self.dfsHelper(i, self.vertex)


g=Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.printGraph()
g.addEdge("A", "B")
g.printGraph()
g.addEdge("A", "B")
g.addEdge("A", "C")
g.printGraph()
# g.removeEdge("A", "B")
g.printGraph()
# g.removeVerticex("A")
g.printGraph()
g.countOfEdges()
g.bfs("C")
print()
g.dfs("B")
