import sys
balance = 5000  

if len(sys.argv) != 2:
    print("Usage: python program.py <withdrawal_amount>")
else:
    try:
        withdrawal = float(sys.argv[1])

        if withdrawal > balance:
            print("Insufficient balance!")
        elif withdrawal < 0:
            print("Invalid amount!")
        else:
            balance -= withdrawal
            print("Withdrawal Successful!")
            print("Remaining Balance:", balance)

    except ValueError:
        print("Please enter a valid number for withdrawal amount!")
