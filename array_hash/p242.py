class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        for val in s:
            if val in map:
                map[val] += 1
            else:
                map[val] = 1
        for val in t:
            if val in map:
                map[val] -= 1
                if map[val] == 0:
                    del map[val]
            else:
                return False
        if len(list(map.keys())) > 0:
            return False

        return True


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1
        for key, val in mapS.items():
            if val != mapT.get(key, -1):
                return False

        return True
