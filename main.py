# def merge_total(arr, left, left_len, right, right_len):
#     i=0
#     j=0
#     k=0
#     while(i<left_len and j<right_len):
#         if left[i]<right[j]:
#             arr[k]=left[i]
#             i=i+1
#         else:
#             arr[k]=right[j]
#             j=j+1
#         k=k+1
#
#     while(i<left_len):
#         arr[k]=left[i]
#         i=i+1
#         k=k+1
#
#     while(j<right_len):
#         arr[k]=right[j]
#         j=j+1
#         k=k+1
#
#     return(arr)
#
# def mergesort(arr, n):
#     mid = int(n / 2)
#     left = []
#     right = []
#     if n <= 1:
#         return
#     else:
#         for i in range(0, mid):
#             left.append(arr[i])
#         for i in range(mid, len(arr)):
#             right.append(arr[i])
#
#     mergesort(left, mid)
#     mergesort(right, n-mid)
#
#     merge_total(arr, left, mid, right, n-mid)
#     return arr
#
# # Taking Array input
# n=int(input("Enter the number of elements"))
# arr=[]
# for i in range(n):
#     temp=int(input())
#     arr.append(temp)
#
# n=len(arr)
#
# # Printing the Unsorted array
# print("Unsorted Array:")
# for i in arr:
#     print(i)
#
# # Sorting the array using Merge Sort recursively
# result = mergesort(arr,n)
#
# # Printing the Sorted array
# print("Sorted Array:")
# for i in result:
#     print(i)
#
#


def merge(arr_to_sort, left, left_len, right, right_len):
    i, j, k = 0, 0, 0
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            arr_to_sort[k] = left[i]
            i += 1
        else:
            arr_to_sort[k] = right[j]
            j += 1
        k += 1

    while i < left_len:
        arr_to_sort[k] = left[i]
        i += 1
        k += 1

    while j < right_len:
        arr_to_sort[k] = right[j]
        j += 1
        k += 1

    return arr_to_sort


def mergesort(arr, n):
    if n > 1:
        mid = n // 2
        left_list = arr[:mid]
        right_list = arr[mid:]

        left_len = len(left_list)
        right_len = len(right_list)

        mergesort(left_list, mid)
        mergesort(right_list, n - mid)

        merge(arr, left_list, left_len, right_list, right_len)

    return arr


num = int(input("Enter the number of elements: "))
list1 = []

print("Enter the elements:\n")
for _ in range(num):
    temp = int(input())
    list1.append(temp)

print("Unsorted List:")
for ele in list1:
    print(ele)

print("\n")
print("Sorting the list....")
print("\n")

if num>1:
    result = mergesort(list1, len(list1))
else:
    result = list1

print("Sorted List:")
for ele in result:
    print(ele)
