# BMI Calculator
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def interpret_bmi(bmi):

    if bmi < 21.5:
        return "Underweight"
    elif 21.5 <= bmi < 25.9:
        return "Normal Weight"
    elif 26 <= bmi < 30.5:
        return "Overweight"
    else:
        return "Obese"
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in Feet: "))
bmi_result = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi_result)
print("Your BMI is:",bmi_result)
print("You are classified as:",bmi_category)
