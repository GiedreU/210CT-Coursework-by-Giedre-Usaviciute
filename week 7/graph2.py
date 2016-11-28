from queue import *


class Node(object):
    def __init__(self,node, linkedTo):
        self.node = node
        self.linkedTo = []

    


graph = []

def insert_node(graph, node):
    graph.append(Node(node,None))

def insert_link(graph, link):
    n1,n2 = link
    if len(graph)!=0:
        for item in graph:
            if item.node == n1:
                if n2 not in item.linkedTo:
                    item.linkedTo.append(n2)
            if item.node == n2:
                if n1 not in item.linkedTo:
                    item.linkedTo.append(n1)

def depth(graph,v):
    visited = []
    S = []
    S.append(v)           
    while len(S)!=0:
        u = S.pop()
        if u not in visited:
            visited.append(u)
            for i in graph:
                if i.node == u:
                    for j in i.linkedTo:
                        S.append(j)

    return visited


def breadth(graph, v):
    visited = []
    Q = Queue(maxsize = 0)
    Q.put(v)             
    while not Q.empty():
        u = Q.get()
        if u not in visited:
            visited.append(u)
            for i in graph:
                if i.node == u:
                    for j in i.linkedTo:
                        Q.put(j)

    return visited

                
        
             
        
        

insert_node(graph, 1)
insert_node(graph, 2)
insert_node(graph, 3)
insert_node(graph, 4)
insert_node(graph, 5)
insert_node(graph, 6)
insert_node(graph, 7)
insert_node(graph, 8)
insert_node(graph, 9)
insert_link(graph,(1,2))
insert_link(graph,(1,3))
insert_link(graph,(3,4))
insert_link(graph,(3,5))
insert_link(graph,(4,6))
insert_link(graph,(4,8))
insert_link(graph,(4,7))
insert_link(graph,(7,5))
insert_link(graph,(5,9))
insert_link(graph,(9,8))
insert_link(graph,(2,1))



dep = []
dep = depth(graph, 1)
b =[]
b = breadth(graph,1)
print(b)
print (dep)

