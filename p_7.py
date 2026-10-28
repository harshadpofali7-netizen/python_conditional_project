# Mobile Data Plan Billing Program

def calculate_bill(customer_name, plan_type, extra_data):
    # Validate input
    if extra_data < 0:
        return "Invalid input: Extra data usage cannot be negative."

    # Initialize charges
    base_charge = 0
    included_data = 0

    # Determine plan details
    if plan_type.lower() == "basic":
        base_charge = 299
        included_data = 10
    elif plan_type.lower() == "standard":
        base_charge = 499
        included_data = 25
    elif plan_type.lower() == "premium":
        base_charge = 799
        included_data = 50
    else:
        return "Invalid plan type. Choose Basic, Standard, or Premium."

    # Calculate extra data charge
    extra_charge = extra_data * 20

    # Apply surcharge if extra data > 10 GB
    surcharge = 100 if extra_data > 10 else 0

    # Final bill
    final_bill = base_charge + extra_charge + surcharge

    # Output
    print("📱 Mobile Data Plan Bill")
    print("----------------------------")
    print(f"Customer Name   : {customer_name}")
    print(f"Plan Type       : {plan_type.capitalize()}")
    print(f"Base Plan Charge: ₹{base_charge}")
    print(f"Extra Data Used : {extra_data} GB")
    print(f"Extra Data Charge: ₹{extra_charge}")
    print(f"Surcharge       : ₹{surcharge}")
    print(f"Final Bill      : ₹{final_bill}")


# Example Run
calculate_bill("Harshad", "premium", 12)
