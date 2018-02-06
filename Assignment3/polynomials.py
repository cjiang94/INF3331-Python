class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with
        the i-th element being the coefficient a_i."""

        self.coefficients = coefficients

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""

        length = len(self.coefficients) - 1

        while (length >= 0):
            if (self.coefficients[length] != 0):
                return length
            length-=1
        return -1

    def coefficients(self):
        """Return the list of coefficients.

        The i-th element of the list should be a_i, meaning that the last
        element of the list is the coefficient of the highest degree term."""

        return self.coefficients

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""

        length = len(self.coefficients) - 1
        result = 0

        for i in range(length+1):
            result += (self.coefficients[i] * (x**i))

        return result


    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        new_list = []
        length_short = 0
        length_long = 0

        if isinstance(p, (int, Polynomial)):
            if len(self.coefficients) > len(p.coefficients):
                length_long = len(self.coefficients)
                length_short = len(p.coefficients)
                longest = self.coefficients
            else:
                length_long = len(p.coefficients)
                length_short = len(self.coefficients)
                longest = p.coefficients

            for i in range(length_short):
                new_list.append(self.coefficients[i] + p.coefficients[i])
            new_list += longest[length_short:]

        else:
            raise ArithmeticError

        return Polynomial(new_list)

    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""

        if isinstance(p, (int, Polynomial)):
            poly_1 = (p*-1)
            poly_2 = (poly_1 + self)
            return poly_2
        else:
            raise ArithmeticError


    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""

        new_list = self.coefficients[:]
        length = len(new_list)

        if isinstance(c, int):
            for i in range(length):
                new_list[i] = new_list[i] * c
        else:
            raise ArithmeticError

        return Polynomial(new_list)

    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        new_list3 = self.coefficients[:]
        length = len(new_list3)

        if isinstance(c, int):
            for i in range(length):
                new_list3[i] = new_list3[i] * c
        else:
            raise ArithmeticError

        return Polynomial(new_list3)

    def __repr__(self):
        """Return a nice string representation of polynomial.

        E.g.: x^6 - 5x^3 + 2x^2 + x - 1"""
        counter = 0
        result = ""
        first = True
        second = True

        for num in self.coefficients:
            if first:
                result = str(num) + result
                first = False
                counter += 1
            elif second:
                result = str(num) + "x" + " + " + result
                second = False
                counter += 1
            elif num != 0:
                result = str(num) + "x^{0}".format(counter) + " + " + result
                counter += 1
            else:
                counter += 1

        return result

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

        new_list1 = self.coefficients[:]
        new_list2 = p.coefficients[:]

        while new_list1[-1] == 0:
            if len(new_list1) == 1:
                break
            else:
                del new_list1[-1]

        while new_list2[-1] == 0:
            if len(new_list2) == 1:
                break
            else:
                del new_list2[-1]

        return new_list1 == new_list2

    def sample_usage():
        p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
        q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


        print("The value of {} at {} is {}".format(p, 7, p(7)))

        print("The coefficients of {} are {}".format(p, p.coefficients()))


        print("\nAdding {} and {} yields {}".format(p, q, p+q))

        p, q, r = map(Polynomial,
                      [
                          [1, 0, 1], [0, 2, 0], [1, 2, 1]
                      ]
        )

        print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
            p, q, r, p+q == r
        ))
        print("\nIs {} - {} the same as {}? Answer: {}".format(
            p, q, r, p-q == r
        ))
