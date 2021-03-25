class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums = sorted(nums)
        s = None
        for i in range(len(nums)-2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    return target
                elif nums[i] + nums[j] + nums[k] > target:
                    s = self.get_closet(s, nums[i] + nums[j] + nums[k], target)
                    k -= 1
                else:
                    s = self.get_closet(s, nums[i] + nums[j] + nums[k], target)
                    j += 1
        return s

    def get_closet(self, s, new, target):
        if s is None:
            return new
        if abs(s - target) > abs(new - target):
            return new
        return s


if __name__ == "__main__":
    # Solution().threeSumClosest([1, 1, 1, 1], 0)
    # Solution().threeSumClosest([-1, 2, 1, -4], 1)
    s = Solution().threeSumClosest([0, 2, 1, -3], 1)
    print(s)
