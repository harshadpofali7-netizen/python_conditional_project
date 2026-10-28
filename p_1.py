# Mini project 1 :Smart electricity bill calculator
customer_name = input("Enter customer name :")
units_consumed = float(input("Enter units consumed :"))
FIXED_SERVICE_CHARGE = 150.0
energy_charge = 0.0
if units_consumed <= 100:
    energy_charges = units_consumed * 3
elif units_consumed <= 200:
    energy_charges = (100 * 3) + ((units_consumed - 100) * 5)
else:
    energy_charges = (100 * 3) + (100 * 5) + ((units_consumed - 200) * 7)
final_bill = energy_charges + FIXED_SERVICE_CHARGE
usage_message = ""
if final_bill > 5000:
    usage_message = "High usage bill"
print("\n" + "="*30)
print("     ELECTRICITY BILL")
print("="*30)
print(f"customer name : {customer_name}")
print(f"units consumed : {units_consumed} units")
print(f"energy charges : ${energy_charges:}")
print(f"service charges : ${FIXED_SERVICE_CHARGE:}")
print(f"final bill : ${final_bill:}")
if usage_message :
    print(f"message           :alert! {usage_message}")
print("="*30)
