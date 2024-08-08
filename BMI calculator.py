class BMICalculator:
    def __init__(self):
        """Initialize the BMI Calculator."""
        pass

    def calculate_bmi(self, weight, height):
        """
        Calculate the Body Mass Index (BMI).

        Args:
            weight (float): The weight in kilograms.
            height (float): The height in meters.

        Returns:
            float: The calculated BMI.
        """
        return weight / (height ** 2)

    def categorize_bmi(self, bmi):
        """
        Categorize the BMI result.

        Args:
            bmi (float): The calculated BMI.

        Returns:
            str: The category of the BMI.
        """
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def run(self):
        """Run the BMI calculator tool."""
        while True:
            try:
                weight = float(input("Enter your weight in kilograms: "))
                height = float(input("Enter your height in meters: "))

                # Calculate BMI
                bmi = self.calculate_bmi(weight, height)
                category = self.categorize_bmi(bmi)

                print(f"Your BMI is: {bmi:.2f}")
                print(f"BMI Category: {category}")

            except ValueError:
                print("Invalid input. Please enter numeric values for weight and height.")

            # Check if the user wants to calculate again
            repeat = input("Do you want to calculate another BMI? (yes/no): ").strip().lower()
            if repeat != 'yes':
                print("Thanks for using, goodbye!")
                break

if __name__ == "__main__":
    # Create an instance of BMICalculator and run it
    bmi_calculator = BMICalculator()
    bmi_calculator.run()