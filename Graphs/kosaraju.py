from sys import stdin,stdout,setrecursionlimit

setrecursionlimit(pow(10,6))

#assume visited,rToposort,adjList,transpose arrays are constructed already

#perform DFS topological sort
def DFSrec(u):
    global adjList,rToposort
    visited[u] = True
    for v in adjList[u]:
        if not visited[v]:
            DFSrec(v)
    rToposort.append(u)

#perform Kosaraju's algorithm to label every SCC
def kosaraju(n):
    global visited,rToposort,adjList,transpose
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFSrec(i)
    labels = [0 for _ in range(n)]; SCC = 0
    for i in range(len(rToposort) - 1, -1, -1):
        if labels[rToposort[i]] == 0:
            SCC += 1
            frontier = [rToposort[i]]
            labels[rToposort[i]] = SCC
            while frontier:
                u = frontier.pop()
                for v in transpose[u]:
                    if not labels[v]:
                        labels[v] = SCC
                        frontier.append(v)
    return labels,SCC
