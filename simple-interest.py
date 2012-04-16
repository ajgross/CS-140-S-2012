#simple-interest.py
#Author: Adam J Gross
#Date: 1/25/12
#V 1.0
#
#This is the solution to book exercise 1.28
#I used no outside assistance in this problem

p = raw_input( 'Initial Product Investment: $' )
t = raw_input ( 'Years On Loan: ')
i = raw_input ('Decimal Interest: ')
B = (float(p)*float(t)*float(i))/100
print 'Total Interest= $',B
