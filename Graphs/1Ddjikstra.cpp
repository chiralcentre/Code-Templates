#include <bits/stdc++.h>
#include <queue>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vii> vvii;

const int INF = 1000000000;

double modifiedDjikstra(vvii &adjList, int N, int s, int e) {
    vi D(N,INF); D[s] = 0;
    priority_queue<ii,vii,greater<ii>> pq;
    pq.emplace(0,s);
    while (!pq.empty()) {
        auto [d,u] = pq.top(); pq.pop();
        if (u == e) return d;
        if (d == D[u]) {
            for (auto &[v,w]: adjList[u]) {
                if (D[v] > D[u] + w) {
                    D[v] = D[u] + w;
                    pq.emplace(D[v],v);
                }
            }
        }
    }
    return - 1;
}