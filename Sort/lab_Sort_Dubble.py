# สร้างฟังก์ชั่น bubbleSort
def bubbleSort(arr):
    #วนลูปตามรอบใน list
    for i in range(len(arr)-1):
        #print("Pass",i)
        # การวนลูปตามรอบของ list จะวนลูปตามจำนวนข้อมูลที่มีทั้งหมด เพื่อให้สามารถเปรียบเทียบข้อมูลที่มีตำแหน่งต่างกัน
        for x in range(len(arr)-i-1):
            # เปรียบเทียบค่ากัน
            if arr[x] > arr[x + 1]:
                temp = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = temp
    print("ข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ")
    #print ค่า ออกมาเป๋นแนสนอนทีละตัว
    for j in arr:
        print(j,end=" ")

#รับค่าขนาดข้อมูล
n = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))
#สร้าง list ว่าง
arr = [] 
print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")
#วนลูปตามจำนวน รอบที่รับ
arr = [int(input('Enter you : ')) for y in range(n)]
print("ข้อมูลก่อนเรียงลำดับคือ")
#print ค่า ออกมาเป๋นแนสนอนทีละตัว
for y in arr:
    print(y,end=' ')
print("\n")
bubbleSort(arr)