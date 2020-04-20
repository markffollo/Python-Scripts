## This script makes lists and performs various actions on lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

## Combine two lists together
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
## Choose an index within a list
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[0:3]
print(three_cheapest)

num_two_dollar_slices = pizzas.count(2)
print(num_two_dollar_slices)
