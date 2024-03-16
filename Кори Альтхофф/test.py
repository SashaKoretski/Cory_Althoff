class Solution:
    def countNegatives(self, grid) -> int:
        neg_sum = 0

        n = len(grid)
        m = len(grid[0])
        x = 0
        y = m - 1

        while x <= n - 1:
            print("x", grid[x][y], neg_sum)
            if grid[x][y] < 0:
                neg_sum += n - x
                if y == 0:
                    return neg_sum
                while y > 0:
                    y -= 1
                    if grid[x][y] < 0:
                        neg_sum += n - x
                    else:
                        break
                    if y == 0:
                        return neg_sum
            x += 1
        return neg_sum


gridd = [[3,3],[3,-1],[3,-2],[-3,-3],[-3,-3]]
a = Solution()
print(a.countNegatives(gridd))
