# Write a Python program to solve the Travelling Salesperson Problem using the branch and bound technique.
import math
def tsp_branch_and_bound(graph):
    n = len(graph)
    visited = [False] * n
    min_cost = [math.inf]
    best_path = []
    def bound(cost, level):
        return cost
    def tsp_util(curr, count, cost, path):
        if count == n and graph[curr][0] > 0:
            total_cost = cost + graph[curr][0]
            if total_cost < min_cost[0]:
                min_cost[0] = total_cost
                best_path.clear()
                best_path.extend(path + [0])
            return
        for i in range(n):
            if not visited[i] and graph[curr][i] > 0:
                temp_cost = cost + graph[curr][i]
                if bound(temp_cost, count + 1) < min_cost[0]:
                    visited[i] = True
                    tsp_util(i, count + 1, temp_cost, path + [i])
                    visited[i] = False
    visited[0] = True
    tsp_util(0, 1, 0, [0])
    return min_cost[0], best_path
n = int(input("Enter number of cities: "))
graph = []
print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))
cost, path = tsp_branch_and_bound(graph)
print("Minimum travel cost:", cost)
print("Path:", " -> ".join(map(str, path)))