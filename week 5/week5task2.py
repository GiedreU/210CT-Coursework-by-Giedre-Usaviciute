class Node(object):
  def __init__(self, value):
      self.value=value
      self.next=None
      self.prev=None

class List(object):
  def __init__(self):
      self.head=None
      self.tail=None
  def insert(self,n,x):
      ''' Function takes insertion location as n and node which will be inserted as x.
      It inserts node x after n node, creating link from n to x, from x to next node
      to which n was linked before. '''
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x              
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x

          
  def delete(self, n):
      '''Deletes given node n by changing links: from previously linked to n to node to which was n linked to, and
      changing previous node of node to which n was linked to into the node previously linked to n.
      If n is head, n.next becomes head, if n is tail, n.previous becomes tail'''
      if n.prev != None:
          n.prev.next = n.next
      else:
          self.head = n.next
                    
      if n.next != None:
          n.next.prev = n.prev
      else:
          self.tail = n.prev
          
          
  def display(self):
      '''Linked node values appended to a list begining head node until there is none node'''
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
      print ("List: ",",".join(values))
      
if __name__ == '__main__':
  l=List()
  node4 = Node(4)
  node6 = Node(6)
  node2 = Node(2)
  node8 = Node(8)
  l.insert(None, node4)
  l.insert(l.head,node6)
  l.insert(l.tail,node2)
  l.insert(l.head,node8)
  l.delete(node4)
  l.display()
