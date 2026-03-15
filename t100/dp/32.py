class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        v = [0] * n

        st = []
        for i in range(n):
            if s[i] == ')':
                if st and s[st[-1]] == '(':
                    id = st.pop()
                    v[i] = 1
                    v[id] = 1
            else:
                st.append(i)

        l = ans = 0
        for i in range(n):
            if v[i] == 1:
                l += 1
            else:
                ans = max(ans, l)
                l = 0
                
        return max(ans, l)