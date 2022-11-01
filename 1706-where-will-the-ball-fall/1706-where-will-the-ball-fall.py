def solve(grid, n):
    current = n;
    for i in range( len(grid) ):
        if( grid[i][current] == 1 ):
            if( current+1 == len(grid[i]) or grid[i][current+1] == -1 ):
                return -1
            current += 1
        else:
            if( current == 0 ): return -1
            if( grid[i][current-1] == 1 ):
                return -1
            current -= 1
    # print(current)
    return current
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid[0])):
            ans.append( solve(grid, i) )
        return ans