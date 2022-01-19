def sort012(arr, n):
    return arr.sort()
n = int(input())
l1 = [int(i) for i in input().strip().split()]
if len(l1) == n:
    print(sort012(l1,n))
else:
    print('Check the length of your array again!')