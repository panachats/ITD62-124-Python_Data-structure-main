table_size = int(input("โปรดป้อนขนาดตารางแฮช"))
hash_table = [None]*table_size
count = 1
while True:
    # รับค่า key
    key = int(input("โปรดป้อนค่า (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป :")) 
    # รับค่า data
    data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช :")

    if key < 0:
        break
    else:
        # Hash 1
        # ทำการ mod เก็บค่าใน address
        address = key%table_size
        if hash_table[address] != None:
            while True:
                address = (key + count)%table_size
                if hash_table[address] != None:
                    count += 1
                else:
                    hash_table[address] = data
                    print("Address =",address)
                    break
        else:
            hash_table[address] = data
            print("Address =",address)

# วนลูปตามจำนวน table_size        
for x in range(table_size):
    if hash_table[x] != None:
        print("Address = {} ข้อมูลที่จัดเก็บ {}".format(x,hash_table[x]))
    else:
        print("Address = {} ไม่มีข้อมูลจัดเก็บ".format(x))
