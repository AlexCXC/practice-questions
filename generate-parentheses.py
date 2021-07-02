class Solution:

    def func(self, s, st):
        if len(s) == 2 * self.n:
            self.results.append(s)
            return
        if 0 <= st < self.n and s.count('(') < self.n:
            self.func(s+'(', st+1)
        if st > 0:
            self.func(s+')', st-1)

    def generateParenthesis(self, n: int):
        if n == 1:
            return ['()']
        self.n = n
        s, st = '(', 1
        self.results = []
        self.func(s, st)
        return self.results


if __name__ == '__main__':
    print(Solution().generateParenthesis(2))
