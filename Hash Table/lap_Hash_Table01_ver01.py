#สร้าง class
class Hash:
    def __init__(self,table_size):
        # กำหนดค่าให้ตารางแฮชมีขนาดเท่ากับ table_size และทุกช่องของตารางแฮชมีค่าเป็น None
        self.size = [None]*table_size
        self.collision = 0
        
    def append(self,address,data):
        if self.size[address] != None:
            print('จัดเก็บข้อมูลในตารางแฮชไม่ได้เพราะ Collistion',self.size[address])
            self.collision += 1
        else:
            self.size[address] = data

    def print_hash(self):
        for i in range(table_size):
            if self.size[i] == None:
                print("index {} ข้อมูลเท่ากับ {}".format(i,self.size[i]))
            else:
                print("index {} ไม่มีข้อมูลจัดเก็บ".format(i))
        print("จำนวนการชนที่เกิด Collistion",self.collision)

# กำหนดขนาดของตารางแฮชเป็นจำนวนเต็มจากค่าที่รับมาจากคีย์บอร์ด
table_size = int(input("โปรดป้อนขนาดตารางแฮช : "))
hash_table = Hash(table_size)
key = int(input("โปรดป้อนค่า (key) ที่มีค่าตั้วแต่ 0 ขึ้นไป : "))
data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตาราง :")

while key >= 0: 
    hash_table.append(key%table_size,data)
    key = int(input("โปรดป้อนค่า (key) ที่มีค่าตั้วแต่ 0 ขึ้นไป : "))
    data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช :")
hash_table.print_hash()




