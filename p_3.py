# Mini project 3 : ATM withdrawal system
account_holder = input("Enter account holder name :")
current_balance = float(input("Enter current balance ($):"))
withdrawal_amonut = float(input("Enter withdrawal amonut ($):"))
print("\n--- ATM TRENSECTION AMOUNT ---")
print(f"Account holder : {account_holder}")
if withdrawal_amonut > 0:
    if withdrawal_amonut <= 20000:
        if withdrawal_amonut <= current_balance:
            remaining_balance = current_balance - withdrawal_amonut
            print("Transaction status : successful")
            print(f"Withdrawal amonut :{withdrawal_amonut}")
            print(f"Remaning balance : {remaining_balance}")
            if remaining_balance < 1000:
                print("Alert : low balance warning!")
        else:
            print("Transaction status : rejected")
            print(f"Rejection reason : insufficient balance. you only have ${current_balance}")
    else:
        print("Transaction status : rejected")
        print("Rejection reason : maximum withdrawal allowed per trancation is 20000.")
else:
    print("Tranction status : rejected")
    print("Rejection reason : withdrawal amonut is greater than 0.")
    