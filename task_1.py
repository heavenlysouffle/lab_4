import math


class Rational:
    """Class for performing arithmetic with fractions"""

    def __init__(self, num=0, denom=1):
        """Method that creates an object of Rational and initialises it with numerator and denumerator"""
        if not isinstance(num, int) or not isinstance(denom, int):
            raise TypeError("Numerator and denominator must be of integer type")
        if not denom:
            raise ZeroDivisionError
        self.__num = num // math.gcd(num, denom)
        self.__denom = denom // math.gcd(num, denom)

    def fraction(self):
        """Method that returns Rational in form numerator/denominator"""
        return f'{self.__num} / {self.__denom}'

    def result(self):
        """Method that returns Rational in floating-point format"""
        return self.__num / self.__denom

    def __set__(self, other):
        """Method that performs Rational = other (Rational, int)"""
        if not isinstance(other, Rational):
            raise TypeError("For Rational operations with int or other Rational are supported")
        self.__num = other.__num
        self.__denom = other.__denom

    def __add__(self, other):
        """Method that performs Rational + other (Rational, int)"""
        if isinstance(other, Rational):
            result_num = self.__num * other.__denom + other.__num * self.__denom
            result_denom = self.__denom * other.__denom
            return Rational(result_num, result_denom)
        if isinstance(other, int):
            result_num = self.__num + other * self.__denom
            return Rational(result_num, self.__denom)
        raise TypeError("This operator support as operands Rational with int or another Rational")

    def __sub__(self, other):
        """Method that performs Rational - other (Rational, int)"""
        if isinstance(other, Rational):
            result_num = self.__num * other.__denom - other.__num * self.__denom
            result_denom = self.__denom * other.__denom
            return Rational(result_num, result_denom)
        if isinstance(other, int):
            result_num = self.__num - other * self.__denom
            return Rational(result_num, self.__denom)
        raise TypeError("This operator support as operands Rational with int or another Rational")

    def __mul__(self, other):
        """Method that performs Rational * other (Rational, int)"""
        if isinstance(other, Rational):
            return Rational(self.__num * other.__num, self.__denom * other.__denom)
        if isinstance(other, int):
            return Rational(self.__num * other, self.__denom * other)
        raise TypeError("This operator support as operands Rational with int or another Rational")

    def __truediv__(self, other):
        """Method that performs Rational / other (Rational, int)"""
        if isinstance(other, Rational):
            if not other.result():
                raise ZeroDivisionError("Divider cannot be 0")
            return Rational(self.__num * other.__denom, self.__denom * other.__num)
        if isinstance(other, int):
            if not other:
                raise ZeroDivisionError("Divider cannot be 0")
            return Rational(self.__num, self.__denom * other)
        raise TypeError("This operator support as operands Rational with int or another Rational")

    def __floordiv__(self, other):
        """Method that performs Rational // other (Rational, int)"""
        return Rational(round(self.__truediv__(other).result()), 1)

    def __lt__(self, other):
        """Method that performs Rational < other (Rational, float, int)"""
        if isinstance(other, Rational):
            if self.__num * other.__denom < other.__num:
                return True
            return False
        if isinstance(other, (int, float)):
            if self.__num < other * self.__denom:
                return True
            return False
        raise TypeError("This operator support as operands Rational with int, float or another Rational")

    def __gt__(self, other):
        """Method that performs Rational > other (Rational, float, int)"""
        if self.__lt__(other):
            return False
        return True

    def __le__(self, other):
        """Method that performs Rational <= other (Rational, float, int)"""
        if isinstance(other, Rational):
            if self.__num * other.__denom <= other.__num:
                return True
            return False
        if isinstance(other, (int, float)):
            if self.__num <= other * self.__denom:
                return True
            return False
        raise TypeError("This operator support as operands Rational with int, float or another Rational")

    def __ge__(self, other):
        """Method that performs Rational >= other (Rational, float, int)"""
        if isinstance(other, Rational):
            if self.__num * other.__denom >= other.__num:
                return True
            return False
        if isinstance(other, (int, float)):
            if self.__num >= other * self.__denom:
                return True
            return False
        raise TypeError("This operator support as operands Rational with int, float or another Rational")

    def __eq__(self, other):
        """Method that performs Rational == other (Rational, float, int)"""
        if isinstance(other, Rational):
            if self.__num * other.__denom == other.__num:
                return True
            return False
        if isinstance(other, (int, float)):
            if self.__num == other * self.__denom:
                return True
            return False
        raise TypeError("This operator support as operands Rational with int, float or another Rational")

    def __ne__(self, other):
        """Method that performs Rational != other (Rational, float, int)"""
        if self.__eq__(other):
            return False
        return True


if __name__ == '__main__':
    object1 = Rational(2, 4)
    print(object1.fraction())
    object2 = Rational(1, 5)
    print(object2.fraction())
    print((object1 + object2).fraction())
    print(object1.fraction())
    object1 += object2
    print(object1.fraction())
    object1 -= object2
    print(object1.fraction())
    object1 *= object2
    print(object1.fraction())
    object1 /= object2
    print(object1.fraction())
    object1 //= object2
    print(f'{object1.fraction()} = {object1.result()}')
    print(object1 == 1)
