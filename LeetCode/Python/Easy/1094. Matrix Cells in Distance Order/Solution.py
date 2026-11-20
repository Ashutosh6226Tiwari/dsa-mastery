class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        
        # collect all element 
        # fun for calculating distance 
        # sort the final 

        cells=[]
        for r in range (rows):
            for c in range (cols):
                cells.append([r,c])

        def get_distance (cell):
            r,c = cell[0] , cell[1]
            return  abs(r-rCenter) + abs(c-cCenter)

        cells.sort(key = get_distance)

        return cells

# time complexity = O(r.c.log (r.c))
# space complexity = O(r.c)


