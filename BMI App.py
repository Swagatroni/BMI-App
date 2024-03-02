# Kenn Thomas, Jr.
# kwt61
# BMI App

# Body Mass Index:
    # Height - feet and inches
    # Weight - pounds

# Calculate BMI value and category:
    # < 18.5 - Underweight 
    # 18.5–24.9 - Normal weight 
    # 25–29.9 - Overweight 
    # >=30 - Obese

def calculate_bmi(weight, height):
    weight = weight * 0.45
    height = height * 0.025
    
    bmi = weight / (height ** 2)
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
h = h_ft * 12 + h_in

bmi_val = calculate_bmi(w, h)
print("Your BMI is:", bmi_val)
classify(bmi_val)


