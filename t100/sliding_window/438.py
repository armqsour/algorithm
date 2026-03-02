from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        p = ''.join(p)
        tmp_set = set()
        tmp_set.add(p)
        n = len(s)
        ans = []
        for i in range(n - len(p) + 1):
            if ''.join(sorted(s[i:i + len(p)])) in tmp_set:
                ans.append(i)
        return ans

# 0x3f
def findAnagrams(self, s: str, p: str) -> List[int]:
    cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
    cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 t 的每种字母的出现次数
    ans = []
    for right, c in enumerate(s):
        cnt_s[c] += 1  # 右端点字母进入窗口
        left = right - len(p) + 1
        if left < 0:  # 窗口长度不足 len(p)
            continue
        if cnt_s == cnt_p:  # t 和 p 的每种字母的出现次数都相同
            ans.append(left)  # t 左端点下标加入答案
        cnt_s[s[left]] -= 1  # 左端点字母离开窗口
    return ans