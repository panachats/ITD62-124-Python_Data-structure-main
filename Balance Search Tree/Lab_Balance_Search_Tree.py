#การประกาศคลาส Node
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

#การประกาศคลาส AVL tree
class AVL_Tree():
#การประกาศเมทอด getHeight()
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

#การประกาศเมทอด getBalance()
    def getBalance(self, root):
        if not root:
            return 0
        # ห่ค่าต่างกันของ
        return self.getHeight(root.left) - self.getHeight(root.right)

#การประกาศเมทอด leftRotate()

    def leftRotate(self, z):
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

#การประกาศเมทอด rightRotate()
    def rightRotate(self, z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

#การประกาศเมทอด nsert()
# การใส่ข้อมูล
    def insert(self, root, key):        
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)      
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)
        return root

    # การท่องไปในแบบ PreOrder
    def PreOrder(self, tree):
        if tree:
            print(tree.data, end = '  ')
            self.PreOrder(tree.left)
            self.PreOrder(tree.right)

Tree = AVL_Tree()
rt = None
# วนลูปรับค่าและส่งค่าจนกว่าจะกดเลข 9999
while True:
    # รับค่า data
    number = int(input("โปรดป้อนจำนวณเต็มเพื่อสร้าง AVL tree : "))
    if number != 9999:
        rt = Tree.insert(rt, number)
    else :
        break
        
#ส่งค่าไปใน PreOrder
print("ผลลัพธ์จากการท่องไปใน AVL tree ด้วยขันตอนวิธีเเบบ Pre-order")
Tree.PreOrder(rt)