# Ian Hedges, Collin Glover



# Comments apply to line/block underneath of the comment




# math library is imported so math.pi can be used for area and volume
import math




# These functions exist to eliminate repetitive code/make the code more readable

# Response for ValueError
def MathInputError():
    print('You have made an invalid entry. You may have included a letter or other non-numerical character in one of your entries or used multiple decimal points.', '\n')

# Response for OverflowError
def OverflowErrorResponse():
    print('The answer is too large and has caused an overflow error! Sorry!', '\n')

# Response for ZeroDivisionError
def DivByZero():
    print('Cannot divide by zero', '\n')

# Automates operator selection response and number entry for basic calculations
def BasicOpBody(operator):
    print('You have selected ', operator, '\n')

    print('Enter the first number:', '\n')

    global Num1

    Num1 = input()

    print()

    print('Enter the second number:', '\n')

    global Num2
    
    Num2 = input()

    print()

    
    #FUNCTIONS FOR BASIC CALCULATIONS

# Function for addition
def add(Num1,Num2):
    global Answer
    Answer = float(Num1) + float(Num2)

# Funciton for subtraction
def subtract(Num1,Num2):
    global Answer
    Answer = float(Num1) - float(Num2)

# Function for multiplication
def multiply(Num1,Num2):
    global Answer
    Answer = float(Num1) * float(Num2)

# Function for division
def divide(Num1,Num2):
    global Answer
    Answer = float(Num1) / float(Num2)

# Function for modulus
def modulus(Num1,Num2):
    global Answer
    Answer = float(Num1) % float(Num2)

# Function for exponentiation
def exponent(Num1,Num2):
    global Answer
    Answer = float(Num1) ** float(Num2)

    

    # FUNCTIONS FOR AREA

# Function for area of a triangle
def areaTriangle(Length,Width):
    global Answer
    Answer = ((float(Length) * float(Width)) / 2)

# Function for area of a rectangle
def areaRectangle(Length,Width):
    global Answer
    Answer = float(Length) * float(Width)

# Function for area a circle
def areaCircle(Radius):
    global Answer
    Answer = math.pi * (float(Radius) ** 2)



    # FUNCTIONS FOR VOLUME

# Function for volume of a cube
def volumeCube(Length,Width,Height):
    global Answer
    Answer = float(Length) * float(Width) * float(Height)

# Function for volume of a cone
def volumeCone(Radius,Height):
    global Answer
    Answer = (math.pi * (float(Radius) ** 2) * float(Height)) / 3

# Function for volume of a cylinder
def volumeCylinder(Radius,Height):
    global Answer
    Answer = (math.pi * (float(Radius) ** 2) * float(Height))
    


    # FUNCTIONS FOR UNIT CONVERSION

# Function for meters to feet conversion
def Meter2FeetConv(meters):
    global Answer
    Answer = float(meters) * 3.2808399
    
# Function for feet to meters conversion
def Feet2MeterConv(feet):
    global Answer
    Answer = float(feet) * 0.3048

# Function for kilograms to pounds conversion
def Kilo2PoundConv(kilograms):
    global Answer
    Answer = float(kilograms) * 2.20462262

# Function for pounds to kilogramss conversion
def Pound2KiloConv(pounds):
    global Answer
    Answer = float(pounds) * 0.45359237



    # FUNCTIONS FOR BUSINESS CALCULATIONS

# Function for compound interest
def compoundInterest(Principal,Interest,NumOfPeriods):
    global Answer
    Answer = (float(Principal) * ((1 + float(Interest)) ** float(NumOfPeriods))) - float(Principal)

# Function for break-even point
def breakEvenPoint(FixedCosts,SalesPricePU,VariableCostsPU):
    global Answer
    Answer = float(FixedCosts) / (float(SalesPricePU) - float(VariableCostsPU))

    # INVALID SELECTION RESPONSE FUNCTION

# Function for when user input does not match an item in menu
                                                                                         
def InvalidSelection():
    print('You have entered an invalid selection', '\n', '\n', 'Please follow the prompt below to return to the selection menu.', '\n')


    
    

# Introduction text for beginning of program
print('Welcome to the Basic, Engineering, and Business Calculator!', '\n')

# Variable for while loop
UseCalculator = 'Yes'

# while loop for continuous use of calculator program
while UseCalculator == 'Yes' or UseCalculator == 'yes' or UseCalculator == 'Y' or UseCalculator == 'y':

    print('Would you like to perfrom a Basic, Engineering, or Business calculation?','\n', '\n','Enter "1" for Basic, "2" for Engineering, or "3" for Business below or enter "9" to shut down the calculator:', '\n')

    CalcType = input()

    print()

    # Most if statements in the program will allow for an uncapitalized input in case user is unaware of the program being case-sensitive
    if CalcType == 'Basic' or CalcType == 'basic' or CalcType == '1':

        print('You have selected Basic', '\n')

        print('The available Basic calculations are:', '\n', 'Addition (+)', '\n', 'Subtraction (-)', '\n', 'Multiplication (*)', '\n', 'Division (/)', '\n', 'Modulus/remainder of division (mod)', '\n', 'Exponentiation/raise a number to a certain power (^).', '\n')

        print('Please enter the corresponding symbol/operator (+, -, *, /, mod, or ^) for your desired calculation:', '\n')

        BasicOp = input()

        print()

        if BasicOp == '+':

            BasicOpBody(BasicOp)

            try:
                add(Num1,Num2)

                print('The answer to ', Num1, '+', Num2, 'is: ', Answer, '\n')

            except ValueError:
                MathInputError()

        elif BasicOp == '-':

            BasicOpBody(BasicOp)

            try:
                subtract(Num1,Num2)

                print('The answer to ', Num1, '-', Num2, 'is: ', Answer, '\n')

            except ValueError:
                MathInputError()

            
        elif BasicOp == '*':

            BasicOpBody(BasicOp)

            try:
                multiply(Num1,Num2)

                print('The answer to ', Num1, '*', Num2, 'is: ', Answer, '\n')
            except ValueError:
                MathInputError()
            except OverflowError:
                OverflowErrorResponse()

            
        elif BasicOp == '/':

            print('You have selected division', '\n')

            print('Enter the dividend (number being divided):', '\n')

            Num1 = input()

            print()

            print('Enter the divisor (the number the dividend is being divided by):', '\n')

            Num2 = input()

            print()

            try:
                divide(Num1,Num2)
                print('The answer to ', Num1, '/', Num2, 'is: ', Answer, '\n')
            except ZeroDivisionError:
                DivByZero()
            except ValueError:
                MathInputError()

            
        elif BasicOp == 'mod':

            print('You have selected modulus', '\n')

            print('Enter the dividend (number being divided)', '\n')

            Num1 = input()

            print()

            print('Enter the divisor (the number the dividend is being divided by):', '\n')

            Num2 = input()

            print()

            try:
                modulus(Num1,Num2)

                print('The remainder of ', Num1, '/', Num2, 'is: ', Answer, '\n')
            except ValueError:
                MathInputError()
            except ZeroDivisionError:
                DivByZero()

            
        elif BasicOp == '^':

            print('You have selected exponentiation', '\n')

            print('Enter the base:', '\n')
 
            Num1 = input()

            print()

            print('Enter the exponent:', '\n')

            Num2 = input()

            print()

            try:
                exponent(Num1,Num2)

                print('The answer to ', Num1, '^', Num2, 'is: ', Answer, '\n')
            except ValueError:
                MathInputError()
            except OverflowError:
                OverflowErrorResponse()


        else:

            InvalidSelection()

        
    elif CalcType == 'Engineering' or CalcType == 'engineering' or CalcType == '2':

        print('You have selected Engineering', '\n')

        print('The available categories of Engineering calculations are:', '\n', '(1) Area', '\n', '(2) Volume', '\n', '(3) Unit Conversion', '\n')

        print('Please enter the number of the category you would like to use:', '\n')

        EngCategory = input()

        print()

        if EngCategory == 'Area' or EngCategory == 'area' or EngCategory == '1':

            print('The following area calculations are available:', '\n', '(1) Triangle', '\n', '(2) Rectangle', '\n', '(3) Circle', '\n')

            print('Please enter the number of the type of area you would like to calculate:', '\n')

            AreaType = input()

            print()

            if AreaType == 'Triangle' or AreaType == 'triangle' or AreaType == '1':

                print('You have chosen to calculate the area of a triangle. The formula for the area of a triangle is: [length (l) * width (w)] / 2', '\n')

                print('Enter the value for length (l):', '\n')

                Length = input()

                print()

                print('Enter the value for width (w):', '\n')

                Width = input()

                print()

                try:
                    areaTriangle(Length,Width)

                    print('The area of a triangle with a length of ', Length, 'and a width of ', Width, 'is', Answer, '\n')
                except ValueError:
                    MathInputError()

            elif AreaType == 'Rectangle' or AreaType == 'rectangle' or AreaType == '2':

                print('You have chosen to calculate the area of a rectangle/square. The formula for the area of a rectangle is: length (l) * width (w)', '\n')

                print('Enter the value for length (l):', '\n')

                Length = input()

                print()

                print('Enter the value for width (w):', '\n')

                Width = input()

                print()

                try:
                    areaRectangle(Length,Width)

                    print('The area of a rectangle with a length of ', Length, 'and a width of ', Width, 'is', Answer, '\n')
                except ValueError:
                    MathInputError()
                
            elif AreaType == 'Circle' or AreaType == 'circle' or AreaType == '3':

                print('You have chosen to calculate the area of a circle. The formula for the area of a circle is: pi * [radius (r)] ^ 2', '\n')

                print('Enter the value for the radius (r):', '\n')

                Radius = input()

                print()

                try:
                    areaCircle(Radius)

                    print('The area of a circle with a radius of ', Radius, 'is', Answer, '\n')
                except ValueError:
                    MathInputError()

            
        elif EngCategory == 'Volume' or EngCategory == 'volume' or EngCategory == '2':
            
            print('The following volume calculations are available:', '\n', '(1) Cube', '\n', '(2) Cone', '\n', '(3) Cylinder', '\n')

            print('Please enter the number of the type of volume you would like to calculate:', '\n')

            VolumeType = input()

            print()

            if VolumeType == 'Cube' or VolumeType == 'cube' or VolumeType == '1':

                print('You have chosen to calculate the volume of a cube. The formula for the volume of a cube is: length (l) * width (w) * height (h)', '\n')

                print('Enter the value for length (l):', '\n')

                Length = input()

                print()

                print('Enter the value for width (w):', '\n')

                Width = input()

                print()

                print('Enter the value for height (h):', '\n')

                Height = input()

                print()

                try:
                    volumeCube(Length,Width,Height)

                    print('The volume of a cube with a length of ', Length, ', a width of ', Width, ', and a height of', Height, 'is', Answer, '\n')
                except ValueError:
                    MathInputError()
                
                
            elif VolumeType == 'Cone' or VolumeType == 'cone' or VolumeType == '2':

                print('You have chosen to calculate the volume of a cone. The formula for the volume of a cone is: [pi * ((radius (r)) ^ 2) * )height (h))] / 3', '\n')

                print('Enter the value for the radius (r):', '\n')

                Radius = input()

                print()

                print('Enter the value for height (h)', '\n')

                Height = input()

                print()

                try:
                    volumeCone(Radius,Height)

                    print('The volume of a cone with a radius of ', Radius, 'and a height of', Height, 'is', Answer, '\n')
                except ValueError:
                    MathInputError()
                
            elif VolumeType == 'Cylinder' or VolumeType == 'cylinder' or VolumeType == '3':

                print('You have chosen to calculate the volume of a cylinder. The formula for the volume of a cylinder is: pi * ((radius (r)) ^ 2) * (height (h))', '\n')

                print('Enter the value for the radius (r):', '\n')

                Radius = input()

                print()

                print('Enter the value for height (h)', '\n')

                Height = input()

                print()

                try:
                    volumeCylinder(Radius,Height)

                    print('The volume of a cylinder with a radius of ', Radius, 'and a height of', Height, 'is', Answer, '\n')
                except ValueError:
                    MathInputError()

            
            
        elif EngCategory == 'Unit Conversion' or EngCategory == 'Unit conversion' or EngCategory == 'unit conversion' or EngCategory == '3':
            
            print('The following unit conversion calculations are available:', '\n',  '(1) Meters to feet', '\n', '(2) Feet to meters', '\n', '(3) Kilograms to pounds', '\n', '(4) Pounds to kilograms', '\n')

            print('Please enter the number of the conversion you would like to perform:', '\n')

            UnitConversionType = input()

            print()
            

            if UnitConversionType == 'meters to feet' or UnitConversionType == '1':
                
                print('You have chosen to convert meters to feet', '\n')

                print('Enter number of meters:', '\n')

                meters = input()

                print()

                try:
                    Meter2FeetConv(meters)

                    print(meters, 'meters is eqaul to', Answer, 'feet', '\n')
                except ValueError:
                    MathInputError()
                

            elif UnitConversionType == 'feet to meters' or UnitConversionType == '2':
                
                print('You have chosen to convert feet to meters', '\n')

                print('Enter number of feet:', '\n')

                feet = input()

                print()

                try:
                    Feet2MeterConv(feet)

                    print(feet, 'feet is equal to', Answer, 'meters', '\n')
                except ValueError:
                    MathInputError()
                

            elif UnitConversionType == 'kilograms to pounds' or UnitConversionType == '3':

                print('You have chosen to convert kilograms to pounds', '\n')

                print('Enter number of kilograms:', '\n')

                kilograms = input()

                print()

                try:
                    Kilo2PoundConv(kilograms)

                    print(kilograms, 'kilograms is equal to', Answer, 'pounds', '\n')
                except ValueError:
                    MathInputError()
                

            elif UnitConversionType == 'pounds to kilograms' or UnitConversionType == '4':

                print('You have chosen to convert pounds to kilograms', '\n')

                print('Enter number of pounds:', '\n')

                pounds = input()

                print()

                try:
                    Pound2KiloConv(pounds)

                    print(pounds, 'pounds is equal to', Answer, 'kilograms', '\n')
                except ValueError:
                    MathInputError()


            else:
                InvalidSelection()
                

    elif CalcType == 'Business' or CalcType == 'business' or CalcType == '3':

        print('You have selected Business', '\n')
        
        print('The available Business calculations are:', '\n', '(1) Compound Interest', '\n', '(2) Break-Even Point', '\n')

        print('Please enter the number of the calculation you would like to perform:', '\n')

        BusCalcType = input()

        print()

        if BusCalcType == 'Compound Interest' or BusCalcType == '1':

            print('You have chosen to calculate Compound Interest. The formula for compound interest is:(P*(1+i)^n) - P)', '\n' * 2, 'P = principal, i = annual interest rate, n = number of periods', '\n')

            print('Enter the amount of the principal (P):', '\n')

            Principal = input()

            print()

            print('Enter the annual interest rate (i):', '\n' * 2, 'Please enter in decimal form without % symbol (25% as 0.25, 10% as 0.10, 3.2% as 0.032, etc.)', '\n')

            Interest = input()

            print()

            print('Enter the number of periods (n):', '\n')

            NumOfPeriods = input()

            print()

            try:
                compoundInterest(Principal,Interest,NumOfPeriods)

                print('\n', 'The compound interest when the prinicipal is ', Principal + ',', 'the annual interest rate is ', Interest + ',', 'and with ', NumOfPeriods, 'periods is: ', Answer, '\n')

            except ValueError:
                MathInputError()

        elif BusCalcType == 'Break-Even Point' or BusCalcType == '2':

            print('You have chosen to calculate Break-Even Point. The formula for a break-even point (units) is: Fixed Costs / (sales price per unit - variable costs per unit)', '\n')

            print('Enter the amount of fixed costs:', '\n')

            FixedCosts = input()

            print('\n', 'Enter the sales price per unit:', '\n')

            SalesPricePU = input()

            print('\n', 'Enter the variable costs per unit:', '\n')

            VariableCostsPU = input()

            print()

            try:
                breakEvenPoint(FixedCosts,SalesPricePU,VariableCostsPU)

                print('\n', 'The break-even point in units with fixed costs of ', FixedCosts + ',', 'a sales price per unit of ', SalesPricePU + ',', 'and variable costs per unit of ', VariableCostsPU, 'is: ', Answer, 'units', '\n')

            except ValueError:
                MathInputError()
                
            except ZeroDivisionError:
                DivByZero()

        else:

            InvalidSelection()

    elif CalcType == 'Exit' or CalcType == 'exit' or CalcType == '9':

        break

    else:

        InvalidSelection()

        

    print('If you would like to calculate something else, type "Yes", "yes", "Y", or "y". If not, type anything else', '\n')

    UseCalculator = input()

    print()
    
    continue

print('Thank you for using the Basic, Engineering, and Business Calculator!', '\n', '\n', 'You have exited the Basic, Engineering, and Business Calculator.')
