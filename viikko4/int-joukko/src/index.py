import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    print(joukko)
    joukko.lisaa(1)
    print(joukko)
    joukko.lisaa(2)
    print(joukko)
    joukko.lisaa(3)
    joukko.lisaa(2)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
