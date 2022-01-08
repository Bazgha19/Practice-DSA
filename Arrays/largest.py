#Problem Link: https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1
def largest(arr, n):
    return max(arr)

n = int(input())
list1 = [int(i) for i in input().strip().split()]
if len(list1) == n:
    print(largest(list1, n))
else:
    print('Check range of list again!')