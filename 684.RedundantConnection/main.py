class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent_info = {}
        loop = {}
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            if not node2 in parent_info:
                parent_info[node2] = node1
            elif not node1 in parent_info:
                parent_info[node1] = node2
                loop = self.getLoop(parent_info, node1)
                if len(loop) != 0: break
            else: return edge
        print loop
        l = len(edge)
        for i in range(l):
            if edges[l-i-1][0] in loop and edges[l-i-1][1] in loop:
                return edge
        return []
    def getLoop(self, parents, start_node):
        node = start_node
        loop = {}
        while node in parents:
            loop[node] = True
            if parents[node] in loop: break
            node = parents[node]
        if node in parents and parents[node] in loop: 
            return loop
        else:
            return {}

def __main__():
    solution = Solution()

    case7 = [[3,4],[1,2],[2,4],[3,5],[2,5]]
    print solution.findRedundantConnection(case7)

    '''
    case6 = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    print solution.findRedundantConnection(case6)

    case1 = [[1,2],[1,3],[2,3]] 
    print solution.findRedundantConnection(case1)

    case2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print solution.findRedundantConnection(case2)

    case3 = [[1,2],[1,3],[3,4],[3,5],[5,6],[5,7],[4,7]]
    print solution.findRedundantConnection(case3)

    case4 = [[1,2],[1,3],[3,4],[3,5],[4,7],[5,6],[5,7]]
    print solution.findRedundantConnection(case4)

    case5 = [[1,2],[1,3],[3,4],[3,5],[3,7],[5,6],[5,7]]
    print solution.findRedundantConnection(case5)
    '''

__main__()
