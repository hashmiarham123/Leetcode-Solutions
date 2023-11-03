class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rList = []
      
        for i in range(ord(s[0]), ord(s[3])+1):
            for j in range(int(s[1]), int(s[4])+1):
                rList.append(chr(i) + str(j))
        return rList
        