def rev(arr, end):
    return arr[::-1]
n = int(input())
arr = [int(i) for i in input().strip().split()]
if len(arr) == n:
    print(rev(arr, len(arr)))
else:
    print('Check your list range again!')