# binary Search

def binary_search(nums, key):
    left = 0
    right = len(nums) -1

    while(left < right):
        mid = (left + right)//2

        if nums[mid] > key:
            right = mid-1
        elif nums[mid] < key:
            left = mid+1
        else:
            return mid

    return -1            


nums_str = input("Enter sorted array separated by space : ")
nums = nums_str.split()
num_arr = [ int(n) for n in nums ]

# print(num_arr)
key = int(input("Enter the element to search: "))

search_res = binary_search(num_arr , key)

if search_res == -1:
    print("Element not found!")
else:
    print(f"Element found at index: {search_res}")