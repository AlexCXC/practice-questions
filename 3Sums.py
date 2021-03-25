class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    results.add('%s_%s_%s' % (nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return [[int(i) for i in r.split('_')] for r in results]
