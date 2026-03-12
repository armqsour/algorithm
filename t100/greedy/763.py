from collections import Counter, defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return s
        all_cnt = Counter(s)
        cnt = defaultdict(int)
        # cnt[s[0]] += 1
        start = 0
        ans = []
        for i in range(0, len(s), 1):
            if cnt and all(v == all_cnt[k] for k, v in cnt.items()):
                ans.append(i-start)
                # ans.append(s[start:i])
                start = i
            cnt[s[i]] += 1
        ans.append(len(s)-start)
        return ans
    
# 0x3f
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}  # 每个字母最后出现的下标
        ans = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])  # 更新当前区间右端点的最大值
            if end == i:  # 当前区间合并完毕
                ans.append(end - start + 1)  # 区间长度加入答案
                start = i + 1  # 下一个区间的左端点
        return ans

print(Solution().partitionLabels(s="ababcbacadefegdehijhklij"))