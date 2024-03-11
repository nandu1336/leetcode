from typing import List , Optional

'''
    Though this program hasn't be tested in local and is a little tricky to even try, this is tested in leet code and 
    beat 79.51% of submissions.
'''
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        visited = set()
        

        def create_nodes(node):
            if node and not node in node_map: 
                newnode = Node(node.val)
                node_map[node] = newnode

                for neighbor in node.neighbors:
                    create_nodes(neighbor)

        def connect_nodes(node):
            if node and node not in visited:
                visited.add(node)
                clone = node_map[node]

                for neighbor in node.neighbors:
                    clone.neighbors.append(node_map[neighbor])
                
                for neighbor in node.neighbors:
                    connect_nodes(neighbor)
        
        create_nodes(node)
        connect_nodes(node)

        for node in node_map.values():
            return node
