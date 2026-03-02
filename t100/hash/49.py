from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {}
        # for i in strs:
        #     res.setdefault(tuple(sorted(Counter(i).items())), []).append(i)
        # return list(res.values())
        res = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            res[ss].append(s)
        return list(res.values())