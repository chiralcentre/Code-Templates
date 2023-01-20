from heapq import heappush,heappop

INF = 1000000000 #use 1 billion to represent infinity
def modifiedDjikstra(adjList,s,e):
    D = [INF for _ in range(N)]; D[s] = 0
    PQ = []; heappush(PQ,(0,s))
    while PQ: #modified Djikstra's is used with O(M log M) time complexity
        d,u = heappop(PQ)
        if u == e:
            return d
        if d == D[u]: # check if this is the superior copy
            for v,w in adjList[u]:
                if D[v] > D[u] + w: # can relax
                    D[v] = D[u] + w
                    heappush(PQ,(D[v],v))
    return -1