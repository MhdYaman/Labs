'''
lab1.def
mohamad
9/5/2018
'''
def miles_per_gallon(miles,gallons):
    miles_driven = input("Enter miles driven")
    gallons_used = input("Enter gallons used")

    miles_driven = float(miles_driven)
    gallons_used = float(gallons_used)

    mpg = miles_driven / gallons_used
    print("miles per gallon:",mpg)
