class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        row = len(rooms)
        col = len(rooms[0])
        s = []
        adjacents = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(row):
            for j in range(col):
                # start with gate but not the neighbors of the gates.
                if rooms[i][j] == 0: s.append((i, j))

                # this works too, add a little complication:
                #if rooms[i][j] != 0: continue
                #for x, y in adjacents:
                    #if 0 <= i+x < row and 0 <= j+y < col and rooms[i+x][j+y] > 0:
                    #    rooms[i+x][j+y] = 1
                    #    s.append((i+x, j+y))
        while s:
            cur_r, cur_c = s.pop(0)
            dis = rooms[cur_r][cur_c]
            for x, y in adjacents:
                new_r = cur_r+x
                new_c = cur_c+y
                if 0 <= new_r < row and 0 <= new_c < col and rooms[new_r][new_c] > 0:
                    if dis + 1 < rooms[new_r][new_c]:
                        rooms[new_r][new_c] = dis + 1
                        s.append((new_r, new_c))
        return

if __name__ == "__main__":
    sol = Solution()

    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

    sol.wallsAndGates(rooms)

    print rooms
