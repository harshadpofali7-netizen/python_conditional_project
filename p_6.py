# Hotel Room Booking System

def hotel_booking():
    
    guest_name = input("Enter guest name: ")
    room_type = input("Enter room type (Standard/Deluxe/Suite): ")
    nights = int(input("Enter number of nights: "))

    if nights <= 0:
        print("Error: Number of nights must be greater than 0.")
    else:
       
        if room_type == "Standard":
            price_per_night = 2000
        elif room_type == "Deluxe":
            price_per_night = 3500
        elif room_type == "Suite":
            price_per_night = 6000
        else:
            print("Error: Invalid room type.")
            return  

     
        room_charge = price_per_night * nights

      
        if nights >= 10:
            discount_rate = 0.20
        else:
            if nights >= 5:
                discount_rate = 0.10
            else:
                discount_rate = 0.0

        discount = room_charge * discount_rate
        final_amount = room_charge - discount

       
        print("\n--- Booking Details ---")
        print(f"Guest Name       : {guest_name}")
        print(f"Room Type        : {room_type}")
        print(f"Number of Nights : {nights}")
        print(f"Room Charge      : ₹{room_charge}")
        print(f"Discount         : ₹{discount}")
        print(f"Final Amount     : ₹{final_amount}")

# Run the program
hotel_booking()
