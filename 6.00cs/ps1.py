
#Problem 1 - calculate the principal owed after a year if only the minimum payments were made on a credit card.
# print("Lets calculate the amount owed on a credit card loan at the end of the year, when only the minimum payment is paid.")
# print("")
# outstandingBal = int(raw_input("How much do you owe on the loan? $" ))
# apr = float(raw_input("what is the annual percentage rate as a decimal? " ))
# monthlyPaymentRate = float(raw_input("what is the minimum monthly payment rate as a decimal? "))
#
# for month in range(1,13):
#     print ("Month : " + str(month))
#     minPayment = monthlyPaymentRate * outstandingBal
#     intPaid = (apr/12) * outstandingBal
#     principalPaid = minPayment - intPaid
#     remainBal = outstandingBal - principalPaid
#     outstandingBal = remainBal
#     print ("Minimum monthly payment is : $" + str(round(minPayment,2)))
#     print ("Principal paid is : $" + str(round(principalPaid,2)))
#     print ("Remaining balance is : $" + str(round(outstandingBal,2)))
#     month += 1
#     print("")

#problem 2
# Now write a program that calculates the minimum fixed monthly payment needed in order pay
# off a credit card balance within 12 months. We will not be dealing with a minimum monthly
# payment rate.
# initialBalance = float(raw_input("Enter the outstanding balance on your credit card: "))
# interestRate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
#
# # Initialize state variables. state variables are tbe most basic variables that describe the system.
# monthlyPayment = 0
# monthlyInterestRate = interestRate/12
# balance = initialBalance
#
# # Test increasing amounts of monthlyPayment in increments of $100
# # until it can be paid off in a year
# #use nested while loops. the second loop will run as long as the first loops parameters are not met, which is balance being less that zero. If the second loop cannot bring the balance down to zero, the second loop will exit and the first loop will increase the monthly payment by ten.
# while balance > 0:
#
#     monthlyPayment += 10
#     balance = initialBalance
#     numMonths = 0
#
#     while numMonths < 12 and balance > 0: #this is why balance can become negative.
#
#         # Count this as a new month
#         numMonths += 1
#         interest = monthlyInterestRate * balance
#         balance -= monthlyPayment
#         balance += interest
#
# balance = round(balance,2)
#
# print "Monthly payment to pay off debt in 1 year:", monthlyPayment
# print "Number of months needed:", numMonths
# print "Balance:",balance

#problem 3  -  use biesection search
#get input
original_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# Initialize state variables
balance = original_balance
low_payment = balance/12
high_payment = (balance*(1+(interest_rate/12))**12)/12

# Use bisection search until the search space is sufficiently small
while True:
    balance = original_balance
    monthly_payment = (low_payment + high_payment)/2

    # Simulate passage of time until outstanding balance is paid off
    # Each iteration represents 1 month
    for month in range(1,13):
        interest = round(balance*interest_rate/12, 2)
        balance += interest - monthly_payment
        if balance <= 0:
            break

    if (high_payment - low_payment < 0.005):
        # Bisection search space is small enough
        # Print result
        print "RESULT"

        # Round monthly payment up to the nearest cent
        monthly_payment = round(monthly_payment + 0.004999, 2)
        print "Monthly payment to pay off debt in 1 year:", round(monthly_payment,2)

        # Recompute remaining balance and the number of months needed
        balance = original_balance
        for month in range(1,13):
            interest = round(balance*interest_rate/12, 2)
            balance += interest - monthly_payment
            if balance <= 0:
                break
        print "Number of months needed:", month
        print "Balance:", round(balance,2)
        break
    elif balance < 0:
        #Paying too much
        high_payment = monthly_payment
    else:
        #Paying too little
        low_payment = monthly_payment
