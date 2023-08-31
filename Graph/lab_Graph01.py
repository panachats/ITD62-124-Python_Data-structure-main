import math 

# การสร้างคลาส queue เพื่อใช้ใน BFS 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

# การสร้างคลาส Vertex 
class Vertex:
    def __init__(self,data):
        self.id = data
        self.distance = math.inf
        self.color = 'white'
        self.pred = None
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        '''
        Adds a connection from this vertex to another
        
        :param nbr: The new neighbor
        :param weight: The weight of the edge from this vertex to the vertex passed in as an argument,
        defaults to 0 (optional)
        '''
        self.connectedTo[nbr] = weight

    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        '''
        It sets the distance.
        
        :param d: the distance between the two points
        '''
        self.distance = d

    def setPred(self,p):
        '''
        It sets the predecessor of the node to the given node.
        
        :param p: the parent node
        '''
        self.pred = p

    def getConnections(self):
        '''
        Return a list of all the connections that this vertex has
        :return: A list of all the vertices that the vertex is connected to.
        '''
        return self.connectedTo.keys()

    def getId(self):
        '''
        Get the id of the object
        :return: The id of the object.
        '''
        return self.id

    def getPred(self):
        '''
        Get the prediction of the model
        :return: The predicted value.
        '''
        return self.pred

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

# การสร้างคลาส Graph
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self,n):
        # ตรวจสอบว่า n อยู่ในกราฟหรือไม่
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices

    def addEdge(self,f,t):
        # ถ้าหากว่าค่าที่รับเข้ามาเป็นค่าที่ไม่มีในคลาสก็จะทำการเพิ่มค่านั้นเข้าไปในคลาสด้วย
        # ตรวจสอบว่าได้ใส่ตัวที่ไม่ได้อยู่ใน vertex นั้นไหม
        if f not in self.vertices: 
            nv = self.addVertex(f)
        # ตรวจสอบว่าได้ใส่ตัวที่ไม่ได้อยู่ใน vertex นั้นไหม
        if t not in self.vertices: 
            nv = self.addVertex(t)
        # add f,t เข้าไปที่ Neighbor
        self.vertices[f].addNeighbor(self.vertices[t])

    def getVertices(self):
        # แสดงรายการทั้งหมดในกราฟ และ return
        return list(self.vertices.keys())

    # ฟังก์ชันนี้ถูกเรียกเมื่อจำเป็นต้องมีตัววนซ้ำสำหรับคอนเทนเนอร์
    def __iter__(self):
        return iter(self.vertices.values())

# ประกาศ method ชื่อ bfs เพื่อท่องไปในกราฟด้วยขั้นตอนวิธีแบบ BFS 
    def bfs(self,start):
        # จุดเริ่มต้น
        s = self.getVertex(start) 
        s.setDistance(0)
        s.setPred(None)
        q = Queue() # สร้างคิวว่าง
        q.enqueue(s) # เอา s ใส่เข้าไปในคิว เพื่อแสดงว่าจะเริ่มทำตัว s
        while not(q.isEmpty()):
            currentVertex = q.dequeue()
            for nbr in currentVertex.getConnections(): # หาว่าจะสามารถไปทางไหนได้บ้าง
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray') # เปลี่ยนเป็นสีเทาแสดงถึงว่ากำลังวางแผนจะไป
                    nbr.setDistance(currentVertex.getDistance() + 1) # ให้บวกระยะทาง 
                    nbr.setPred(currentVertex) # set ให้ตัวก่อนหน้าเป็ย nbr
                    q.enqueue(nbr)
                    print("ระยะทางทีสั่นที่สุดจากจุดเริ่มต้นในการท่องไปในกราฟไปยังจุด ",nbr.getId(), ' = ',nbr.getDistance())
            currentVertex.setColor('black') # set ให้ตัวก่อนหน้าเป็นสีดำ เพราะได้ผ่านมาแล้ว

# ประกาศ object ชื่อ g ให้มีชนิดเป็นคลาส Graph
g = Graph()
round = int(input("โปรดระบุจำนวนจุดในกราฟ : "))
for i in range(round):
    putGrap = input("โปรดระบุชื่อ vertex :")
    g.addVertex(putGrap)

print("โปรดระบุชื่อจุดที่เป็น source และ destination ของเส้นเชื่อม")
front = input("score = ")
tail = input("destination = ")
while True:
    print("โปรดระบุชื่อจุดที่เป็น source และ destination ของเส้นเชื่อม")
    g.addEdge(front,tail) 
    front = input("ชื่อจุดที่เป็น source = ")
    if front != "-":
        tail = input("ชื่อจุดที่เป็น destination = ") 
    else:
        break      
    
print("โปรดระบบชื่อจุดเริ่มต้นในการท่องไปในกราฟด้วยขั้นตอนวิธีแบบ Breadth-first Search")
eggGraph = input("ชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟ : ")
g.bfs(eggGraph)