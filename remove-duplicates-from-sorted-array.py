class Solution:
    def removeDuplicates(self, nums) -> int:
        index = 0
        count = len(nums)
        while index < count:
            end_index = index
            for i in range(index+1, count):
                if nums[index] != nums[i]:
                    break
                end_index = i
            if index != end_index:
                for i in range(end_index+1, count):
                    nums[i - (end_index - index)] = nums[i]
                count -= end_index - index
            index += 1
        return count


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
    print(nums)
