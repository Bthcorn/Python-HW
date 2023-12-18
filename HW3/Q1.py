name = input("Enter employee's name: ")
hour = float(input("Enter number of hours worked in a week: "))
payrate = float(input("Enter hourly pay rate: "))
ftax = float(input("Enter federal tax withholding rate: "))
stax = float(input("enter state tax withholding rate: "))
grosspay= hour*payrate
federal= ftax*grosspay
state= stax*grosspay
deduct =federal+state
print("Employee Name: ", name)
print("Hourly Worked: ", hour)
print("Pay Rate: " + "$" +str(payrate))
print("Gross Pay: " +"$"+ str(grosspay))
print("Deduction: ")
print("  Federal Withholding " + "("+ str(ftax*100) +"%"+ ") : " + "$" + str(format(federal, ".1f")))
print("  State Withholding " + "("+ str(stax*100) +"%" +") : " + "$" + str(format(state, ".2f")))
print("  Total Deduction : " + "$" + str(format(deduct, ".2f")))
print("Net Pay : " +"$"+ str(format(grosspay-deduct, ".2f")))