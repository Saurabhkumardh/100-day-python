from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine= MoneyMachine()

is_on=True
menu=Menu()
while is_on:
    
    option=menu.get_items()
    choice=input(f"What would you like? {option}:").lower()
    if choice=='report':
        coffee_maker.report()
        money_machine.report()
    elif choice=='off':
        is_on=False
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


