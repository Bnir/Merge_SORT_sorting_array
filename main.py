def mergetotal(arr, left, left_len, right, right_len):
    i=0
    j=0
    k=0
    while(i<left_len and j<right_len):
        if left[i]<right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1

    while(i<left_len):
        arr[k]=left[i]
        i=i+1
        k=k+1

    while(j<right_len):
        arr[k]=right[j]
        j=j+1
        k=k+1

    return(arr)

def mergesort(arr, n):
    mid = int(n / 2)
    left = []
    right = []
    if n <= 1:
        return
    else:
        for i in range(0, mid):
            left.append(arr[i])
        for i in range(mid, len(arr)):
            right.append(arr[i])

    mergesort(left, mid)
    mergesort(right, n-mid)

    mergetotal(arr, left, mid, right, n-mid)
    return arr

# Taking Array input
n=int(input("Enter the number of elements"))
arr=[]
for i in range(n):
    temp=int(input())
    arr.append(temp)

n=len(arr)

# Printing the Unsorted array
print("Unsorted Array:")
for i in arr:
    print(i)

# Sorting the array using Merge Sort recursively
result = mergesort(arr,n)

# Printing the Sorted array
print("Sorted Array:")
for i in result:
    print(i)


