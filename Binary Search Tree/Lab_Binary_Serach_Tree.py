class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    # การท่องไปในแบบ InOrder
    def InOrder(self,tree):
        if tree is not None:
            self.InOrder(tree.leftChild)
            print(tree.data, end=' ')
            self.InOrder(tree.rightChild)

    # การหา Max
    def findMaximumValue(self):
        if self.rightChild == None:
            return self.data
        return self.rightChild.findMaximumValue()

    # การใส่ข้อมูล
    def insert(self, data):
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.leftChild == None:
                self.leftChild  = Node()
                self.leftChild.data  = data
            else:
                self.leftChild.insert(data)
        elif data > self.data:
            if self.rightChild == None:
                self.rightChild  = Node()
                self.rightChild.data  = data
            else:
                self.rightChild.insert(data)

BST = Node()
print("โปรดป้อนจำนวนเต็มเพือจัดเก็บใน Binary search tree ถ้าไม่ต้องการเพิ่มข้อมูลอีกให้ป้อนค่าตัวเลข 999 : ")

# วนลูปรับค่าและส่งค่าจนกว่าจะกดเลข 999
while True:
    # รับค่า data
    number = int(input("โปรดป้อนจำนวณเต็มเพื่อสร้าง AVL tree : "))
    if number != 999:
        BST.insert(number)
    else :
        break

#ส่งค่าไปใน InOrder
print("ผลลัพธ์จากการท่องไปใน Binary search tree ด้วยขันตอนวิธีเเบบ In-order")
BST.InOrder(BST)

print("\nจำนวนเต็มมากที่สุดจัดเก็บใน Binary search tree คือ :",BST.findMaximumValue())




