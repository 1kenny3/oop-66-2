rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    def convert_to_kgs(self):
        """Переводит текущую валюту в сомы (KGS)"""
        return self.amount * rates[self.currency]

    def __str__(self):
        """Красивый вывод объекта"""
        if isinstance(self.amount, float) and self.amount.is_integer():
            return f"{int(self.amount)} {self.currency}"
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        """Сложение денег: money1 + money2"""
        if not isinstance(other, Money):
            raise TypeError("Складывать можно только объекты класса Money")
        
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __sub__(self, other):
        """Вычитание денег: money1 - money2"""
        if not isinstance(other, Money):
            raise TypeError("Вычитать можно только объекты класса Money")
        
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        
        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __mul__(self, number):
        """Умножение денег на число: money * 3"""
        if not isinstance(number, (int, float)):
            raise TypeError("Умножать можно только на число (int или float)")
        
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number):
        """Деление денег на число: money / 2"""
        if not isinstance(number, (int, float)):
            raise TypeError("Делить можно только на число (int или float)")
        if number == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
            
        return Money(self.amount / number, self.currency)



if __name__ == "__main__":
    money1 = Money(100, "USD")
    money2 = Money(5000, "KGS")
    
    print(f"Первая сумма: {money1}")
    print(f"Вторая сумма: {money2}")
    print("-" * 30)

    result_add = money1 + money2
    print(f"Сложение (money1 + money2): {result_add}")

    result_sub = money1 - money2
    print(f"Вычитание (money1 - money2): {result_sub}")

    result_mul = money1 * 3
    print(f"Умножение (money1 * 3): {result_mul}")

    result_div = money2 / 2
    print(f"Деление (money2 / 2): {result_div}")