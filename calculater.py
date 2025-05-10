class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero!"

# Example usage
calc = Calculator()
print(calc.add(10, 5))        # 15
print(calc.divide(10, 0))     # Cannot divide by zero!