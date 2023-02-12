"""
https://leetcode.com/problems/find-center-of-star-graph/

2/10/2023

--- PROMPT ---
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---
        input: list of lists

        Every value is unique!!

        Figure out the len of the list

        iterate thru the lists, and populate a dictionary with the counter for each number

        Return the key associated with the value that matches the size of list

        output: value that is shared in that list

"""
# --- MY SOLUTION ---
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        dsoln = {}

        n = len(edges)

        for items in edges:
            for elem in items:
                if elem not in dsoln:
                    dsoln[elem] = 1
                else:
                    dsoln[elem] += 1
        
        for key,value in dsoln.items():
            if value == n:
                return key


# --- TEST ---


# --- ALT SOLN by others ---
