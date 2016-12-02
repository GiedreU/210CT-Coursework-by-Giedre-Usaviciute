
class E(object):
    def __init__(self, label, tw, pre, edges = []):
        self.label = label
        self.edges = []
        self.tw = tw
        self.pre = pre

class G(object):
    def __init__(self):
        self.graph = []
    
    def add(self,e):
        self.graph.append(e)

    def edge(self, e1, e2, value):
        linkedVal = (e2,value)
        linkedVal2 = (e1,value)

        for i in self.graph:
            if i == e1 and e2 not in i.edges:
                i.edges.append(linkedVal)
            if i == e2 and e1 not in i.edges:
                i.edges.append(linkedVal2)

def dijkstra(graph,s,d):
    v = s #1st node
    for n in graph.graph:
        n.tw = float('inf')
    s.tw = 0
    visited = []
    while v.label != d.label: #v = has to be  node
        for u in v.edges:
            adjNode = u[0]
            if v.tw + u[1] < adjNode.tw:
                adjNode.tw = v.tw + u[1]
                adjNode.pre = v
        visited.append(v)
        mini = float('inf')
        for i in v.edges:
            if i[0] not in visited and i[0].tw < mini:
                v = i[0]
                mini = i[0].tw

    
                
                
graph = G()
node1 = E(1,None,None, None)
node2 = E(2,None,None, None)
node3 = E(3,None, None, None)
node4 = E(4,None, None, None)
node5 = E(5,None, None, None)
node6 = E(6,None, None, None)
graph.add(node1)
graph.add(node2)
graph.add(node3)
graph.add(node4)
graph.add(node5)
graph.add(node6)
graph.edge(node1,node2,10)
graph.edge(node2,node3,5)
graph.edge(node1,node3,4)
graph.edge(node1,node6,9)
graph.edge(node2,node4,1)
graph.edge(node3,node4,20)
graph.edge(node6,node5,6)
graph.edge(node6,node4,7)
graph.edge(node5,node4,3)
 
dijkstra(graph, node1, node4)
node = node4
while node.pre!=None:
    print(node.pre.label)
    node = node.pre

