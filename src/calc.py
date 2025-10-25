class Calculator:
    def add(self, a: int | float, b: int | float) -> int | float:
        return a + b

    def divide(self, a: int | float, b: int | float) -> float:
        if b == 0:
            raise ValueError("division by zero")
        return a / b
