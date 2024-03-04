# Kenn Thomas, Jr.
# kwt61
# BMI App


def calculate_bmi(weight, height_ft, height_in):
    weight_kg = weight * 0.45
    height_m = (height_ft * 12 + height_in) * 0.025

    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify(val):
    if val < 18.5:
        print("You are Underweight")
    elif 18.5 <= val <= 24.9:
        print("You are Normal Weight")
    elif 25 <= val <= 29.9:
        print("You are Overweight")
    elif val >= 30:
        print("You are Obese")
    else:
        print("Error")
    
    
w = float(input("Enter your weight in pounds: "))

h_ft = int(input("Enter your height in feet: "))
h_in = int(input("Enter your height in inches: "))

bmi_val = calculate_bmi(w, h_ft, h_in)
print("Your BMI is:", bmi_val)
classify(bmi_val)


