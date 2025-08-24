# BMI Calculator - Command Line Version

def calculate_bmi(weight, height):
    """Calculate BMI using formula: BMI = weight / height^2"""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Validation
        if weight <= 0 or height <= 0:
            print("Please enter positive values for weight and height.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        # Display result
        print(f"\n Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()

