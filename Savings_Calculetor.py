print("Hi Dear, Today I assist You")
print("Provide me those information to calculate your savings.")
print("But First tell me, How you want to calculate")

print("1 = Monthly")
print("2 = Annually")
Monthly_Annually = int(input("How to calculate 1 or 2: "))

Income = int(input(f"How much is your {'monthly' if Monthly_Annually == 1 else 'annual'} income: "))
House_Rent = int(input(f"How much is your {'monthly' if Monthly_Annually == 1 else 'annual'} house Rent: "))
Food = int(input(f"How much money's food you consume {'monthly' if Monthly_Annually == 1 else 'annually'}: "))
Personal = int(input(f"How much you spend {'monthly' if Monthly_Annually == 1 else 'annually'} for your personal accessories: "))
Network = int(input(f"How much is your {'monthly' if Monthly_Annually == 1 else 'annual'} network cost: "))
Transportation_Cost = int(input(f"What is your {'monthly' if Monthly_Annually == 1 else 'annual'} transportation cost: "))
Others = int(input(f"How much you {'monthly' if Monthly_Annually == 1 else 'annual'} spend for others Cost: "))

print("Now Calculating time of your Savings")

Total_expense = House_Rent + Food + Personal + Network + Transportation_Cost + Others
Savings = Income - Total_expense

if Total_expense > Income:
    print("You can't save money because you spend more than your income")
    print("You spend more", abs(Savings), "than your income")
else:
    print("Your Monthly Saving is:", Savings)
    print("That's mean you can save", Savings, "a month")
