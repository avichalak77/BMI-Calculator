def calculate_bmi(weight, height_m):
    return weight / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Low body weight may affect immunity. Focus on nutritious meals."
    elif bmi < 25:
        return "Normal weight", "Excellent! Maintain balanced diet and regular activity."
    elif bmi < 30:
        return "Overweight", "Increased risk of lifestyle diseases. Light exercise is recommended."
    else:
        return "Obese", "High health risk. Medical guidance and lifestyle changes are advised."

print("=== ADVANCED BMI CALCULATOR ===")

while True:
    try:
        weight = float(input("\nEnter your weight (kg): "))
        if weight <= 0:
            print("Weight must be greater than zero.")
            continue

        height_choice = input("Is your height in (cm/m)? ").lower()

        if height_choice == "cm":
            height_cm = float(input("Enter height in cm: "))
            height_m = height_cm / 100
        elif height_choice == "m":
            height_m = float(input("Enter height in meters: "))
        else:
            print("Invalid choice. Enter 'cm' or 'm'.")
            continue

        if height_m <= 0:
            print("Height must be greater than zero.")
            continue

        bmi = calculate_bmi(weight, height_m)
        category, advice = bmi_category(bmi)

        print("\n--- BMI REPORT ---")
        print(f"BMI Value   : {round(bmi, 2)}")
        print(f"Category    : {category}")
        print(f"Health Note : {advice}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

    again = input("\nDo you want to calculate BMI for another person? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for using Advanced BMI Calculator 💙")
        break
