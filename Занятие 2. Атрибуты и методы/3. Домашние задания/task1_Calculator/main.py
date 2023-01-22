class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    ...  # TODO написать статические методы

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
