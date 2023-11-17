def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i -1
        while j >= 0 and nums[j] > base:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = base
        
arr = [4,4,3,1,52,2]
insertion_sort(arr)
print(arr)

def isort(nums):
    for index in range(1, len(nums)):
       value = nums[index]
       i =  index - 1
       while i >= 0:
           if value < nums[i]:
               nums[i+1] = nums[i]
               nums[i] = value
               i -= 1
           else:
               break

arr = [4,4,3,1,6,8,52,2]
isort(arr)
print(arr)