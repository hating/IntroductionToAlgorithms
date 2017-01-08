class Vertex:
    def __init__(self, key, adjacent):
        self.key = key
        self.adjacent = adjacent


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

    def BDFS(self, s, t):
        OPEN = []
        CLOSE = []
        OPEN.append(self.node[s])
        self.Recursion(OPEN, CLOSE, t)
        return CLOSE

    def Recursion(self, OPEN, CLOSE, s):
        if len(OPEN) == 0:
            return
        i = OPEN.pop(0)
        CLOSE.append(i)
        for j in i.adjacent:
            isUndiscover = True
            for k  in OPEN:
                if j[0] == k:
                    isUndiscover = False
            for k in CLOSE:
                if j[0] == k:
                    isUndiscover = False
            if (isUndiscover):
                if s == "BFS":
                    OPEN.append(j[0])
                elif s == "DFS":
                    OPEN.insert(0, j[0])
        self.Recursion(OPEN, CLOSE,s)


G = Graph()
G.AddVertex("H")
G.AddVertex("I")
G.AddVertex("J")
G.AddVertex("K")
G.AddVertex("L")
G.AddVertex("M")
G.AddVertex("N")
G.AddVertex("O")
G.AddVertex("D", ["H", "I"])
G.AddVertex("E", ["J", "K"])
G.AddVertex("F", ["L", "M"])
G.AddVertex("G", ["N", "O"])
G.AddVertex("B", ["D", "E"])
G.AddVertex("C", ["F", "G"])
G.AddVertex("A", ["B", "C"])
LIST = G.BDFS("A", "BFS")
print [i.key for i in LIST]
LIST = G.BDFS("A", "DFS")
print [i.key for i in LIST]
