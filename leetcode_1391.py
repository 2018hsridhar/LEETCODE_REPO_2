'''
URL := https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/
1391. Check if There is a Valid Path in a Grid
TINY GRID : 6 configurations only
-> can put in an adjList?

15 ish minutes -> on harder end
It needs grid connectivitty SMH

'''
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        adjList = dict()
        m = len(grid)
        n = len(grid[0])

        directions = {
            "left cell": [0, -1],
            "right cell": [0, 1],
            "top cell": [-1, 0],
            "bottom cell": [1, 0]
        }

        street_map = {
            1: ["left cell", "right cell"],
            2: ["top cell", "bottom cell"],
            3: ["left cell", "bottom cell"],
            4: ["right cell", "bottom cell"],
            5: ["left cell", "top cell"],
            6: ["right cell", "top cell"]
        }

        # [1][ make adj list]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                key = (str)(r) + "-" + (str)(c)
                adjList[key] = []
                configVal = grid[r][c]
                nHood = street_map[configVal]
                for cell in list(nHood):
                    delta = directions[cell]
                    [dx,dy] = delta
                    cx = r + dx
                    cy = c + dy
                    child = [cx,cy]
                    if(self.isInBounds(cx,cy,grid)):
                        adjList[key].append(child)

        cleaned_data = self.clean_asymmetric_links(adjList)

    
       
        reachStatus = False
        # DFS on the adjList and explore
        start = [0,0]
        frontier = [start]
        visited = set()
        while(len(frontier) > 0):
            parent = frontier.pop()
            [pr,pc] = parent
            if(pr == m-1 and pc == n-1):
                # Kinda : the shape has to make sense
                # The connectivity is there, but we need a sensical shape 
                # In both ways too
                reachStatus = True
                break
            parentKey = (str)(pr) + "-" + (str)(pc)
            if(parentKey not in visited):
                visited.add(parentKey)
                children = cleaned_data[parentKey]
                # Can we even go to the child position
                # reacability : parent->children and children->parent needed
                for child in children:
                    frontier.append(child)
        return reachStatus

    def isInBounds(self, r, c, grid) -> bool:
        m = len(grid)
        n = len(grid[0])
        return (0 <= r and r < m ) and (0 <= c and c < n)

    def clean_asymmetric_links(self, d):
        # Build coordinate → key lookup
        coord_to_key = {tuple(map(int, k.split('-'))): k for k in d}

        cleaned = {}

        for key, connections in d.items():
            key_coords = list(map(int, key.split('-')))
            valid_connections = []

            for conn in connections:
                conn_key = coord_to_key.get(tuple(conn))
                if not conn_key:
                    continue  # skip invalid or unknown target

                # If the target links back, it's valid
                if key_coords in d.get(conn_key, []):
                    valid_connections.append(conn)

            cleaned[key] = valid_connections

        return cleaned
