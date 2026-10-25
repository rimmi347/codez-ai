
adj_list = {
    "A" :["B", "C"],
    "B" :["D", "E"],
    "C" :["B", "F"],
    "D" :[ ],
    "E" :["F"],
    "F" :[],
   
}
color = {}
parent = {}
trav_time = {}
dfs_traversal_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]

visited = {}
level = {}
parent = {}
dfs_traversal_output = []

for node in adj_list.keys():
    visited[node] = False
    parent[node]  = None
    level[node]   = -1

time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v]  = u
            dfs_util(v)

    color[u] = "B"  
    trav_time[u][1] = time    
    time += 1
for u in adj_list.keys():
    if color[u] == "W":
        dfs_util(u)
dfs_util("A")
print(dfs_traversal_output)
print(parent)
print(trav_time)


