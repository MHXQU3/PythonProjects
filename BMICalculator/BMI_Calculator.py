class WeightCalc():

    def __init__(self):
        pass

    def htwt(self):
        while True:
            try:
                height = float(input('Please enter your height in metres: '))
                break
            except ValueError:
                print("Invalid input. Please enter a valid height.")
        
        while True:
            try:
                weight = float(input('Please enter your weight in kg: '))
                break
            except ValueError:
                print("Invalid input. Please enter a valid weight.")
        return height, weight

    def BMI(self, weight, height):
        bmi_calc = weight/(height**2)
        print(bmi_calc)
        return bmi_calc



    def group(self, bmi_calc):
        if bmi_calc < 18.5:
            print(f'Your BMI is {bmi_calc}. You are underweight')
        elif bmi_calc >= 18.5 and bmi_calc < 25:
            print(f'Your BMI is {bmi_calc}. You are in the healthy range')
        elif bmi_calc >= 25 and bmi_calc < 30:
            print(f'Your BMI is {bmi_calc}. You are in the overweight range')
        elif bmi_calc >= 30 and bmi_calc < 40:
            print(f'Your BMI is {bmi_calc}. You are in the obese range')
        else:
            print(f'Your BMI is {bmi_calc}. You are in the severely obese range')

weight_calc = WeightCalc()
height, weight = weight_calc.htwt()
bmi_value = weight_calc.BMI(weight, height)
weight_calc.group(bmi_value)