
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
print("Now lets determine the minimum monthly payment needed to pay off the credit card debt within a year. ")
bal = int(raw_input("What is the outstanding balance on the card? $"))
rate = float(raw_input("What is the annual interest rate in decimal form? "))
minimumMonthlyPayment = int(10)
monthlyRate = rate/12
updatedBalance = bal * (1+monthlyRate) - minimumMonthlyPayment
numberGuesses = 0
