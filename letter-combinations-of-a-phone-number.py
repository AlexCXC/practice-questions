class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        self.lmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        strs_list = []
        self.results = []
        for d in digits:
            strs_list.append(self.lmap[d])
        # print('strs_list: ', strs_list)

        self.gen_strs('', 0, strs_list)
        return self.results

    def gen_strs(self, result, index, strs_list):
        # print('result: ', result, ' index: ', index)
        if index >= len(strs_list):
            self.results.append(result)
            return
        for x in strs_list[index]:
            self.gen_strs(result+x, index+1, strs_list)


if __name__ == "__main__":
    print(Solution().letterCombinations('23'))
