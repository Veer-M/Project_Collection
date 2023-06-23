'''
   Description: This program reads financial information and produces a payroll statement
   Input: Console input employee name, number of hours in a week, hourly pay rate, federal tax withholding rate, and state tax withholding rate
   Output: Console output given input and gross pay, federal withholding amount, state withholding amount, total deduction, and net pay
   Known bugs: Error when non-numerical value is provided for info, but error when non-string input is given for employee name
'''

name = str(input("Enter employee's name: "))
hours = float(input("Enter number of hours worked in a week: "))
payrate = float(input("Enter hourly pay rate: "))
federaltax = float(input("Enter federal tax withholding rate: "))
statetax = float(input("Enter state tax withholding rate: "))

print("")

print("Employee Name: " + str(name))
print("Hours Worked: " + str(hours))
print("Pay Rate: $" + str(round(payrate, 2)))
print("Gross Pay: $" + str(round((hours*payrate), 2)))
print("Deductions:")
print("  Federal Withholding (" + str((federaltax*100)), "%): $" + str(round((federaltax*hours*payrate), 2)))
print("  State Withholding (" + str((statetax*100)), "%): $" + str(round((statetax*hours*payrate), 2)))
print("  Total Deduction: $" + str(round((federaltax*hours*payrate+statetax*hours*payrate), 2)))
print("Net Pay: $" + str(round(hours*payrate-(federaltax*hours*payrate+statetax*hours*payrate), 2)))

'''
Enter employee's name: Veer Mistry
Enter number of hours worked in a week: 167
Enter hourly pay rate: 1.99
Enter federal tax withholding rate: 0.1
Enter state tax withholding rate: 0.01

Employee Name: Veer Mistry
Hours Worked: 167.0
Pay Rate: $1.99
Gross Pay: $332.33
Deductions:
  Federal Withholding (10.0 %): $33.23
  State Withholding (1.0 %): $3.32
  Total Deduction: $36.56
Net Pay: $295.77
'''
