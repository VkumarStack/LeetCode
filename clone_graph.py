from collections import deque
"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        # List containing copies of the nodes
        nodes = {}
        self.__cloneGraphHelper(node, nodes)
        # Return the copy of the first node
        return nodes[1]

    def __cloneGraphHelper(self, node : 'Node', nodes) -> 'Node':
        # Perform a depth-first search
        if node.val in nodes:
            return nodes[node.val]
        # Copy the node, initializing an empty neighbor list
        nodes[node.val] = Node(node.val, [])
        # Recurse through each of the neighbors, returning its copy 
        for neighbor in node.neighbors:
            nd = self.__cloneGraphHelper(neighbor, nodes)
            # Put the returned copy into the neighbor list; this will work in both ways since the neighbor will have already found
            # the current node and put it in its own neighbor list
            nd.neighbors.append(nodes[node.val])
        return nodes[node.val]

            

        


