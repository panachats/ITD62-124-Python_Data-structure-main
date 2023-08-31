class Stack:
    # เป็นฟังก์ชั่นเริ่มต้นการทำงานเมื่อมีการเรียกใช้ method ใน class
    def __init__(self,size):
        self.size = size
        self.stack = [] * size
    
    # สร้าง method สำหรับตรวจสอบว่าค่าใน list ว่างไหม
    def is_empty(self):
        return self.stack == []

    # สร้าง method สำหรับตรวจสอบว่าค่าใน list มีขนาดเต็มรึยัง
    def is_full (self):
        return len(self.stack) == self.size

    # สร้าง method สำหรับนเข้าข้อมูลใส่เข้าไป
    # และเรียกใช้ method is_full ว่าตรวจสอบว่ามีข้อมูลเต็มหรือไหม
    def push(self, data):
        if self.is_full():
            print("Stack is Full")
        self.stack.append(data)

    # สร้าง method สำหรับนนำข้อมูล
    # และเรียกใช้ method is_empty ว่าตรวจสอบว่าในlist มีค่าว่างไหม
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        self.stack.pop()

    # สร้าง method สำหรับelement ตัวล่าสุดใน stack
    # และเรียกใช้ method is_empty ว่าตรวจสอบว่าในlist มีค่าว่างไหม
    def top(self):
        if self.is_empty():
            print("Stack is Empty")
        return self.stack[-1]

    # สร้าง method สำหรับเรียกดูข้อมูลทั้งหมดใน stack
    # และเรียกใช้ method is_empty ว่าตรวจสอบว่าในlist มีค่าว่างไหม
    def allStack(self):
        if self.is_empty():
            print("Stack is Empty")
        self.stack

#รับค่าทาง keybord แบบ int 
size = int(input("โปรดระบุขนาด Stack ที่เป็นจำนวนเต็มที่มากกว่า 0 : "))

#มาวนลูปตรวจสอบว่า size ที่เรารับมามีค่าน้อยกว่าหรือเท่กับ 0 ไหม
while size <= 0:
    size = int(input("โปรดระบุขนาด Stack ที่เป็นจำนวนเต็มที่มากกว่า 0 : "))

# สร้างตัวแปรออบเจ็คจากคลาส เพื่อสำหรับส่งพารามิเตอร์เข้าไป
Mystack = Stack(size)

x = 1
# วนลูป 4 รอบ พร้อมรับค่าทางเลือก และตรวจสอบค่าทางเลือก
while x > 0 and x <= 4:
    print('-'*25)
    print("โปรดระบุทางเลือกในการดำเนินการของ Stack ")
    print("1.Push\n2.Pop\n3.Top of Stack\n4.Display ข้อมูลที่จัดเก็บ ")
    way = int(input("ทางเลือกในการดำเนินการ "))

# เข้าถึงสมาชิกภายในออบเจ็คจะใช้เครื่องหมายจุด
    if way == 1:
        Mystack.push(int(input("ข้อมูลที่ต้องการจัดเก็บ : ")))
    elif way == 2:
        Mystack.pop()
    elif way == 3:
        print("ค่าTop of Stack : ",Mystack.top())
    elif way == 4:
        print("ข้อมูลที่จัดเก็บทั้งหมด : ",Mystack.allStack())
        print("ค่าที่มากที่สุด : ",max(Mystack.stack))
        print("ค่าที่น้อยที่สุด : ",min(Mystack.stack))
        print("ค่าเฉลี่ย : ",sum(Mystack.stack)/len(Mystack.stack)) #หาค่าเฉลี่ย
    else:
        break










