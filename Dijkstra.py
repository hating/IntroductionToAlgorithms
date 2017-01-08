class Vertex:
    def __init__(self, key, adjacent):
        self.key = key
        self.adjacent = adjacent
        self.prev = None


class Graph:
    def __init__(self):
        self.node = {}

    def AddVertex(self, key, adjance=[], rank=[]):
        A = []
        if rank == []:
            rank = [1 for i in range(0, len(adjance))]
        for i in range(0, len(adjance)):
            A.append((self.node[adjance[i]], rank[i]))

        self.node[key] = Vertex(key, A)

    def AddEdge(self, u, v, r):
        for i in self.node[u].adjacent:
            if i[0].key == v:
                return False
        self.node[u].adjacent.append((self.node[v], r))

    def Dijkstra(self, s, e):
        OPEN = []
        CLOSE = []
        OPEN.append((self.node[s], 0))
        self.Recursion(OPEN, CLOSE, e)
        RET = []
        i = self.node[e]
        while i != None:
            RET.append(i)
            i = i.prev
        RET.reverse()
        return RET

    def Contains(self, list, e):
        for i in list:
            if i[0] == e:
                return i
        return False

    def Recursion(self, OPEN, CLOSE, e):
        if self.Contains(CLOSE, e):
            return
        if len(OPEN) == 0:
            return
        i = OPEN.pop(0)
        CLOSE.append(i)
        for j in i[0].adjacent:
            if self.Contains(CLOSE, j[0]):
                continue
            con = self.Contains(OPEN, j[0])
            if con:
                if con[1] > i[1] + j[1]:
                    OPEN.remove(con)
                else:
                    continue
            j[0].prev = i[0]
            rank = i[1] + j[1]
            OPEN.append((j[0], rank))
        OPEN.sort(lambda x, y: cmp(x[1], y[1]))
        self.Recursion(OPEN, CLOSE, e)


G = Graph()
G.AddVertex("s")
G.AddVertex("t")
G.AddVertex("x")
G.AddVertex("y")
G.AddVertex("z")
G.AddEdge("s", "t", 10)
G.AddEdge("s", "y", 5)
G.AddEdge("t", "x", 1)
G.AddEdge("t", "y", 2)
G.AddEdge("x", "z", 4)
G.AddEdge("y", "t", 3)
G.AddEdge("y", "x", 9)
G.AddEdge("y", "z", 2)
G.AddEdge("z", "s", 7)
G.AddEdge("z", "x", 6)
path = G.Dijkstra("s", "x")
print [i.key for i in path]
print "DEBUG"
