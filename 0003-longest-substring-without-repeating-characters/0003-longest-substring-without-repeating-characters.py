class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # left = 0
        # result = 0
        # for right in range(len(s)):
        #     while s[right] in charSet:
        #         charSet.remove(s[left])
        #         left +=1
        #     charSet.add(s[right])
        #     result = max(result, right - left + 1)
        # return result
        #or
        if len(s) == 0:
            return 0
        
        map = {}
        max_length = start = 0
        
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            map[s[i]] = i
        return (max_length)
            