nums = input("Enter numbers separated by space")
num_arr = nums.split()
print("nums_arr : ",num_arr)
num_list = [ int(num) for num in num_arr ]
print("mylist: ",num_list)

for num in num_list:
    if(num*num)%8==0:
        print(num)