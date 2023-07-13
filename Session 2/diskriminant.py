import math

def function(a, b, c):
	if a == 0 and b != 0:
		return -c/b
	if a == 0 and b == 0:
		return "equation is incorrect"
	D = b*b - 4*a*c
	if D > 0:
		return str((-b + math.sqrt(D))/(2*a)) + " and " + str( (-b - math.sqrt(D))/(2*a))
	if D == 0:
		return -b/(2*a)
	if D < 0:
		return "no solution"

print(function(0, 0, 2)) 
