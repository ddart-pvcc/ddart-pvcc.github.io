# Name: Dwight Dart
# Prog Purpose: This program computes gross pay, deductions, and net pay based
#   on the number of hours they worked and their job category.
#
#       Category Codes and Pay Rates
#       C   Cashier:        $16.50 - Position 0 in pay_rates tuple
#       S   Stocker:        $15.75 - Position 1 in pay_rates tuple
#       J   Janitor:        $15.75 - Position 2 in pay_rates tuple
#       M   Maintenance:    $19.50 - Position 3 in pay_rates tuple
#       
#       Deduction Rates
#       Federal Income Tax Rate:    12%   - Position 0 in deduction_rates tuple
#       State Income Tax Rate:      3%    - Position 1 in deduction_rates tuple
#       Social Security Tax Rate:   6.2%  - Position 2 in deduction_rates tuple
#       Medicare Tax Rate:          1.45% - Position 3 in deduction_rates tuple    

import datetime

#use tuples to define pay and deduction rates
pay_rates = (16.50, 15.75, 15.75, 19.50)
deduction_rates = (.12, .03, .062, .0145)

#define global variables
pay_rate = 0
gross_pay = 0
fed_tax = 0
state_tax = 0
ss_tax = 0
med_tax = 0
total_deductions = 0
net_pay = 0
job_cat = ""
job_title = ""
hours_worked = 0

def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('Would you like to calculate weekly pay for another employee? (Y/N): ')
        if yesno.upper() != "Y":
            another_employee = False

def get_user_data():
    global job_cat, job_title, hours_worked, pay_rate
    
    print('\nJob Category Codes: ', 'C: Cashier', 'S: Stocker', 'J: Janitor', 'M: Maintenance\n')
    
    job_cat = input("Please input your job category code (C, S, J, M): ")
    hours_worked = int(input("How many hours did you work this week?: "))
    
    if job_cat.upper() == 'C':
        pay_rate = pay_rates[0]
        job_title = 'Cashier'
    if job_cat.upper() =='S':
        pay_rate = pay_rates[1]
        job_title = 'Stocker'
    if job_cat.upper() =='J':
        pay_rate = pay_rates[2]
        job_title = 'Janitor'
    if job_cat.upper() == 'M':
        pay_rate = pay_rates[3]
        job_title = 'Maintenance'


def perform_calculations():
    global gross_pay, pay_rate, fed_tax, state_tax, ss_tax, med_tax, total_deductions, net_pay
    gross_pay = pay_rate * hours_worked
    fed_tax = gross_pay * deduction_rates[0]
    state_tax = gross_pay * deduction_rates[1]
    ss_tax = gross_pay * deduction_rates[2]
    med_tax = gross_pay * deduction_rates[3]
    total_deductions = fed_tax + state_tax + ss_tax + med_tax
    net_pay = gross_pay - total_deductions

def display_results():
    print('\n--------------------------------------------------')
    print('          ***** FRESH FOOD MARKETPLACE *****')
    print('          ****** EMPLOYEE WEEKLY PAY *******')
    print('----------------------------------------------------')
    print('         Job Category:        ', job_title)
    print('         Pay Rate:            $', format(pay_rate,'8,.2f'))
    print('         Hours Worked:        $', format(hours_worked, '8,.2f'))
    print('----------------------------------------------------')
    print('         Gross Pay:           $', format(gross_pay, '8,.2f'))
    print('         Federal Income Tax:  $', format(fed_tax, '8,.2f'))
    print('         State Income Tax:    $', format(state_tax, '8,.2f'))
    print('         Social Security Tax: $', format(ss_tax, '8,.2f'))
    print('         Medicare Tax:        $', format(med_tax, '8,.2f'))
    print('         Total Deducations:   $', format(total_deductions, '8,.2f'))
    print('----------------------------------------------------')
    print('         Net Pay:             $', format(net_pay, '8,.2f'))
    print('----------------------------------------------------')
    print('            ' + str(datetime.datetime.now()) + '\n')
main()