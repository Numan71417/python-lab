wage = float(input("Enter the hourly wage: "))
no_of_hrs = int(input("Enter no of hours worked last week: "))

if no_of_hrs > 40 and no_of_hrs <= 60:
    print("your's week pay is: ", no_of_hrs * wage * 1.5)
elif no_of_hrs > 60 :
    print("your's week pay is: ", no_of_hrs * wage * 2)
else:
    print("your's week pay is: ", no_of_hrs * wage)