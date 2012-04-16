#law-of-cosines.py
#Author: Adam J Gross
#Date: 1/25/12
#V 1.0.0
#
#This program uses the law of cosines and the Side-Side-Side congruency theorem
#to find the internal angles of the triangle, in degrees
#This is the solution of book problem 1.31
#Thursday's class is the only additional help i needed
import math
a = float(raw_input('line A= '))
b = float(raw_input('line B= '))
c = float(raw_input('line C= '))

angA = (((b)**2+(c)**2-(a)**2)/(2*c*b))
angB = (((a)**2+(c)**2-(b)**2)/(2*a*c))
angC = (((a)**2+(b)**2-(c)**2)/(2*a*b))

angA = math.degrees(math.acos(angA))
angB = math.degrees(math.acos(angB))
angC = math.degrees(math.acos(angC))

#takes the inverse cos of the formulae while converting them from rad->deg

print 'angle A= ',angA
print 'angle B= ',angB
print 'angle C= ',angC




