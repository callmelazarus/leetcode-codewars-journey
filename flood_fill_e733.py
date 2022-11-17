"""
https://leetcode.com/problems/flood-fill/

11/7/2022

--- PROMPT ---

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.


--- LESSONS ---
Breadth first search BFS - an algorithm for searching graphs
used for shortest path problems
You want to search the same plane first before going into depths
you have a visited and queu list
Time complexity O( #Vertices's + #Edges

Graphs - recognizing this data structure is step 1
- node - points
- edges - arrows that link nodes

15 min Video describing BFS and flood fill:
https://www.youtube.com/watch?v=xlVX7dXLS64

1 hr vide lecture on graph search:
https://www.youtube.com/watch?v=s-CYnVz-uh4

--- QUESTIONS ---

"""


# --- MY SOLUTION ---
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):

        # solution from leetcode
        # time complexity: O(n) -> we cycle thru number of pixels in image, we may process every pixel
        # Space complexity O(n) -> size of implicit call stack when calling dfs

        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image



        # floodfill a specific pixel
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image

    def floodFill_jay(self, image, sr, sc,color):
      # this solution doesn't work, but was my first try
    # edge case
    
    # if the value located at sr/sc matches the color value -> return image
        if image[sr][sc] == color:
            return image
        
        # actual solution
        # impacted values: indexes that are ADJACENT to sr/sc

        # the hard part is the daisy chaining of the next adjacent value

        else:
            # one more and less sc / one more and less sr
            if image[sr][sc] != color:
                image[sr][sc] = color
                new_val = image[sr][sc]
            if image[sr+1][sc] != new_val: # 2, 1 index loc (0)
                image[sr+1][sc] = color
                self.floodFill(image, sr+1, sc, color)
            if image[sr-1][sc] != new_val:
                image[sr-1][sc] = color # 0, 1
                self.floodFill(image, sr-1, sc, color)
            if image[sr][sc+1] != new_val:
                image[sr][sc+1] = color
                self.floodFill(image, sr, sc+1, color)
            if image[sr][sc-1] != new_val:
                image[sr][sc-1] = color
                self.floodFill(image, sr, sc-1, color)
            return image



# --- PSUEDOCODE ---
"""
start by covering edge case where the sr/sc value is the same as the color value
take the smallest step forward
Achieve the next case where you are able to adjust the adjacent index conditions




"""
# --- TEST ---



# --- ALT SOLN by others ---
