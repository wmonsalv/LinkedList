class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0: #Checks if ll is empty 
            return None
        temp = self.head #These two will help us keep up with the last node and the next to last 
        pre = self.head
        while(temp.next): #while there is a pointer that is pointing to another node 
            pre = temp 
            temp = temp.next
        self.tail = pre # After loop is completed, moves the tail pointer to the next to last node, which takes care of removing our last node
        self.tail.next = None
        self.length -= 1
        if self.length == 0: #This last section allows us to pop the only remaining node in the list 
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head # we make the new node point to head 
            self.head = new_node #after that is done, we make head point to the new node
        self.length += 1
        return True 
    
    def pop_first(self):
        if self.length == 0: #returns none if there are no nodes to return
            return None 
        temp = self.head 
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        if self.length == 0: #this one checks again to see if the numebr of nodes is set to zero after we pop our node
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range (index):
            temp = temp.next
        return temp
    
    def set_value(self, index, new_value):
       temp = self.get(index)
       if temp is not None:
           temp.value = new_value
           return True
       return False
    
    def insert(self, index, value):
        new_node = Node(value) # First, we create the node
        if index < 0 or index >= self.length: #if we have an index that is out of range
            return False
        elif index == 0 :
            return self.prepend(value)
        elif index == self.length :
            return self.append(value)
        else:
            temp = self.get(index-1) # will help us point to the appropriate node
            new_node.next = temp.next #now we are both pointing to what the node in front of our index node is pointing to, which is the targte/index node entered as a parameter in the code
            temp.next = new_node
            self.length += 1
            return True
    
    def remove(self, index):
        if index > self.length or index < 0:
            return None #we return none because none would be the opposite of returning a node
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1) # we are going to point the previous node point to wathever the index node is pointing to 
        temp = prev.next
        prev.next = temp.next # here we are saying, point the prev node to whatever the current node was pointing to
        temp.next = None #This removes our item from the list
        self.length -= 1 #since we popped one out, we need to decrease the length of the list
        return temp #returns the node being popped 
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length): #order of the bottom steps has to be exact 
            after = temp.next #this moves us one over to set things up for the arrow switiching
            temp.next = before #this flips the arrow (refer to illustration)
            before = temp #then we move before over to the next node
            temp = after #then we can move temp over to the next node as well and continue the process
       
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and slow is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value


ll = LinkedList(0)
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.find_middle_node())

# print("list before reversal: ")
# ll.print_list()
# print("list after reversal: ")
# ll.reverse()
# ll.print_list()

# print("Before prepending")
# ll.print_list()
# print("after prepending")
# ll.prepend(1)
# ll.prepend(0)
# # ll.print_list()
# print(f"popping the first node of value {ll.pop_first()}")
# print("Index result:")
# print(ll.get(2))
# print("list print")
# ll.print_list()
# print("print after set")
# ll.set_value(2,5)
# ll.print_list()
# print(f"get: {ll.get(2)}")