# Leetcode: https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # if len(strs) == 1:
        #     return [strs]
        # res = []
        # for i in range(len(strs)):
        #     # if strs[i] == "":
        #     #     r.append("")
        #     #     continue
        #     r = []
        #     r.append(str(strs[i]))
        #     for j in strs:
            
        #         if sorted([m for m in strs[i]]) == sorted([k for k in j]) and strs[i]!=j:
        #             r.append(str(j))
        #     if sorted(r) not in res:
        #         res.append(sorted(r))
        # # print(res)
        # return res
        d = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        return d.values()
        # d = defaultdict(list)
        # for s in strs:
        #     t = hash(''.join(sorted(s)))
        #     d[t].append(s)
        # return [v[1] for v in d.items()]
