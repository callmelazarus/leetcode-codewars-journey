"""
https://leetcode.com/problems/number-of-islands/

2/15/2023
Graphs
Apparently a common fang question
BFs

--- PROMPT ---
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---




"""
# --- MY SOLUTION ---
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        input - list of lists

        island is based on if there are adjacent items (horiz or vert)

        output - integer

        Breadth first search - marking when elements nearby are visited or not
        Need to consider if something is visited or not, which will guide the condition in which we can increment the islands

        """
        # if empty grid
        if not grid:
            return 0
        # define length of row and column
        rows, cols = len(grid), len(grid[0])
        # setup a set to account for visited
        visit = set()
        islands = 0

        # BFS: iterative, and queue
        def bfs(r, c):
            # initalize the queue
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                # popping the first element (FIFO)
                row, col = q.popleft()
                # define right, left, up, down direction
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # check if in bounds... no small feat here
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                    c in range(cols) and
                    grid[r][c] == "1" and
                    (r, c) not in visit):
                    # if it is in bounds, add to queue, and add to visit
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                # so long as the grid is equal to 1, and the value is NOT in visit, increment the islands
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands

# --- TEST ---


# --- ALT SOLN by others ---
