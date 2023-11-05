# def linear_search(lst, target):
#     """Returns the index position of the target if found, else returns -1"""

#     for i in range(0, len(lst)):
#         if lst[i] == target:
#             return i
#     return -1


def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9]

result = linear_search(numbers, 6)
verify(result)