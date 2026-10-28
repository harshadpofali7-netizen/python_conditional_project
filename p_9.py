# Insurance Premium Calculator


name = input("Enter customer name: ")
age = int(input("Enter age: "))
occupation = input("Enter occupation risk (Low/Medium/High): ").lower()
smoker = input("Smoker? (Yes/No): ").lower()


base_premium = 10000
additional_charges = 0
eligibility = "Eligible"
risk_message = "Normal Policy"


if age < 18:
    eligibility = "Not Eligible"
    final_premium = 0
else:
  
    if age > 50:
        additional_charges += 5000

    if occupation == "high":
        additional_charges += 7000
    elif occupation == "medium":
        additional_charges += 3000

    if smoker == "yes":
        additional_charges += 5000

    final_premium = base_premium + additional_charges

    if additional_charges >= 10000:
        risk_message = "High Risk Policy"


print("\n--- Insurance Premium Details ---")
print("Customer Name:", name)
print("Eligibility:", eligibility)

if eligibility == "Eligible":
    print("Base Premium: ₹", base_premium)
    print("Additional Charges: ₹", additional_charges)
    print("Final Premium: ₹", final_premium)
    print("Risk Message:", risk_message)
else:
    print("Base Premium: Not Applicable")
    print("Additional Charges: Not Applicable")
    print("Final Premium: Not Applicable")
    print("Risk Message: Not Applicable")
