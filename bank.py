import sys

if len(sys.argv) == 3:
    balance = sys.argv[1]
    deposit = sys.argv[2]
    print("User provided input values:")
else:
    print("No input given - using default values:")
    balance = "1000"
    deposit = "500"

updated_balance = eval(balance) + eval(deposit)
print("Updated Balance:", updated_balance)
