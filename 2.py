inp_str = input("Enter the string :  ")

set_str = set(inp_str)

for ele in set_str:
    no_of_ele = 0
    for char in inp_str:
        if ele == char:
            no_of_ele+=1
    print(f"The character {ele} occures {no_of_ele} times.")