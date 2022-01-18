def smallest(arr, k):
    arr.sort()
    return arr[k-1]

n = int(input())
list1 = [int(i) for i in input().strip().split()]
k = int(input())
if len(list1)==n:
    print(smallest(list1,k))
else:
    print("Check the length of array again!")
