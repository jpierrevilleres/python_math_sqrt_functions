import math #imports math module to be able to use math.sqrt and abs function

#Part 1 defining my_sqrt function
def my_sqrt(a):     #Python code taken from Section 7.5 
	x = a / 2       #takes  as an argument and uses it to initialize value of x
	while True:     #uses while loop as mentioned in Section 7.5
		y = ( x + a / x ) / 2.0
		if y == x:
			break
		x = y
	return x        #returns an estimated square root value

#Part 2 defining test_sqrt function
def test_sqrt():
    print("a \t mysqrt(a)   \tmath.sqrt(a) \tdiff \n" + "- \t ---------   \t ------------ \t----" ) #header for the table
    a = 1.0         #initializes the value of a to 1
    while a < 26:   #uses while loop to print a value from 1 to 25
        
        #prints the values returned by my_sqrt for each value of a.
        #prints the values from math.sqrt for each value of a.
        #prints the absolute values of the differences between my_sqrt and math.sqrt for each value of a.
        print ('%(a)d	%(my_sqrt(a)).11f	%(math.sqrt(a)).11f %(diff).11g' %
		{"a": a, "my_sqrt(a)":my_sqrt(a), "math.sqrt(a)":math.sqrt(a), "diff":abs(my_sqrt(a) - math.sqrt(a))})	#computed data values for the table	     
        a = a + 1   #increments the value of a by 1 for the while loop to work

