
#! สร้าง Node
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

#! สร้าง linkList
class SLink_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #! สร้าง method สำหรับใส่ข้อมูลลงไปที่จุดเริ่มต้น
    def inseart_beginning(self,data):
        newNode = Node(data) #! สร้างโหนดใหม่
        if self.head == None :
            newNode.next = None #!set pointer เท่ากับ None
            self.head = newNode #! ให้ pointer head ไปอยู่ที่ Node ใหม่ที่สร้าง
            self.tail = newNode #! ให้ pointer tail ไปอยู่ที่ Node ใหม่ที่สร้าง

        else :
            newNode.next = self.head #! ให้ pointer Node ใหม่ที่ชี้ไปยังโหนดถัดไปให้ชี้ไปที่ pointer head ปัจจุบัน
            self.head = newNode #! set ให้ pointer head ไปอยู่ที่โหนดใหม่ที่สร้าง

    #! สร้าง method สำหรับใส่ข้อมูลลงไปที่จุดสิ้นสุด
    def inseart_end(self,data):
        newNode = Node(data) #! สร้างโหนดใหม่
        if self.head == None: 
            newNode.next = None #!set pointer เท่ากับ None
            self.head = newNode #! ให้ pointer head ไปอยู่ที่ Node ใหม่ที่สร้าง
            self.tail = newNode #! ให้ pointer tail ไปอยู่ที่ Node ใหม่ที่สร้าง

        else:
            newNode.next = None #!set pointer เท่ากับ None
            self.tail.next = newNode #! set ให้ pointer next ของ tail ในปัจจุบันไปชี้ที่โหนดใหม่
            self.tail = newNode #! set ให้ pointer tail ไปอยู่ที่โหนดใหม่ที่สร้าง

    #! สร้าง method สำหรับลบข้อมูลที่จุดเริ่มต้น
    def remove_beginning(self):
        if self.head is None:
            print("ไม่สามารถลบ Node ได้ เพราะ Node ว่าง")

        elif self.tail == self.head: #! ถ้า pointer head and pointer tail อยู่ที่เดียวกัน
            self.head = None #! ให้ pointer head มีค่าว่าง
            self.tail = None #! ให้ pointer tail มีค่าว่าง

        else:
            self.head = self.head.next #! set pointer head ที่โหนดปัจจุบันที่ลบไป ไปชี้ที่โหนดถัดไปของตัวที่ลบ

    #! สร้าง method สำหรับลบข้อมูลที่จุดเสิ้นสุด    
    def remove_end(self):
        if self.tail is None :
            print("ไม่สามารถลบโหนดได้เพราะโหนดว่าง")

        elif self.tail == self.head: #! ถ้า pointer head and pointer tail อยู่ที่เดียวกัน
            self.head = None #! ให้ pointer head มีค่าว่าง
            self.tail = None #! ให้ pointer tail มีค่าว่าง

        else:
            tmp = self.head #! set pointer tmp ให้ไปอยู่ที่โหนดแรก
            while tmp.next != self.tail: #! ถ้า pointer next ที่ชี้ไปยังโหนดถัดไปไม่เท่ากับ โหนดตัวสุดท้าย 
                tmp = tmp.next #! ให้ pointer tmp ขยับไปโหนดข้างหน้าเลื่อยๆ
            self.tail = tmp #! ให้ pointer tail ที่อยู่ที่โหนดปัจจุบัน เท่ากับ ตรงโหนดที่ tmp อยู่
            self.tail.next = None #! set ให้ pointer next ที่ชั้ไปที่โหนดใหม่ของ tail ให้เป็นค่าว่าง
  
    #! สร้าง method สำหรับลบข้อมูลที่ที่เราต้องการหา
    def remove_seard(self,data):
        if self.head is None:
            print("ไม่สามารถลบโหนดได้เพราะโหนดว่าง")

        else:
            tmp = self.head #! set pointer tmp ให้ไปอยู่ที่โหนดแรก
            prev = self.head #! set pointer prev ให้ไปอยู่ที่โหนดแรก
            if data == self.head.data: #! ถ้าข้อมูลเท่ากับข้อมูลตรงโหนดที่ pointer head ชี้ออยู่
                self.head = self.head.next #! set pointer head ที่โหนดปัจจุบันที่ลบไป ไปชี้ที่โหนดถัดไปของตัวที่ลบ

            elif self.tail.data == data: #! ถ้าข้อมูลเท่ากับข้อมูลตรงโหนดที่ pointer tail ชี้ออยู่
                self.remove_end() #! ให้ไปเรียกใช้ method ลบตัวสิ้นสุดของโหนด
                return

            while tmp.data != data: #! ถ้า ข้อมูลที่ pointer tmp ชี้อยู่ ไม่เท่ากับ ข้อมูลที่ต้องการหา 
                if self.tail == tmp and tmp.data != data:
                    return print("ไม่มีข้ออมูลในโหนด") #! ออกจาก func 
                prev = tmp #! set pointer prev ให้ไปออยู่ที่ Node เดียวกับ pointer tmp
                tmp = tmp.next #! ให้ pointer tmp ขยับไปโหนดข้างหน้าเลื่อยๆ
            prev.next = tmp.next #! ให้ pointer next ของ prev ชี้ไปยังโหนดที่ pointer next ของ tmp ชี้อยู่ ก็คือชี้ไปตัวโหนดที่อยู่ข้างหน้าของ pointer tmp

    #! สร้าง method สำหรับแสดง Head and Tail and all data 
    def display(self):
        if self.head is not None:
            tmp = self.head
            count = 1
            print("Head = {} Tail = {} ".format(self.head.data,self.tail.data))
            while tmp is not None :
                print("ข้อมูลที่ {} ข้อมูลที่เก็บ = {} ".format(count,tmp.data))
                tmp = tmp.next
                count += 1
        else:
            print("ไม่สามารถแสดงข้แมูลได้เพราะโหนดว่าง")

#! สร้างตัวแปรออบเจ็คจากคลาส เพื่อสำหรับส่งพารามิเตอร์เข้าไป
s = SLink_List()
way = 1
#! วนลูปถ้า way มีค่าตั้งแต่ 1 - 6 
while way> 0  and way < 7 :
    print("-"*45)
    print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list")
    print("กด 1 เพิ่มข้อมูลที่จุดเริ่มต้น Singly linked list")
    print("กด 2 เพิ่มข้อมูลที่จุดสิ้นสุด Singly linked list")
    print("กด 3 ลบข้อมูลที่จุดเริ่มต้น Singly linked list")
    print("กด 4 ลบข้อมูลที่จุดสิ้นสุด Singly linked list")
    print("กด 5 ลบข้อมูลที่ระบุจาก Singly linked list")
    print("กด 6 แสดงข้อมูลที่จัดเก็บทั้งหมดใน Singly linked list ทางจอภาพ")
    
    #! ส่งค่าเข้าไปตรวจสอบและวนลูปข้างบน
    way = int(input("ทางเลือกในการดำเนินการ : "))

    #! if way = 1 input data and call inseart_beginning
    if way == 1 :
        input_data = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดเริ่มต้น Singly linked list = "))
        s.inseart_beginning(input_data)

    #! if way = 2 input data and call inseart_end
    elif way == 2 :
        input_data = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดสิ้นสุด Singly linked list = "))
        s.inseart_end(input_data)
    
    #! if way = 3 remove_beginning
    elif way == 3:
        s.remove_beginning()

    #! if way = 4 remove_end
    elif way == 4:
        s.remove_end()
    
    #! if way = 5 input data and call remove_seard
    elif way == 5 :
        remove = int(input("ข้อมูลที่ต้องการลบออกจาก Singly linked list = "))
        s.remove_seard(remove)

    #! if way = 6  call display
    elif way == 6 :
        s.display()
    else:
        break