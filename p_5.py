# Mini project 5 : Employee performance bonus
employee_name = input("Enter empoyee name")
monthly_salary = float(input("Enter monthly salary ($) :"))
experience = float(input("Enter years of experience :"))
performance_rating = int(input("Enter performance rating (1 to 5):"))
if performance_rating < 1 or performance_rating > 5:
    print("\n--- ERROR ---")
    print("Invalid input : performance rating must be whole number 1 and 5.")
else:
    bonus_percentage = 0
    if experience >= 10 and performance_rating >= 4:
        bonus_percentage = 20
    elif experience >= 5 and performance_rating >= 4:
            bonus_percentage = 15
    elif experience >= 2 and performance_rating >= 3:
                bonus_percentage = 10
    else:
          bonus_percentage = 0
    bonus_amount = (bonus_percentage/100) * monthly_salary
    final_salary = monthly_salary + bonus_amount
if performance_rating == 5:
      performance_message = "Excellent performance"
elif performance_rating >= 3:
      performance_message = "Good performer"
else:
      performance_message = "Needs improvement"
print("\n--- SALARY BONUS REPORT ---")
print(f"Employee name :{employee_name}")
print(f"performance message :{performance_message}")
print(f"bonus percentage : {bonus_percentage}%")
print(f"bonus amonut : {bonus_amount}")
print(f"Final salary (salary + bonus): ${final_salary:}")

