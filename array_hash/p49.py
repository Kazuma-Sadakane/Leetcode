class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cache = dict()
        for str in strs:
            key = "".join(sorted(str))
            if key in cache:
                cache[key].append(str)
            else:
                cache[key] = [str]
        return list(cache.values())
