import math


class Calculator:

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def power(self, a: float, b: float) -> float:
        return a ** b

    def sqrt(self, a: float) -> float:
        if a < 0:
            raise ValueError("Square root of negative number not allowed")
        return math.sqrt(a)

    #Future extension example
    def factorial(self, n: int):
    	if n < 0:
        	raise ValueError("Factorial not defined for negative numbers")

    	if n == 0:
        	return 1

    	result = 1
    	for i in range(1, n + 1):
        	result *= i

    	return result
    
    
    
    
    def quadratic(self, a: float, b: float, c: float):
        """
        Solve ax^2 + bx + c = 0
        Returns tuple of roots
        """
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("No real roots")
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
	
	
