class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
                # print("Insert sucessfull : ",letter)
            node = node.children[letter]
            print(node.isEnd)
        node.isEnd = True
        print(node.isEnd)

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return "The word is Not there "
            node = node.children[char]
        return node.isEnd
    def prefix(self, word):
        node = self.root
        l = []
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            l.append(char)
        if node.isEnd == False :
            return "The prefix is :", l
        
        

t =Trie()
t.insert("siju")  
t.insert("ram")
t.insert("sijiiu")
t.insert("sijuuu")
print()
print(t.search("sijttt"))
print()
print(t.prefix("si"))