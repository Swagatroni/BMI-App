# Kenn Thomas, Jr.
# kwt61
# BMI App


def calculate_bmi(weight, height_ft, height_in):
    if weight <= 0 or height_ft <= 0 or height_in < 0 or height_in >= 12:
        raise ValueError("Invalid input values")

    weight_kg = weight * 0.45
    height_m = (height_ft * 12 + height_in) * 0.025

    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)  # Round to two decimal places

def classify(val):
    if 0 <= val < 18.5:
        return "You are Underweight"
    elif 18.5 <= val <= 24.9:
        return "You have a Normal Weight"
    elif 25 <= val <= 29.9:
        return "You are Overweight"
    elif val >= 30:
        return "You are Obese"
    else:
        raise ValueError("Invalid BMI value")

try:
#     w = float(input("Enter your weight in pounds: "))
#     h_ft = int(input("Enter your height in feet: "))
#     h_in = int(input("Enter your height in inches: "))
    w = 0
    h_ft = 0
    h_in = 0

    bmi_val = calculate_bmi(w, h_ft, h_in)
    print("Your BMI is:", bmi_val)
    print(classify(bmi_val))

except ValueError as e:
    print("Error:", e)
