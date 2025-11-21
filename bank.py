import sys

if len(sys.argv) == 3:
    current= sys.argv[1]
    withdrawal = sys.argv[2]
    print("User provided input values:")
else:
    print("No input given - using default values:")
    current = "1000"
    withdrawal= "500"

updated_balance = eval(current) -eval(withdrawal)
print("Updated Balance:", updated_balance)
