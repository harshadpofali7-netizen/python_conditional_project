# Mini project 4 : Student scholarship eligilibility
student_name = input("Enter student name :")
percentage = float(input("Enter acadimic percentage (%):"))
family_income = float(input("Enter annual family income ($):"))
attendence = float(input("Enter attendence percentage (%):"))
basic_condition_met = (percentage >= 75) and (family_income <= 400000) and (attendence <= 75)
print("\n--- SCHOLARSHIP ELIGILIBILITY REPORT ---")
print(f"student name : {student_name}")
if basic_condition_met:
    print("Eligilibility status : eligible")
    if percentage >= 90:
        print("Scholarship category : full scholarship")
    else:
        print("scholarship catagory : partial scholarship")
else:
    print("Eligilibility status : not eligible")
    print("scholarship category : none")
    rejection_reasons = []
    if percentage < 75:
        rejection_reasons.append(f"percentage is {percentage}%, bot at least 75% required")
    if family_income > 400000:
        rejection_reasons.append(f"family income is ${family_income}, which exceeds the limit of $4,00,000.")
    if attendence < 75:
        rejection_reasons.append(f"attendence is {attendence}%, but at least 75% is required")
print(f"Reason : {'AND'. join(rejection_reasons)}")
