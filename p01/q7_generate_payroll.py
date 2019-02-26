'''Write a program q7_generate_payroll.py that reads the following information and prints a payroll statement. A sample input and output session is as follows:

Sample input:

Enter name: Lim Ah Seng
Enter number of hours worked weekly: 10
Enter hourly pay rate: 6.75
Enter CPF contribution rate(%): 20

Sample output:

Payroll statement for Lim Ah Seng
Number of hours worked in week: 10
Hourly pay rate: $6.75
Gross pay = $67.50
CPF contribution at 20% = $13.50
Net pay = $54.00'''

name = input('Enter name: ')
hours = float(input('Enter number of hours worked weekly: '))
rte = float(input('Enter hourly pay : '))
cpf = float(input('Enter CPF contribution rate (%): '))
pay = hours*rte
cpf_tot = pay*(cpf/100)
net_pay = pay - cpf_tot
rate_u = ['$' + str('{0:.2f}'.format(rate))]
cpf_u = [str(int(cpf)) + '%']
pay_u = ['$'+ str('{0:.2f}'.format(pay))]
cpf_tot_u = ['$'+ str('{0:.2f}'.format(cpf_tot))]
net_pay_u = ['$'+ str('{0:.2f}'.format(net_pay))]
print('Payroll statement for '+str(name))
print('Number of hours worked in a week:'+ str(int(hours)))
print('Hourly pay rate: ',''.join(map(str, rate_u)))
print('Gross pay = ', ''.join(map(str, pay_u)))
print('CPF contribution at', ''.join(map(str, cpf_u)),'=', ''.join(map(str,cpf_tot_u)))
print('Net pay = ',''.join(map(str, net_pay_u)))
