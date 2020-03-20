#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: test.py
# First Edit: 2020-03-19
# Last Change: 19-Mar-2020.
"""
This scrip is for test

"""

amount_dict = {"high": 1.2, "normal": 1.0, "low": 0.8}


def main():
    factorya = AbstractPizzaFactory(PizzaFactoryA())
    pizza1 = factorya.make_pizza("high")
    pizza1.check_pizza()

    print("-----")

    factoryb = AbstractPizzaFactory(PizzaFactoryB())
    pizza2 = factoryb.make_pizza("normal")
    pizza2.check_pizza()


# AbstractFactory
class AbstractPizzaFactory:
    def __init__(self, pizza_factory, amount_str="normal"):
        self.factroy = pizza_factory

    def make_pizza(self, amount_str):
        amount = amount_dict[amount_str]
        self.pizza_materials = []
        self.pizza_materials.append(self.factory.add_dough(amount))
        self.pizza_materials.append(self.factory.add_source(amount))
        self.pizza_materials.append(self.factory.add_topping(amount))

    def check_pizza(self):
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    # createproduct
    def add_dough(self, amount=1):
        pass

    # createproduct
    def add_source(self, amount=1):
        pass

    # createproduct
    def add_topping(self, amount=1):
        pass


# ConcreteFactory
class PizzaFactoryA(AbstractPizzaFactory):
    def __init__(self):
        pass

    # createproduct
    def add_dough(self, amount=1):
        return WheatDough(amount)

    # createproduct
    def add_source(self, amount=1):
        return TomatoSource(amount)

    # createproduct
    def add_topping(self, amount=1):
        return CoanTopping(amount)


# ConcreteFactory
class PizzaFactoryB(AbstractPizzaFactory):
    def __init__(self):
        pass

    # createproduct
    def add_dough(self, amount=1):
        return RiceFlourDough(amount)

    # createproduct
    def add_source(self, amount=1):
        return BasilSource(amount)

    # createproduct
    def add_topping(self, amount=1):
        return CheeseTopping(amount)


# この場合は__init__は共通のため、子クラスでは__init__しません。
# ConcreteProduct
class Dough:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass


# ConcreteProduct
class WheatDough(Dough):
    def check(self):
        print("Wheat(amount: {})".format(self.amount))


# ConcreteProduct
class RiceFlourDough(Dough):
    def check(self):
        print("FlourDough(amount: {})".format(self.amount))


# ConcreteProduct
class Source:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass


# ConcreteProduct
class TomatoSource(Source):
    def check(self):
        print("Tomato(amount: {})".format(self.amount))


# ConcreteProduct
class BasilSource(Source):
    def check(self):
        print("Basil(amount: {})".format(self.amount))


# ConcreteProduct
class Topping:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass


# ConcreteProduct
class CoanTopping(Topping):
    def check(self):
        print("Coan(amount: {})".format(self.amount))


# ConcreteProduct
class CheeseTopping(Topping):
    def check(self):
        print("Cheese(amount: {})".format(self.amount))


if __name__ == "__main__":
    main()
