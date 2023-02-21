"""
https://leetcode.com/problems/clone-graph/

2/20/2023
graphs
DFS - depth first search / hashmap
recursion

--- PROMPT ---
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

JUST CREATE AN EXACT CLONE...

--- LESSONS ---


--- QUESTIONS ---


--- PSEUDOCODE ---
Use hashmap, and DFS

NT connection
start somewhere.
Create a clone
  Map the old node, to new node
visit to neighbor - node
  clone neighbor
  map the old node, to new node
visit another neighbor - 
  clone neighbor
  map the old node, to new node
  check neighbor - since it sees it is already mapped,
  connect these two nodes
  

time: O(N) (Edges + Vertices)


"""
# --- MY SOLUTION ---
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # track the nodes visited
        oldToNew = {}

        def dfs(node):
            # check if node is already cloned. if it is, just return it
            if node in oldToNew: 
                return oldToNew[node]
            
            # create a copy of a node
            copy = Node(node.val)

            oldToNew[node] = copy

            # for each neighbor, run DFS, appending to copies
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        # return the copy. If node input is null, return null/none
        return dfs(node) if node else None



# --- TEST ---


# --- ALT SOLN by others ---
