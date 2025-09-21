Pizza_list = ['Margerita pizza', 'Napoli authentic pizza', 'Mutton peperoni pizza']
for pizza in Pizza_list:
    print(f"I like {pizza.title()}")
print("My love for pizza is indispencible")

friend_pizzas = Pizza_list[:]

Pizza_list.append('Paneer Pizza')

friend_pizzas.append('Farmhouse pizza')

print(f"My favourite pizzas are:")
for pizza in Pizza_list[:]:
    print(pizza)
print("\n")
print(f"My friends favourite pizzas are:")
for pizza1 in friend_pizzas[:]:
    print(pizza1)