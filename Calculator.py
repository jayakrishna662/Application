class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def sqrt(self, a):
        if a < 0:
            return "Error: Cannot compute square root of negative number"
        return a ** 0.5


def main():
    calc = Calculator()
    
    print("=== Simple Calculator ===")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"√16 = {calc.sqrt(16)}")


if __name__ == "__main__":
    main()