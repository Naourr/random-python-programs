import sys

def stop():
    print("Invalid input, exiting.")
    sys.exit()

def done():
    input("\nProgram finished. Press Enter to return to the main menu.")


# Minutes to hours converter
def mins_to_hours():
    print("\nMinutes to hours and minutes converter.")
    try:
        mins = int(input("Enter minutes to convert to hours: "))
        hours = mins // 60
        excess_mins = mins % 60

        if excess_mins:
            print(f"{hours} hours, and {excess_mins} minutes.")
        else:
            print(f"{hours} hours.")

    except ValueError:
        stop()
    done()


# BMI calculator
def bmi_calc():
    print("\nBMI calculator.")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in m: "))
        bmi = weight / height**2

        if bmi >= 30:
            classif = "obese"
        elif bmi >= 25:
            classif = "overweight"
        elif bmi >= 18.5:
            classif = "healthy"
        else:
            classif = "underweight"

        print(f"Your BMI is {round(bmi, 2)}, classified as {classif}.")

    except ValueError:
        stop()
    done()


# Leap Year Identifier
def leap_year_identifier():
    print("\nLeap Year Identifier.")
    try:
        year = int(input("Enter a year: "))
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                print("That is not a leap year (it's a century year).")
            else:
                print("That is a leap year.")
        else:
            print("That is not a leap year.")

    except ValueError:
        stop()
    done()


# Factorial Calculator
def factorial_calc():
    print("\nFactorial Calculator.")
    number = int(input("Enter a number to calculate its factorial: "))
    try:
        def factorial(num):
            if num == 1 or num == 0:
                return 1
            else:
                return num * factorial(num - 1)
		
        print(factorial(number))

    except ValueError:
        stop()
    done()


# Quiz Average Calculator
def quiz_average():
    print("\nQuiz Average Calculator.")
    try:
        q1 = float(input("Quiz 1 score /10: "))
        q2 = float(input("Quiz 2 score /20: "))
        q3 = float(input("Quiz 3 score /20: "))
        lq = float(input("Long quiz score /50: "))
        exam = float(input("Exam score /100: "))

        written = (q1 + q2 + q3 + lq) * 50 / 100
        finals = exam * 50 / 100
        print(f"Your final grade is {written + finals}.")

    except ValueError:
        stop()
    done()


# Common Length Unit Converter
def length_converter():
    print("\nCommon Length Units Converter.")
    try:
        mmTOm = 0.001
        cmTOm = 0.01
        mTOm = 1
        kmTOm = 1000
        inchTOm = 0.0254
        footTOm = 0.3048

        mTOmm = 1000
        mTOcm = 100
        mTOkm = 0.001
        mTOinch = 39.3701
        mTOfoot = 3.28084

        print("""\nUnits:
1) mm
2) cm
3) m
4) km
5) inch
6) foot
""")
        from_unit = int(input("Convert from (number): "))
        from_value = float(input("Enter value: "))

        if from_unit == 1:
            from_UNIT = "mm"; TOm = from_value * mmTOm
        elif from_unit == 2:
            from_UNIT = "cm"; TOm = from_value * cmTOm
        elif from_unit == 3:
            from_UNIT = "m"; TOm = from_value
        elif from_unit == 4:
            from_UNIT = "km"; TOm = from_value * kmTOm
        elif from_unit == 5:
            from_UNIT = "inch"; TOm = from_value * inchTOm
        elif from_unit == 6:
            from_UNIT = "foot"; TOm = from_value * footTOm
        else:
            stop()

        print("""\nConvert to:
1) mm
2) cm
3) m
4) km
5) inch
6) foot
""")
        to_unit = int(input("Convert to (number): "))

        if to_unit == 1:
            to_UNIT = "mm"; to_value = TOm * mTOmm
        elif to_unit == 2:
            to_UNIT = "cm"; to_value = TOm * mTOcm
        elif to_unit == 3:
            to_UNIT = "m"; to_value = TOm
        elif to_unit == 4:
            to_UNIT = "km"; to_value = TOm * mTOkm
        elif to_unit == 5:
            to_UNIT = "inch"; to_value = TOm * mTOinch
        elif to_unit == 6:
            to_UNIT = "foot"; to_value = TOm * mTOfoot
        else:
            stop()

        print(f"{from_value} {from_UNIT} = {to_value} {to_UNIT}")
    except ValueError:
        stop()
    done()


# Main Menu
def main_menu():
    print(r"""
 ____                 _                 
|  _ \ __ _ _ __   __| | ___  _ __ ___  
| |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \ 
|  _ < (_| | | | | (_| | (_) | | | | | |
|_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|
                                        
 ____                                          
|  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  ___ 
| |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \/ __|
|  __/| | | (_) | (_| | | | (_| | | | | | \__ \
|_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|___/
                 |___/                                                                            
""")
    print("""Selection:

1) BMI Calculator
2) Minutes to Hours Converter
3) Common Length Units Converter
4) Leap Year Identifier
5) Factorial Calculator
6) Quiz Average Calculator

Tip: Press CTRL + C anytime to stop.
""")

    choice = input("Enter number: ")
    if choice == "1":
        bmi_calc()
    elif choice == "2":
        mins_to_hours()
    elif choice == "3":
        length_converter()
    elif choice == "4":
        leap_year_identifier()
    elif choice == "5":
        factorial_calc()
    elif choice == "6":
        quiz_average()
    else:
        input("Invalid choice. Press Enter to try again.")
        main_menu()


# Main Program Loop
while True:
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nProgram terminated manually.")
        break
