import collections

#creating our object
class Node:
    #defining our object
    def __init__(self,data):
        self.left=None
        self.right= None
        self.data=data
    #recursive insert function
    def insert(self,data):
        if self.data is None:
            self.data=data
        else: 
            if data <self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)

#function to print 
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end= '  ')
        inOrderPrint(r.right)

#function to print
def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end= '  ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)

#function to print
def postOrderPrint(r):
    if r is None:
        return
    else:
        postOrderPrint(r.right)
        print(r.data, end= '  ')
        postOrderPrint(r.left)

#function to print parent node with childs        
def makeList(r):
    if r is None:
        return
    else:
        d[r.data] =[]
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        if r.right:
            d[r.data].append(r.right.data)
        makeList(r.right)
    return d

#function to print parent after getting kids 
def bfs(al):
    queue=collections.deque('g')
    visited = []

    while queue:
        node= queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
        #same ad for x in al[node]:queue.append(x)
    print(visited)    

def dfs(al):
    stack=['g']
    visited = []
    
    while stack:
        node= stack.pop()
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
            #same ad for x in al[node]:stack.append(x)
    print(visited) 

#function to print if we have a the given key
def search(al,key):
    stack=['g']
    visited=[]
    found= False
    while stack:
        node=stack.pop()
        if node == key:
            return True
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    return found

if __name__ =='__main__':
    root = Node("g")
    root.insert("c")
    root.insert("b")
    root.insert("a")
    root.insert("e")
    root.insert("d") 
    root.insert("f")
    root.insert("t")
    root.insert("y")
    root.insert("o")
    root.insert("n") 
    root.insert("k")

    d={}
    aList=makeList(root)

print("")
print("inOrder")
inOrderPrint(root)
print("")
print("preOrder")
preOrderPrint(root)
print("")
print("postOrder")
postOrderPrint(root)
print("")
print("Adjacency List")
for L in aList:
    print(f'{L}:{d[L]}')
print("")
print("BFS")
bfs(aList)
print("")
print("DFS")
dfs(aList)
print("")
k="c"
print(f'We have {k} in our tree!')
print (search(aList,k))