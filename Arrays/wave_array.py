#Problem Link: https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1
def waveArray(arr, n):
        for i in range(0, n, 2):
          
            if (i> 0 and arr[i] < arr[i-1]):
                arr[i],arr[i-1] = arr[i-1],arr[i]
            
            if (i < n-1 and arr[i] < arr[i+1]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
  
k = int(input())
arr = [int(i) for i in input().strip().split()]
if len(arr) == k:
    print(waveArray(arr, len(arr)))
    for i in range(0,len(arr)):
        a = arr[i]
        print(a, end=' ')
else:
    print('Check range of list again!')