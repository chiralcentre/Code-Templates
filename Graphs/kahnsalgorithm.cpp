#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef queue<int> qi;

/* preconditions:
1) graph must be directed acyclic
2) adjList is a list of lists representing the graph in adjaceny list form
3) indeg is a list of length V where indeg[v] represents the indegree of vertex v
postconditions:
1) indeg array is modified such that every entry is now 0
2) returns an list of vertices in topological order 
*/
vi kahnsAlgorithm(vvi adjList, vi indeg) {
    qi frontier;
    for (int i = 0; i < indeg.size(); i++) {
        if (indeg[i] == 0) frontier.push(i);
    }
    vi toposort;
    while (!frontier.empty()) {
        int u = frontier.front(); frontier.pop();
        toposort.push_back(u);
        for (int v: adjList[u]) {
            if (--indeg[v] == 0) frontier.push(v);
        }
    }
    return toposort;
}