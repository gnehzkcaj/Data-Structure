# refer to coin_change.property
import random

class SortingAlgorithm:
    def quick_sort(self, nums: list[int], left: int, right: int):
        """快速排序（尾递归优化）"""
    # 子数组长度为 1 时终止
        while left < right:
            # 哨兵划分操作
            pivot = self.partition(nums, left, right)
            # 对两个子数组中较短的那个执行快排
            if pivot - left < right - pivot:
                self.quick_sort(nums, left, pivot - 1)  # 递归排序左子数组
                left = pivot + 1  # 剩余未排序区间为 [pivot + 1, right]
            else:
                self.quick_sort(nums, pivot + 1, right)  # 递归排序右子数组
                right = pivot - 1  # 剩余未排序区间为 [left, pivot - 1]


    def median_three(self, nums: list[int], left: int, mid: int, right: int) -> int:
        """选取三个元素的中位数"""
    # 此处使用异或运算来简化代码
    # 异或规则为 0 ^ 0 = 1 ^ 1 = 0, 0 ^ 1 = 1 ^ 0 = 1
        if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):
            return left
        elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):
            return mid
        return right

    def partition(self, nums: list[int], left: int, right: int) -> int:
        """哨兵划分（三数取中值）"""
        # 以 nums[left] 作为基准数
        med = self.median_three(nums, left, (left + right) // 2, right)
        # 将中位数交换至数组最左端
        nums[left], nums[med] = nums[med], nums[left]
        pivot = nums[left]  # Use the median-of-three value as the pivot
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1  # 从右向左找首个小于基准数的元素
            while i < j and nums[i] <= pivot:
                i += 1  # 从左向右找首个大于基准数的元素
            # 元素交换
            nums[i], nums[j] = nums[j], nums[i]
        # 将基准数交换至两子数组的分界线
        nums[i], nums[left] = nums[left], nums[i]
        return i  # 返回基准数的索引

# 测试
sorting_algorithm = SortingAlgorithm()
arr = [random.randint(0, 1000) for _ in range(20)]

sorting_algorithm.quick_sort(arr, 0, len(arr) - 1)
print(arr)
