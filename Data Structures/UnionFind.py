class UnionFind:
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]
        self.numSets = N

    def findSet(self,j):
        if self.p[j] == j:
            return j
        else:
            self.p[j] = self.findSet(self.p[j])
            return self.p[j]

    def isSameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self,i,j):
        if not self.isSameSet(i,j):
            x,y = self.findSet(i),self.findSet(j)
            # invariant: rank(x) <= rank(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.setSize[y] += self.setSize[x]
            self.numSets -= 1

    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]