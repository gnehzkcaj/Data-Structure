def binary_search_insertion_simple(nums: list[int], target: int) -> int:
    """二分查找插入点（无重复元素）"""
    i, j = 0, len(nums) - 1  # 初始化双闭区间 [0, n-1]
    while i <= j:
        m = (i + j) // 2  # 计算中点索引 m
        if nums[m] < target:
            i = m + 1  # target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # target 在区间 [i, m-1] 中
        else:
            nums.insert(m + 1, target)
            return m + 1  # 找到 target ，insert target to the right of m
    # 未找到 target ，insert target to the right of i
    nums.insert(i, target)
    return i

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binary_search_insertion_simple(nums=numbers, target=10)
print(numbers)
print("Inserted at index:", index)