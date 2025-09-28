# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
availabe_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pinapple', 'extra cheese')
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers', 'french fires']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')

# print("\nFinished making your pizza!")

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'Pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')
# print("\nFinished making your pizza")
# if requested_toppings:
#     for toppings in requested_toppings:
#         if toppings == 'green peppers':
#             print("Sorry, we are out of green peppers right now.")
#         else:
#             print(f"Adding {toppings}.")
# print("\nFinished making your pizza!")

for toppings in requested_toppings:
    if toppings in availabe_toppings:
        print(f"Adding {toppings}.")
    else:
        print(f"Sorry, we don't have {toppings}.")
print("\nFinished making your pizza!")