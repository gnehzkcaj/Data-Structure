# 初始化列表
# 无初始值
nums1: list[int] = []
# 有初始值
nums: list[int] = [1, 3, 2, 5, 4]

# 访问元素
num: int = nums[1]  # 访问索引 1 处的元素

print(num)

# 更新元素
nums[1] = 0    # 将索引 1 处的元素更新为 0

print(nums)

# 清空列表
nums.clear()

# 尾部添加元素
nums.append(1)
nums.append(3)
nums.append(2)
nums.append(5)
nums.append(4)

# 中间插入元素
nums.insert(3, 6)  # 在索引 3 处插入数字 6
print(nums)
# 删除元素
nums.pop(3)        # 删除索引 3 处的元素
print(nums)

# 排序
nums.sort()
print(nums)

# 反转
nums.reverse()
print(nums)

# 长度
print(len(nums))

# 遍历
for num in nums:
    print(num)

# 拼接两个列表
nums1: list[int] = [6, 8, 7, 10, 9]
nums += nums1  # 将列表 nums1 拼接到 nums 之后

print(nums)

# 通过索引遍历列表
count = 0
for i in range(len(nums)):
    count += 1

# 直接遍历列表元素
count = 0
for num in nums:
    count += 1
print(count)