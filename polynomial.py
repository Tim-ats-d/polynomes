#  polynomial.py
#
#  Copyright 2020 Timéo Arnouts <dogm@dogm-s-pc>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import math


class CalculationNotPossible(Exception):
    pass


def introduction_text():
    print("=================")
    print("CALCUL POLYNOMIAL")
    print("=================")

    print("\nThe shape of a polynomial of the second degree corresponds to: ax^2 + bx + c, enter a, b and c values :")


def ask_valor():
    return int(input("a = ")), int(input("b = ")), int(input("c = "))


def delta_calculation(a: int, b: int, c: int):
    return pow(b, 2) - 4*a*c


def non_negative_number_check(nb: int):
    """Check if given number was not nul"""
    if nb <= 0:
        raise CalculationNotPossible("The value of A must be greater than 0.")

def main():
    introduction_text()

    val_a, val_b, val_c = ask_valor()
    non_negative_number_check(val_a)

    delta = delta_calculation(val_a, val_b, val_c)
    print("\nDiscriminant value: %s\n" % delta)

    if delta > 0:
        sol_x1 = (-val_b + math.sqrt(delta))/(2*val_a)
        sol_x2 = (-val_b - math.sqrt(delta))/(2*val_a)

        alpha = -val_B/2*val_A
        beta = -delta/4*val_A

        print("Polynome have two solutions : x1 = %s and x2 = %s", sol_x1, sol_x2);

        print("Canonical form: %s(x - %s)^2 + %s"  % (val_a, alpha, beta))
        print("Factorized form: %s(x - %s)(x - %s)" % (val_a, sol_x1, sol_x2))
    elif delta < 0:
        print("Polynome haven't solutions in real number")
        print("No need to display the factorized form")
    elif delta == 0:
        sol_x0 = -val_b/2*val_a

        alpha = sol_x0
        beta = -delta/4*val_a

        print("Polynome have one solutions : x0 = %s", sol_x0);

        print("Canonical form: %s(x - %s)^2 + %s" % (val_a, alpha, beta))
        print("Factorized form: %s(x - %s)^2" % (val_a, sol_x0))


if __name__ == "__main__":
    main()
