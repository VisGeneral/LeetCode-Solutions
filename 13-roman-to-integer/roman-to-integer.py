class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        chardict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        n = len(s)
        for i in range(n):
            if i < n - 1 and chardict[s[i]] < chardict[s[i + 1]]:
                count -= chardict[s[i]]
            else:
                count += chardict[s[i]]

        return count