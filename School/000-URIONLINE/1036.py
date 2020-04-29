#input Program
from math import sqrt
a, b, c = input().split()

a,b,c = float(a), float(b), float(c)

#proses Program
Bhaskara = (b**2-4*a*c) #diskriminan
if Bhaskara < 0 or a==0:
	#output Program
	print("Impossivel calcular")
else:
	R1 = (-b+sqrt(Bhaskara))/(2*a)
	R2 = (-b-sqrt(Bhaskara))/(2*a)
	print("R1 = %.5f" % (R1))
	print("R2 = %.5f" % (R2))