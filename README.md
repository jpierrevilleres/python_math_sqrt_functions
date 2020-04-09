# python_math_sqrt_functions
Demonstration of Math Square Root Functions using While Loops in Python

Requirements:
* Encapsulate the below Python code in a function named `my_sqrt` that takes a as a
parameter, chooses a starting value for x, and returns an estimate of the square root of a.
```
while True:
y = (x + a/x) / 2.0
if y == x:
break
x = y
```

* Write a function named `test_sqrt` that prints a table like the following using a while loop, where "di " is the
absolute value of the di erence between `my_sqrt(a)` and `math.sqrt(a).`
