#Problem Link: https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
def minmax(arr, n):
    return min(arr), max(arr)

n = int(input())
list1 = [int(i) for i in input().strip().split()]

if len(list1)==n:
    print(minmax(list1, 4))
else:
    print("Check you list range again!")