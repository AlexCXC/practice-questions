class Solution:

    def can_add_left(self, s, n):
        s = list(s)
        if s.count('(') >= n:
            return False
        

    def can_add_right(self, s, n):
        s = list(s)
        if s.count(')') >= n:
            return False

    def generateParenthesis(self, n: int):
        results, results_set = [], set()
        stack, flags = ['('], {'('}
        while stack:
            top = stack.pop()
            if len(top) == n * 2 and top not in results_set:
                results.append(top)
                results_set.add(top)
                continue
            # whether can add '(' and stack in

            # whether can add ')' and stack in
