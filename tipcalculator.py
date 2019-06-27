#!/usr/bin/python

##This function takes the input from the customer requesting the bill total. It then
##prompts the user to select a tip percentage. The tip amount is then output to terminal.
def get_bill():
    billtotal = float(input("How much is your bill?\n"))
    while (billtotal >= 1):
        desiredpercent = float(input("What percent tip do you want to leave?\n"))
        subtotal_tip = float(billtotal) * desiredpercent / 100 
        print("The total tip is: " + "$" + ("{:.2f}".format(subtotal_tip)))
        return subtotal_tip
        #break
    if (billtotal <= 0):
        print("Please re-enter the amount. Bill must be greater than 0.")
        get_bill()

##This takes the returned value from def get_bill() and makes it usable for the code related to splitting the tip.
subtotal_tip= get_bill()

##The following code asks the user if they want to split the tip.
split = str(input("Do you want to split the tip? Y/N\n"))

#The following code checks the user input to determine if the total tip should be divided between a number of people,
#or to return the total tip value again.
if (split == "Y" or split == "y"):
    splitnumber = int(input("Between how many people do you want to split the tip?\n"))
    pptip= float(subtotal_tip)/float(splitnumber)
    print("The per person tip is: " + "$" + str(round(pptip, 2)))
else:
    print("The total tip is: " + "$" + ("{:.2f}".format(subtotal_tip)))

