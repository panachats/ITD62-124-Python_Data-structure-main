def ShellSort(n,myArr):
    # กำหนดให้ flag มีค่าเป็น 1 ถ้ามีการเปลี่ยนแปลงค่าจะเป็น 0 ก็จะไม่เปลี่ยนแปลงค่าจะเป็น 1 เช็คค่าว่ามีการทำงานแล้วหรือยัง
    flag = 1
    #เป็นตัวแปรที่เช็คขนาดของ colume
    gap_size = n 
    # เข้า loop เมื่อ ค่า flag เท่ากับ 1 หรือ gap_size > 1
    while flag == 1 or gap_size > 1:
        flag = 0
        gap_size = int((gap_size + 1) / 2)
        for i in range(n - gap_size):
            if myArr[i + gap_size] < myArr[i]:
                temp = myArr[i + gap_size]
                myArr[i + gap_size] = myArr[i]
                myArr[i] = temp
                flag = 0

    print("ข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ")
    #print ค่า ออกมาเป๋นแนสนอนทีละตัว
    for j in arr:
        print(j,end=" ")

n = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))

arr = [] 
print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")

#วนลูปตามจำนวน รอบที่รับ
arr = [(input('Enter you : ')) for y in range(n)]
print("ข้อมูลก่อนเรียงลำดับคือ")

#print ค่า ออกมาเป๋นแนสนอนทีละตัว
for y in arr:
    print(y,end=' ')
print("\n")
ShellSort(n,arr)

