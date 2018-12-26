class Solution:
    # return an autonomous function corresponding to operation("+", "-", "*")
    def op(self, operator):
        """
        :type operator: str
        :rtype: lambda x, y
        """
        if operator == "+":
            return lambda a, b: a+b
        if operator == "-":
            return lambda a, b: a-b
        if operator == "*":
            return lambda a, b: a*b
    def readNum(self, input, pos):
        num = ""
        while pos < len(input) and pos >= 0:
            if input[pos] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                num += input[pos]
                pos += 1
            else: break
        return int(num), pos
    # recursively divide and conquer the input and calculate the possible output
    def cal(self, root, lops, rops):
        left = []
        right = []
        rst = []
        cur = root[0]
        operation = root[1]
        if not lops:
            left = [self.nums[cur-1]]
        else: 
            for i, op in enumerate(lops): left += self.cal(op, lops[0:i], lops[i+1:])
        if not rops:
            right = [self.nums[cur+1]]
        else: 
            for i, op in enumerate(rops): right += self.cal(op, rops[0:i], rops[i+1:])
        for l in left:
            for r in right:
                rst.append(self.op(operation)(l, r))
        return rst
            
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.ops = []
        self.nums = {}
        pos = count = 0
        while pos < len(input):
            if input[pos] in ["+", "-", "*"]:
                self.ops.append((count, input[pos]))
                pos += 1
            else:
                n, pos = self.readNum(input, pos) 
                self.nums[count] = n
            count += 1
        if len(self.ops) == 0: return [int(input)]
        rst = []
        for i, op in enumerate(self.ops):
            rst += self.cal(op, self.ops[0:i], self.ops[i+1:])
        return rst

if __name__ == "__main__":
    sol = Solution()
    print sol.diffWaysToCompute("0")
    print sol.diffWaysToCompute("12")
    print sol.diffWaysToCompute("3+5")
    print sol.diffWaysToCompute("2*3-4")
    print sol.diffWaysToCompute("2*3-4*5")
