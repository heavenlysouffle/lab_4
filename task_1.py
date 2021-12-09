import math


class Rational:
    """Class for performing arithmetic with fractions"""
    def __init__(self, num=0, denom=1):
        """Method that creates an object of Rational and initialises it with numerator and denominator"""
        self.num = num
        self.denom = denom
        self.reduce()

    @property
    def num(self):
        return self.__num

    @property
    def denom(self):
        return self.__denom

    @num.setter
    def num(self, num):
        if not isinstance(num, int):
            raise TypeError("Numerator and denominator must be of integer type")
        self.__num = num

    @denom.setter
    def denom(self, denom):
        if not isinstance(denom, int):
            raise TypeError("Numerator and denominator must be of integer type")
        if not denom:
            raise ZeroDivisionError

    def reduce(self):
        """Method that reduces numerator and denominator"""
        rational_gcd = math.gcd(self.__num, self.__denom)
        self.__num //= rational_gcd
        self.__denom //= rational_gcd

    def fraction(self):
        """Method that returns Rational in form numerator/denominator"""
        return f'{self.__num} / {self.__denom}'

    def result(self):
        """Method that returns Rational in floating-point format"""
        return self.__num / self.__denom

    def __set__(self, other):
        """Method that performs Rational = other (Rational, int)"""
        if not isinstance(other, Rational):
            return NotImplemented
        self.__num = other.__num
        self.__denom = other.__denom
        self.reduce()

    def __add__(self, other):
        """Method that performs Rational + other (Rational, int)"""
        if isinstance(other, Rational):
            result_num = self.__num * other.__denom + other.__num * self.__denom
            result_denom = self.__denom * other.__denom
            return Rational(result_num, result_denom)
        if isinstance(other, int):
            result_num = self.__num + other * self.__denom
            return Rational(result_num, self.__denom)
        return NotImplemented

    def __iadd__(self, other):
        if not isinstance(other, (Rational, int)):
            return NotImplemented
        """Method that performs Rational += other (Rational, int)"""
        if isinstance(other, Rational):
            self.__num = self.__num * other.__denom + other.__num * self.__denom
            self.__denom = self.__denom * other.__denom
        if isinstance(other, int):
            self.__num = self.__num + other * self.__denom
            self.__denom = self.__denom
        self.reduce()
        return self

    def __sub__(self, other):
        """Method that performs Rational - other (Rational, int)"""
        if isinstance(other, Rational):
            result_num = self.__num * other.__denom - other.__num * self.__denom
            result_denom = self.__denom * other.__denom
            return Rational(result_num, result_denom)
        if isinstance(other, int):
            result_num = self.__num - other * self.__denom
            return Rational(result_num, self.__denom)
        return NotImplemented

    def __isub__(self, other):
        """Method that performs Rational -= other (Rational, int)"""
        if not isinstance(other, (Rational, int)):
            return NotImplemented
        if isinstance(other, Rational):
            self.__num = self.__num * other.__denom - other.__num * self.__denom
            self.__denom = self.__denom * other.__denom
        if isinstance(other, int):
            self.__num = self.__num - other * self.__denom
            self.__denom = self.__denom
        self.reduce()
        return self

    def __mul__(self, other):
        """Method that performs Rational * other (Rational, int)"""
        if isinstance(other, Rational):
            return Rational(self.__num * other.__num, self.__denom * other.__denom)
        if isinstance(other, int):
            return Rational(self.__num * other, self.__denom * other)
        return NotImplemented

    def __imul__(self, other):
        if not isinstance(other, (Rational, int)):
            return NotImplemented
        if isinstance(other, Rational):
            self.__num *= other.__num
            self.__denom *= other.__denom
        if isinstance(other, int):
            self.__num *= other
            self.__denom *= other
        self.reduce()
        return self

    def __truediv__(self, other):
        """Method that performs Rational / other (Rational, int)"""
        if isinstance(other, Rational):
            if not other.result():
                return NotImplemented
            return Rational(self.__num * other.__denom, self.__denom * other.__num)
        if isinstance(other, int):
            if not other:
                return NotImplemented
            return Rational(self.__num, self.__denom * other)
        return NotImplemented

    def __itruediv__(self, other):
        """Method that performs Rational /= other (Rational, int)"""
        if not isinstance(other, (Rational, int)):
            return NotImplemented
        if isinstance(other, Rational):
            if not other.result():
                return NotImplemented
            self.__num *= other.__denom
            self.__denom *= other.__num
        if isinstance(other, int):
            if not other:
                return NotImplemented
            self.__denom *= other
        self.reduce()
        return self

    def __floordiv__(self, other):
        """Method that performs Rational // other (Rational, int)"""
        return Rational(round(self.__truediv__(other).result()), 1)

    def __ifloordiv__(self, other):
        if not isinstance(other, (Rational, int)):
            return NotImplemented
        self.__num = round(self.__truediv__(other).result())
        self.__denom = 1
        return self

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
        return NotImplemented

    def __gt__(self, other):
        """Method that performs Rational > other (Rational, float, int)"""
        return -self.__lt__(other)

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
        return NotImplemented

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
        return NotImplemented

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
        return NotImplemented

    def __ne__(self, other):
        """Method that performs Rational != other (Rational, float, int)"""
        return -self.__eq__(other)


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
