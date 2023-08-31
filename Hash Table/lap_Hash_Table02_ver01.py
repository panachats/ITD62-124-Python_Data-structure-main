class Hash:
    def __init__(self,table_size):
        self.size = [None]*table_size
        
    def Hash_append(self,key,data): 
        address = key % table_size
        if self.size[address] == None:
            self.size[address] = data
            print("Address = ",address)
        else:
            count = 0
            while True:
                address = (key + count)%table_size
                if self.size[address]!= None:
                    count += 1
                else:
                    self.size[address] = data
                    print("Address = ",address)
                    break
    def print_hash(self):
        for x in range(table_size):
            if self.size[x] != None:
                print("Address = {} ข้อมูลที่จัดเก็บ {}".format(x,self.size[x]))
            else:
                print("Address = {} ไม่มีข้อมูลจัดเก็บ".format(x))

table_size = int(input("โปรดป้อนขนาดตารางแฮช : "))
hash_table = Hash(table_size)
while True :
    key = int(input("โปรดป้อนค่า (key) ที่มีค่าตั้วแต่ 0 ขึ้นไป : "))
    data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช :")
    if key < 0:
        break
    else:
        hash_table.Hash_append(key,data)
hash_table.print_hash()



