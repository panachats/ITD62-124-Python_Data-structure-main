class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def Pre(Infor):
    if Infor is None :
        return
    print(Infor.data)
    Pre(Infor.left)
    Pre(Infor.right)

def In(Infor):
    if Infor is None:
        return
    In(Infor.left)
    print(Infor.data)
    In(Infor.right)

def Post(Infor):
    if Infor is None:
        return
    Post(Infor.left)
    Post(Infor.right)
    print(Infor.data)

def Insert(Infor, Data):
    i = input("L/R : ")
    # If the current node has no left child, then we create a new node and assign it as the left child
    # of the current node. Otherwise, we call the Insert() function recursively on the left child.
    if i == "L":
        if Infor.left == None:
            Infor.left = Node()
            Infor.left.data = Data
            return
        else:
            Insert(Infor.left, Data)
    if i == "R":
        if Infor.right == None:
            Infor.right = Node()
            Infor.right.data = Data
            return
        else:
            Insert(Infor.right, Data)
            
n = Node()
n.data = int(input("Root : "))
while True:
    choice = int(input("1/2/3/4 : "))
    if choice == 1 :
        Pre(n)
    elif choice == 2 :
        In(n)
    elif choice == 3 :
        Post(n)
    elif choice == 4 :
        Insert(n, int(input("Data :")))
    else :
        break
