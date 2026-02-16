#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void topologicalSort(int V, vector<vector<int>>& adj) {
    vector<int> indegree(V, 0);

    // Calculate in-degrees of all vertices
    for (int i = 0; i < V; i++) {
        for (int neighbor : adj[i]) {
            indegree[neighbor]++;
        }
    }

    queue<int> q;

    // Add all vertices with indegree 0 to queue
    for (int i = 0; i < V; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    vector<int> topoOrder;

    // Process the queue
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        topoOrder.push_back(node);

        for (int neighbor : adj[node]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    // Check for cycle
    if (topoOrder.size() != V) {
        cout << "Graph has a cycle. Topological sort not possible.\n";
        return;
    }

    cout << "Topological Order: ";
    for (int node : topoOrder) {
        cout << node << " ";
    }
    cout << endl;
}

int main() {
    int V, E;
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;

    vector<vector<int>> adj(V);

    cout << "Enter edges (u v) meaning u -> v:\n";
    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    topologicalSort(V, adj);

    return 0;
}
