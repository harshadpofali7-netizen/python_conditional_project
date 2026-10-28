# Movie Ticket Booking Program

def calculate_ticket(customer_name, age, show_type, day_type):
   
    if age < 0:
        return "Invalid input: Age cannot be negative."

   
    base_price = 200
    discount = 0
    surcharge = 0

   
    if age < 12:
        discount = base_price * 0.50   # 50% discount
    elif age >= 60:
        discount = base_price * 0.30   # 30% discount

   
    if show_type.lower() == "morning":
        discount += 30
    elif show_type.lower() != "evening":
        return "Invalid show type. Choose Morning or Evening."

   
    if day_type.lower() == "weekend":
        surcharge = 50
    elif day_type.lower() != "weekday":
        return "Invalid day type. Choose Weekday or Weekend."

   
    final_price = base_price - discount + surcharge

   
    print("🎬 Movie Ticket Bill")
    print("----------------------------")
    print(f"Customer Name     : {customer_name}")
    print(f"Original Price    : ₹{base_price}")
    print(f"Discount Applied  : ₹{discount}")


calculate_ticket ("Harshad", 65, "Morning", "Weekend")