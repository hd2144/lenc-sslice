#Make Some Pizzas
#1. To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
topping = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms" ]
print(topping)
#2. To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
prices = ["2", "6", "1", "3", "2", "7", "2"]
print(prices)
toppingPrices = [[topping[0], prices[0]], [topping[1], prices[1]], [topping[2], prices[2]], [topping[3], prices[3]], [topping[4], prices[4]], [topping[5], prices[5]], [topping[6], prices[6]]]
print(toppingPrices)
#3. Your boss wants you to do some research on $2 slices. Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices. Print it out
num_two_dollar_slices = toppingPrices[0:1] + toppingPrices[4:5] + toppingPrices[6:7]
print(num_two_dollar_slices)
size = len(num_two_dollar_slices)
print(size)
#4. Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(topping)
print(num_pizzas)
#5. Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
num_pizzas = len(topping)
print("We sell "+str(num_pizzas)+" different kinds of pizzas!")
#6. Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.Each sublist in pizza_and_prices should have one pizza topping and an associated price.
#Price	Topping
#2	"pepperoni"
#6	"pineapple"
#1	"cheese"
#3	"sausage"
#2	"olives"
#7	"anchovies"
#2	"mushrooms"
#For this new list make sure the prices come before the topping name like so:
#[price, topping_name]
#Note: You don’t need to use your original toppings and prices lists in this exercise. Create a new two-dimensional list from scratch.
#7. Print pizza_and_prices.
pizza_and_prices = [2, "Pepperoni"], [6, "pineapple"],[1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]
print(pizza_and_prices)
#Sorting and Slicing Pizzas. 
#8. Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending)
pizza_and_prices = list(zip(prices, topping))
print(pizza_and_prices)
pizza_and_prices.sort()
print(pizza_and_prices)
#9. Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[6]
print(priciest_pizza)
#11. It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.remove(priciest_pizza)
print(pizza_and_prices)
#12. Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:
#[2.5, "peppers"]
#Add the new peppers pizza topping to our list pizza_and_prices.
pizza_and_prices.insert(2,"(2.5, 'peppers')")
print(pizza_and_prices)
#13. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.
#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = [pizza_and_prices[0]], [pizza_and_prices[1]], [pizza_and_prices[2]]
print(three_cheapest)