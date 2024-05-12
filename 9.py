file_name = input("Enter the file name: ")

words =0
no_of_words = 0
no_of_lines = 0
no_of_chars = 0


with open(file_name, 'r') as f:
    for line in f:
        words = line.split()
        no_of_lines += 1
        no_of_words += len(words)
        no_of_chars += len(line)

print(f"\nNumber of lines in the file is: {no_of_lines}")
print(f"\nNumber of words in the file is: {no_of_words}")
print(f"\nNumber of chars in the file is: {no_of_chars}")