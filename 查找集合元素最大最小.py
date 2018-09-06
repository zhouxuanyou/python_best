import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
#获取最大元素
print(heapq.nlargest(3,nums))
#获取最元素
print(heapq.nsmallest(3,nums))
print(list(nums))