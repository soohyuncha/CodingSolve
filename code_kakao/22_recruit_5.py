# def solution(info, edges):
#     class Node:
#         def __init__(self, node_id):
#             self.node_id = node_id
#             self.left = None
#             self.right = None
#             self.animal = info[node_id]

#     def _add_node(node, parent_node_id, new_node_id):
#         if node is None:
#             return False
#         if node.node_id == parent_node_id:
#             if node.left is None:
#                 node.left = Node(new_node_id)
#                 return True
#             else:
#                 node.right = Node(new_node_id)
#                 return True
#         if _add_node(node.left, parent_node_id, new_node_id):
#             return True
#         if _add_node(node.right, parent_node_id, new_node_id):
#             return True
#         return False

#     def _initialize_cost(node):
#         if node is None:
#             return None
#         left_shortest_sheep = _initialize_cost(node.left)
#         right_shortest_sheep = _initialize_cost(node.right)
        
#         # Wolf
#         if info[node.node_id] == 1:
#             is_left_sheep = ((node.left is not None) and (info[node.left.node_id] == 0))
#             is_right_sheep = ((node.right is not None) and (info[node.right.node_id] == 0))
#             node.num_sheeps = is_left_sheep + is_right_sheep
#             if node.num_sheeps > 0:
#                 node.shortest_sheep = node.num_sheeps - 1
#             else:
#                 if (left_shortest_sheep is not None) and (right_shortest_sheep is not None):
#                     node.shortest_sheep = max(left_shortest_sheep, right_shortest_sheep) - 1
#                 elif (left_shortest_sheep is not None):
#                     node.shortest_sheep = left_shortest_sheep - 1
#                 elif (right_shortest_sheep is not None):
#                     node.shortest_sheep = right_shortest_sheep - 1
#                 else:
#                     node.shortest_sheep = None
#             #print(f'{node.node_id} {node.num_sheeps} {node.shortest_sheep}')
#             return node.shortest_sheep
#         else:
#             return 1
    
#     def _initialize_queue(node, queue):
#         if node is None:
#             return
#         if info[node.node_id] == 1 and (node.shortest_sheep is not None):
#             queue.append(node)
#             return
#         _initialize_queue(node.left, queue)
#         _initialize_queue(node.right, queue)
    
#     def _init_sheep(node):
#         if (node is None) or (info[node.node_id] == 1):
#             return 0
#         left = _init_sheep(node.left)
#         right = _init_sheep(node.right)
        
#         return left + right + 1
    
#     def _append_queue(node, queue):
#         if node is None:
#             return
#         if info[node.node_id] == 1 and (node.shortest_sheep is not None):
#             queue.append(node)
#             return
#         _append_queue(node.left, queue)
#         _append_queue(node.right, queue)

#     # Build tree
#     added_node = [0] * len(info)
#     root = Node(node_id=0)
#     added_node[0] = 1
#     while len(edges) > 0:
#         edge = edges.pop(0)
#         if added_node[edge[0]]:
#             _add_node(root, edge[0], edge[1])
#             added_node[edge[1]] = 1
#         else:
#             edges.append(edge)
    
#     # For "wolf" node, calculate (benefit, cost)
#     _initialize_cost(root)

#     # Sort each wolf node
#     queue = []
#     _initialize_queue(root, queue)
#     queue.sort(key=lambda x: (x.num_sheeps, x.shortest_sheep), reverse=True)

#     sheep, wolf = _init_sheep(root), 0

#     while len(queue) > 0:
#         q = queue[0]
#         if q.num_sheeps > 0:
#             node = queue.pop(0)
#             wolf += 1
#             if wolf >= sheep:
#                 break
#             sheep += node.num_sheeps
#             _append_queue(node.left, queue)
#             _append_queue(node.right, queue)
#         else:
#             node = queue.pop(0)
#             wolf += 1
#             if wolf >= sheep:
#                 break
#             _append_queue(node.left, queue)
#             _append_queue(node.right, queue)

#         queue.sort(key=lambda x: (x.num_sheeps, x.shortest_sheep), reverse=True)
#     answer = sheep
#     return answer

def solution(info, edges):
    def _find_nodes_to_visit(node, graph, visited, queue):
        if (node is None):
            return 
        # Case 1. Base case; Not visited
        if (visited[node] is not None) and (not visited[node]):
            return
        # Case 2. Not searched yet
        if visited[node] is None:
            queue.append(node)
            return
        # Case 3. For already visited nodes, search for children node
        for c in graph[node]:
            _find_nodes_to_visit(c, graph, visited, queue)

    def _bruteforce(graph, visited, wolf, sheep):
        queue = []
        _find_nodes_to_visit(0, graph, visited, queue)
        #print(queue, visited, sheep)
        if len(queue) == 0:
            return sheep
        
        sheep_max = sheep
        for node in queue:
            sheep_1, sheep_2 = sheep, sheep
            # Case 1. Not visit the node; For sheep, we always visit the node
            if info[node] == 1:
                visited[node] = False
                sheep_1 = _bruteforce(graph, visited, wolf, sheep)
            
            # Case 2. Visit the node
            if (info[node] == 0) or ((info[node] == 1) and (sheep - wolf > 1)):
                #print(node)
                visited[node] = True
                # Sheep
                if info[node] == 0:
                    sheep_2 = _bruteforce(graph, visited, wolf, sheep + 1)
                # Wolf
                else:
                    sheep_2 = _bruteforce(graph, visited, wolf + 1, sheep)
        
            visited[node] = None
            sheep_max = max(sheep_max, max(sheep_1, sheep_2))
        return sheep_max
    
    # Create graph
    graph = {}
    for i in range(len(info)):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])

    # Initialize visit by dfs; free "0" should be necessarily visited
    visited = [None] * len(info)
    visited[0] = True
    
    # Bruteforce search
    answer = _bruteforce(graph, visited, wolf=0, sheep=1)
    return answer

if __name__ == '__main__':
    info, edges = [0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    #info, edges = [0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    ans = solution(info, edges)
    print(ans)