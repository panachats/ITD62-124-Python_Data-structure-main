Collistion = 0
table_size = int(input("โปรดป้อนขนาดตารางแฮช"))
# กำหนดค่าให้ตารางแฮชมีขนาดเท่ากับ table_size และทุกช่องของตารางแฮชมีค่าเป็น None
hash_table = [None]*table_size
key = int(input("โปรดป้อนค่า (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป :")) 
data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตาราง :")
while True:
    if key < 0:
        break
    # ทำการ mod เก็บค่าใน address 
    address = key % table_size
    if hash_table[address] != None:
        print('จัดเก็บข้อมูลในตารางแฮชไม่ได้เพราะ Collistion',hash_table[address])
        # เพิ่มค่า collistion ไปเลื่อยๆ
        Collistion += 1
    else:
        hash_table[address] = data
    # รับค่า key
    key = int(input("โปรดป้อนค่า (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป :")) 
    # รับค่า data
    data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช :")

print("ข้อมูลที่จัดเก็บในตาราง")
# วนลูปตามจำนวน table_size
for i in range(table_size):
    if hash_table[i] == None:
        print("index {} ข้อมูลเท่ากับ {}".format(i,hash_table[i]))
    else:
        print("index {} ไม่มีข้อมูลจัดเก็บ".format(i))
print("จำนวนการชนที่เกิด Collistion",Collistion)