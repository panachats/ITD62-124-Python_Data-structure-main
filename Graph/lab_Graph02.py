class Graph:
    def __init__(self,vertices):
        self.V = vertices
         # self.graph เป็นการจัดเก็บข้อมูลเส้นเชื่อมด้วย list ของเส้นเชื่อมที่มี 3 ค่า คือ u,v,w โดย u คือ source, v คือ destination, w คือ weight
        self.graph = []
       
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w]) #เมื่อมีการเพิ่มเส้นเชื่อมจะมีการเพิ่มข้อมูลใน List
    
    # การประกาศ method ชื่อ find_set
    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    # การประกาศ method ชื่อ union
    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y 
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1

    # Kruskal
    def kruskal(self):
        A = []
        self.graph = sorted(self.graph, key= lambda item: item[2])
        parent = []
        rank =[]
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        i = 0
        e = 0
        sum = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent,u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)   
            print("เส้นเชื่อมระหว่างจุด",u,"กับจุด",v,"มีค่าน้ำหนัก = ",w)
            sum += w #แล้วก็บวกเพิ่มค่าของค่า w ในตัวแปร sum 
        print("Weight รวมของ Minninum spanning tree คือ",sum)

        
        '''
         #มาทำการลูปแสดงค่า u, v, w ใน A ออกมา
            for u,v,w in A: 
                print("เส้นเชื่อมระหว่างจุด",u,"กับจุด",v,"มีค่าน้ำหนัก = ",w)
                sum += w #แล้วก็บวกเพิ่มค่าของค่า w ในตัวแปร sum 
        print("Weight รวมของ Minninum spanning tree คือ",sum)
        '''

           

# รับค่า input_N เพื่อส่งไปที่ self.V = vertices ใน init
input_N = int(input("โปรดระบุค่าตัวแปร input_N (จำนวนจุดในกราฟแบบไม่มีทิศทาง (undirectef graph)) : "))
g = Graph(input_N)

# รับค่า input_Edge เพื่อนำไปใช้กับ loop 
input_Edge = int(input("โปรดระบุจำนวนเส้นเชื่อม (Edge) ในกราฟแบบไม่มีทิศทาง : ")) #กำหนดการวนลูป
print("โปรดระบุชื่อจุดที่เป็น Source ชื่อจุดที่เป็น Destination และค่าน้ำหนัก (Weight) ของเส้นเชื่อในกราฟ")

#วนลูปตามรอบ input_Edge
for i in range(input_Edge):
        Source = int(input("Source = "))
        Destination = int(input("Destination = "))
        Weight = int(input("Weight = "))
        # ส่งค่าไปที่ addEdge
        g.addEdge(Source,Destination,Weight)

#เรียกใช้ kruskal
g.kruskal()


