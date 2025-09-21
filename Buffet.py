foods = ('Butter chicken', 'Mutton biryani', 'Smash Burger', 'Daal and rice', 'Egg bhurji')
print("The menu of the resturant is:")
for food in foods:
    print(food)

foods[0] = ('Mutton Nihari')

print("There has been some changes in the menu so here is the new menu:")
foods = ('Mutton ghost with less spices', 'Butter chicken', 'Mutton biryani', 'Smash burger', 'Daal and rice', 'Egg bhurji', 'Paneer bhurji')
for food in foods:
    print(food)