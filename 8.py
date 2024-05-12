print("\t\t Welcome  to Bike Rental App \t\t")
print("\t\t------------------------------------\t")

option = 0
bill = 0
discount = 0.7

bikes = ["Geared", "Non Geared", "Heavy Duty", "Travel"]

def getBill(ch):
    amt = 0
    print("Claim family Discount of 30% by renting 3 to 5 bikes")
    no_of_bikes = int(input("Enter no of bikes you want to rent: "))
    if ch == 1:
        amt += 100 * no_of_bikes
    elif ch == 2:
        amt += 500 * no_of_bikes
    elif ch == 3:
        amt += 2500 * no_of_bikes
    else:
        print("Invalid choice")
        return -1
    
    if no_of_bikes in range(3,6):
        print("\nCongratulations you got 30% discount 🎉")
        amt = amt*discount
    
    return amt


while(True):
    print("\nSelect your option from below: ")
    print("1.View Bikes\n2.See Prices\n3.Rent now\n4.exit")
    op = int(input("Enter your choice: "))

    if op == 1:
        print()
        for i in bikes:
            print(i)
    elif op == 2:
        print("\n1.For Hourly Rental --------- 100\n2.For Daily Rental --------- 500\n3.For weekly rental -------- 2500")

    elif op == 3:
        print("\n\nSelect the type of rental you need: ")
        print("1.Hourly\t- 100\n2.Daily\t- 500\n3.Weekly\t- 2500")
        print("\nClaim family Discount of 30% by renting 3 to 5 bikes\n")
        ch = int(input("Enter your choice: "))
        bill = getBill(ch)
        
        if bill == -1:
            break
        
        print("\n\n\t----- Thank you for Renting from our company -----\t")
        print("Your final Bill is\t----- ",bill)
    
    else:
        break

