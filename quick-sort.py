def quick_sort(nums, start, end):
    if start >= end:
        return

    mid = nums[start]
    left, right = start + 1, end
    while left <= right:
        while left <= right and nums[left] < mid:
            left += 1
        while left <= right and nums[right] > mid:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    nums[right], nums[start] = nums[start], nums[right]

    quick_sort(nums, start, left - 1)
    quick_sort(nums, left + 1, end)


def inplace_quick_sort(s,a,b):
    """列表的就地快速排序，s为列表，a为起始索引，b为终止索引"""
    if a >= b:
        return
    # s[b]作为基准值
    p = s[b]
    # left和right相当于指向
    left = a
    right = b-1
    # 把除了s[b]d 其他元素按照以s[b]为基准分割
    while left <= right:
        while left <= right and s[left] < p:
            left += 1
        while left <= right and p < s[right]:
            right -=1
        if left <= right:
            s[left],s[right] = s[right],s[left]
            left,right = left+1,right-1

    s[left],s[b] = s[b],s[left]
    inplace_quick_sort(s,a,left-1)
    inplace_quick_sort(s,left+1,b)


def self_inplace_quick_sort(nums, start, end):
    if start >= end:
        return
    left, right = start, end
    p = nums[start]
    while left < right:
        while left < right and nums[right] >= p:
            right -= 1
        nums[left] = nums[right]
        print('temp nums: ', nums)
        while left < right and nums[left] < p:
            left += 1
        nums[right] = nums[left]
        print('temp nums: ', nums)
    nums[left] = p
    print('stage nums: ', nums)
    # exit(1)
    self_inplace_quick_sort(nums, start, left-1)
    self_inplace_quick_sort(nums, left+1, end)


if __name__ == '__main__':
    nums = [5, 9, 1, 11, 6, 7, 2, 4]
    # nums = [2, 3, 1]
    # quick_sort(nums, 0, len(nums) - 1)
    # inplace_quick_sort(nums, 0, len(nums)-1)
    self_inplace_quick_sort(nums, 0, len(nums)-1)
    print(nums)
