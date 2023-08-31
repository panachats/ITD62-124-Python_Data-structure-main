
#! สร้าง class Node
class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    #! สร้าง method สำหรับใส่ข้อมูลลง
    def insert(self,info):
        if info != " ":
            self.data = info
        else:
            return
        
        print("ใส่ข้อมูลลงใน leftChild ของ {} (ถ้าไม่มีให้ใส้ค่าช่องว่าง)".format(self.data))
        info = input()
        if info != " ":
            self.leftChild = Node() #! สร้างโหนดที่ด้านซ้าย
            self.leftChild.insert(info) #! วนกลับไปรับข้อมูลอีกครั้ง

        print("ใส่ข้อมูลลงใน rightChild ของ {} (ถ้าไม่มีให้ใส้ค่าช่องว่าง)".format(self.data))
        info = input()
        if info != " ":
            self.rightChild = Node() #! สร้างโหนดที่ด้านขวา
            self.rightChild.insert(info) #! วนกลับไปรับข้อมูลอีกครั้ง

    #! สร้าง method สำหรับแสดงข้อมูลของ InOrder
    def InOrder(self,tree):
        #! ตรวจสอบว่าเป็นค่าว่างไหม
        if tree is not None:
            self.InOrder(tree.leftChild)
            print(tree.data)
            self.InOrder(tree.rightChild)

    #! สร้าง method สำหรับแสดงข้อมูลของ PostOder
    def PostOrder(self,tree):
        #! ตรวจสอบว่าเป็นค่าว่างไหม
        if tree is not None:
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            #! ให้แสดงคำเฉพาะที่ขึ้นต้นด้วย a e i o u
            if tree.data.startswith("a") or tree.data.startswith("e") or tree.data.startswith("i") or tree.data.startswith("o") or tree.data.startswith("u"):
                print(tree.data)

#! รับค่า data
input_data = input("โปรดป้อนข้อความเพื่อจัดเก็บที่ Root node : ")          
#! สร้างตัวแปรออบเจ็คจากคลาส เพื่อสำหรับส่งพารามิเตอร์เข้าไป  
binary_tree = Node()
#! ส่ง Data เข้าไปใน insert
binary_tree.insert(input_data)
print("ผลลัพธ์จากการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ In-order : ")
#! ส่งค่าให้ไปแสดงแบบ InOder
binary_tree.InOrder(binary_tree)
print("ผลลัพธ์จากการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ Post-order โดยแสดงข้อความที่จัดเก็บในแต่ละโหนดที่ขึ้นต้นด้วย a,e,i,o,u : ")
#! ส่งค่าให้ไปแสดงแบบ PostOder
binary_tree.PostOrder(binary_tree)