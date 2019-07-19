class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stk = []
        for s in S:
            if not stk:
                stk.append(s)
            else:
                if stk[-1] == s:
                    stk.pop(-1)
                else:
                    stk.append(s)
        return "".join(stk)
