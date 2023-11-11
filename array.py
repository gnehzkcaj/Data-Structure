# 初始化数组
import random
arr: list[int] = [0] * 5  # [ 0, 0, 0, 0, 0 ]
nums: list[int] = [1, 3, 2, 5, 4]  


def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    # 在区间 [0, len(nums)-1] 中随机抽取一个数字
    random_index = random.randint(0, len(nums) - 1)
    # 获取并返回随机元素
    random_num = nums[random_index]
    return random_num

def insert(nums: list[int], num: int, index: int):
    """在数组的索引 index 处插入元素 num"""
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 将 num 赋给 index 处元素
    nums[index] = num

def remove(nums: list[int], index: int):
    """删除索引 index 处元素"""
    # 把索引 index 之后的所有元素向前移动一位
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

def traverse(nums: list[int]):
    """遍历数组"""
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += 1
    # 直接遍历数组
    for num in nums:
        count += 1
    # 同时遍历数据索引和元素
    for i, num in enumerate(nums):
        count += 1

def find(nums: list[int], target: int) -> int:
    """在数组中查找指定元素"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(find(nums,5))

def reverse(nums: list[int]):
    """反转数组"""
    for i in range(len(nums) // 2):
        nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
    return nums

def sort(nums: list[int]):
    """排序数组"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def binary_search(nums: list[int], target: int) -> int:
    """二分查找"""
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:   # nums[mid] > target
            right = mid - 1
    return -1
  

insert(nums, 6, 2)
print(nums)

remove(nums, 2)
print(nums)
print(random_access(nums))
print(reverse(nums))
print(sort(nums))
print(binary_search(nums, 3))
#merge(nums, 5, [2, 5, 6], 3)
print(nums)


