def get_node_from_reversed_graph(graph,node):
    list_node=[]
    for node_g in graph:
        if node in graph[node_g]:
            list_node.append(node_g)
    return list_node

def dfs(graph,node,finished_order,viewed):
    viewed.append(node)
    for child_node in get_node_from_reversed_graph(graph,node):
        if child_node not in viewed:
            dfs(graph,child_node,finished_order,viewed)
    finished_order.insert(0,node)
    
def dfs_sub(graph,node,connected,viewed):
    viewed.append(node)
    connected.append(node)
    for child_node in graph[node]:
        if child_node not in viewed:
            dfs_sub(graph,child_node,connected,viewed)
    

def compute_strongly_connected_component(graph):
    viewed=[]
    finished_order=[]
    list_of_conencted_component=[]
    for node in graph:
        if node not in viewed:
            dfs(graph,node,finished_order,viewed)
    viewed=[]
    for node in finished_order:
        if node not in viewed:
            connected=[]
            dfs_sub(graph,node,connected,viewed)
            list_of_conencted_component.append(connected)
    return list_of_conencted_component
      
graph={1:[4],
       2:[8],
       3:[6],
       4:[7],
       5:[2],
       6:[9],
       7:[1],
       8:[6,5],
       9:[7,3]
}
print(compute_strongly_connected_component(graph))