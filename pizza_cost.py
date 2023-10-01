#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: September 28, 2023
# This program calculates the price of a pizza

import constants


def main():
    # get the diameter
    print("Calculating Price of a Pizza")
    diameter = int(input("What is the diameter of your desired pizza (in)?"))

    # calculate the subtotal, tax, and total cost
    subtotal = (
        constants.INGREDIENTS_COSTS * diameter
        + constants.LABOR_COSTS
        + constants.RENTAL_COSTS
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # display the total cost
    print("Your total cost is ${:.2f}.".format(total))


if __name__ == "__main__":
    main()
