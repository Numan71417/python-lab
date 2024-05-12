# merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left , right)

def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j+=1
        elif left[i] < right[j]:
            res.append(left[i]) 
            i+=1
    
    res += left[i:]
    res += right[j:]
    return res


nums_str = input("Enter the elements of array separated by space: ")
nums = nums_str.split()
nums_arr = [int(num) for num in nums]

print(nums_arr)

sorted_arr = merge_sort(nums_arr)

print("sorted array is", sorted_arr)