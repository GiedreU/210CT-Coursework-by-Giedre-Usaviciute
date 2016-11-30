from queue import *

class E(object):
    def __init__(self, label, edges = []):
        self.label = label
        self.edges = []

class G(object):
    def __init__(self):
        self.graph = []
    
    def add(self,e):
        self.graph.append(e)
        
    def edge(self, e1, e2):
        for i in self.graph:
            if i == e1 and e2 not in i.edges:
                i.edges.append(e2)
            if i == e2 and e1 not in i.edges:
                i.edges.append(e1)

def depthFirstSearch(G, v):
    S = []
    visited = []
    S.append(v)
    while len(S)!=0:
        u = S.pop()
        if u not in visited:
            visited.append(u)
            for e in u.edges:
                S.append(e)
    return visited

def breadthFirstSearch(G,v):
    Q = Queue(maxsize = 0)
    visited = []
    Q.put(v)
    while not Q.empty():
        u = Q.get()
        if u not in visited:
            visited.append(u)
            for e in u.edges:
                Q.put(e)
    return visited

node1 = E(1,None)
node2 = E(2,None)
node3 = E(3,None)
node4 = E(4,None)
node5 = E(5,None)
node6 = E(6,None)
node7 = E(7,None)
node8 = E(8,None)
node9 = E(9,None)
graph = G()
graph.add(node1)
graph.add(node2)
graph.add(node3)
graph.add(node4)
graph.add(node5)
graph.add(node6)
graph.add(node7)
graph.add(node8)
graph.add(node9)
graph.edge(node1,node2)
graph.edge(node1,node3)
graph.edge(node3,node4)
graph.edge(node3,node5)
graph.edge(node4,node6)
graph.edge(node4,node7)
graph.edge(node7,node5)
graph.edge(node5,node9)
graph.edge(node9,node8)
graph.edge(node2,node1)

dep =depthFirstSearch(graph, node1)
bre = breadthFirstSearch(graph, node1)
for i in dep:
    print(i.label)
for i in bre:
    print(i.label)
