#Mini project 2 : Online shoping checkpoint
customer_name = input("Enter customer name :")
purchase_amount = float(input("Enter purchase amount ($):"))
customer_type = input("Enter customer type (Regular/Premium)")
discount_percentage = 0.0
delivary_charge = 0.0
if purchase_amount >= 5000:
    discount_percentage = 0.20
elif purchase_amount >= 3000:
    discount_percentage = 0.10
elif purchase_amount >= 1000:
    discount_percentage = 0.05
else:
    discount_percentage = 0.00
if customer_type == "Premium":
    discount_percentage += 0.05
discount_amount = purchase_amount + discount_percentage
provisional_amount = purchase_amount - discount_amount
if provisional_amount >= 2000:
    delivary_charge = 0.0
else:
    delivary_charge = 100.0
final_payable = provisional_amount + delivary_charge
print("\n" + "="*35)
print("         Shopping Checkout Recipt")
print("="*35)
print(f"customer name : {customer_name} ")
print(f"customer type : {customer_type}")
print(f"original purchase : ${purchase_amount:}")
print(f"discount applied : ${discount_amount:}")
print(f"dilivary charge : ${delivary_charge:}")
print("-"*35)
print(f"Final payable amount : ${final_payable:}")
print("="*35)
