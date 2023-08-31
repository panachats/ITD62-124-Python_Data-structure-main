
#TODO สร้าง Class
class My_Queue():
    def __init__ (self,size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.count = 0
        self.sum = 0

#TODO สร้าง Method enqueue เพื่อส่งค่าเข้าไป
    def enqueue (self,_data):
        if self.rear == self.size - 1:
            print("Queue is full")
        else:
            if self.front == -1 and self.rear == -1:
                self.front = 0
                self.rear = 0
                self.queue[self.rear] = _data #TODO ทำการเอาค่าที่เราใส่เข้าไปมาแทนค่า None ที่ตำแหน่ง rear
            else:
                self.rear +=1
                self.queue[self.rear] = _data
            print("-"*25)

#TODO สร้าง Method dequeue เพื่อดึงค่าออก
    def dequeue (self):
        if self.front > self.size - 1:
            print("Queue is empty")
        else:
            self.queue[self.front] = None
            self.front += 1
        print("-"*25)

#TODO สร้าง Method display_All_Queue เพื่อแสดงค่าทั้งหมด
    def display_All_Queue (self):
        if self.rear == -1:
            print("Queue is empty")
        else:
            print("ข้อมูลใน Queue ทั้งหมด = ",self.queue)
        print("-"*25)

#TODO สร้าง Method display_Sum_Queue เพื่อแสดงผลรวม และ แสดงคจำนวนค่าที่มากกว่า 200
    def display_Sum_Queue(self):
        for i in self.queue:
            #TODO ถ้า type ใน element ของ queue เป็นตัวเลข
            if type(i) == int:
                if i > 200 :
                    self.count += 1
                self.sum = i + self.sum
        print("ผลรวม = ",self.sum)
        print("จำนวนตัวเลขใน Queue ที่มีมากกว่า 200 = ",self.count)
        print("front = ",queue.front,"rear = ",queue.rear)
        print("จบการทำงาน")
        
#TODO รับค่าขนาดของ list
size = int(input("โปรดระบุขนาดของ Queue : "))
#TODO วนลูปเพื่อตรวจสอบว่า size ที่ส่งมามีค่าน้อยกว่า 0 
while size <= 0:
    size = int(input("โปรดระบุขนาดของ Queue : "))

#TODO สร้างตัวแปรออบเจ็คจากคลาส เพื่อสำหรับส่งพารามิเตอร์เข้าไป
queue = My_Queue(size)

#TODO 
while True:
    print("โปรดระบุทางเลือกในการดำเนินการกับ Queue")
    print("1. รับข้อมูลจำนวนเต็มจัดเก็บใน Queue\n2. ดึงข้อมูลจาก Queue\n3. แสดงข้อมูลที่จัดเก็บทั้งหมดใน Queue")
    select = int(input("ทางเลือกในการดำเนินการ = "))
    
#TODO เข้าถึงสมาชิกภายในออบเจ็คจะใช้เครื่องหมายจุด
    if select == 1:
        queue.enqueue(int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Queue : ")))
    elif select == 2:
        queue.dequeue()
    elif select == 3:
        queue.display_All_Queue()
    else:
        queue.display_Sum_Queue()
        break
