#Rudolf Musika
#CIS 1400
#Chapter 11 Assignment

ConstantMealPlan1 = 560.00
ConstantMealPlan2 = 900.00
ConstantMealPlan3 = 1300.00
def main():
    while True:
        displayMenu()
        if menuSelectedNumber ==1:
            calcNumberOfSemesterTot()
        if menuSelectedNumber ==2:
            calcNumberOfSemesterTot()
        if menuSelectedNumber==3:
            calcNumberOfSemesterTot()
            
        if menuSelectedNumber ==4:
            print("Goodbye!")
            break;
        
# displayMenu Calls the menu on which the user will read the instructions
def displayMenu():
    print('COLLEGE OF DUPAGE MENU PLAN OPTIONS')
    print('1.  One-Meal-A-Day Plan -7 meals per week for $560.00 ')
    print('2.  Two-Meal-A-Day -14 meals per week for $900.00')
    print('3.  Unlimited-Meals-A-Day Plan - $1300.00')
    print('4.  END THE PROGRAM')

    global menuSelectedNumber 
    menuSelectedNumber = int(input("Enter Your Selection: "))

# Input Validation loop
    while menuSelectedNumber <1 or menuSelectedNumber > 4:
        print ("That is an invalid selection")
        menuSelectedNumber = int(input("Enter 1,2, 3 or 4: "))

#calcNumberOfSemesterTot is the module that calculates the total price for the semesters also as specified by user        
def calcNumberOfSemesterTot():
    semesterCount = float(input("Enter the number of semesters -1 or 2: "))
# Input Validation loop 
    while semesterCount<1 or semesterCount>2:
        print("It is up to only 2 semesters per year, so please enter either 1 or 2, ")
        semesterCount = float(input("Enter the number of semesters -1 or 2: "))
    while True:
        if menuSelectedNumber == 1:
            totalPrice = semesterCount*ConstantMealPlan1
            print("The total price of one meal a day for "+str(semesterCount)+"semesters is $ ",format(totalPrice,".0f"),"\n")
        if menuSelectedNumber == 2:
            totalPrice = semesterCount*ConstantMealPlan2
            print("The total price of two meals a day for "+str(semesterCount)+"semesters is $ ",format(totalPrice,".0f"),"\n")
        if menuSelectedNumber == 3:
            totalPrice = semesterCount*ConstantMealPlan3
            print("Unlimited total price for "+str(semesterCount)+"semesters is $ ",format(totalPrice,".0f"),"\n")

        break;
        
main()
