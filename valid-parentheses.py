class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == '(':
                l.append(i)
            elif i == ')':
                if not l or l[-1] != '(':
                    return False
                l = l[:-1]
            elif i == '[':
                l.append(i)
            elif i == ']':
                if not l or l[-1] != '[':
                    return False
                l = l[:-1]
            elif i == '{':
                l.append(i)
            elif i == '}':
                if not l or l[-1] != '{':
                    return False
                l = l[:-1]
        return not l


if __name__ == '__main__':
    print(Solution().isValid('((()))[]'))
