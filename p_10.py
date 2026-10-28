# Restaurant Bill and Service Charge Calculator

name = input("Enter customer name: ")
bill_amount = float(input("Enter food bill amount: ₹"))
membership = input("Membership? (Yes/No): ").lower()

discount_rate = 0
service_charge_rate = 0.05
message = ""

if bill_amount < 1000:
    discount_rate = 0
elif bill_amount >= 1000 and bill_amount <= 2999:
    discount_rate = 0.05
elif bill_amount >= 3000 and bill_amount <= 4999:
    discount_rate = 0.10
else:
    discount_rate = 0.15

if membership == "yes":
    discount_rate += 0.05

discount = bill_amount * discount_rate
amount_after_discount = bill_amount - discount

service_charge = amount_after_discount * service_charge_rate
final_amount = amount_after_discount + service_charge

if final_amount >= 5000:
    message = "Thank you for being a valued customer"
else:
    message = "Visit Again!"

print("\n--- Restaurant Bill Details ---")
print("Customer Name:", name)
print("Original Bill: ₹", bill_amount)
print("Discount: ₹", discount)
print("Service Charge: ₹", service_charge)
print("Final Payable Amount: ₹", final_amount)
print("Message:", message)
