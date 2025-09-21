my_foods = ['pizza', 'falafel', 'carrot cake', 'Pasta']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

# print("My favorite foods are: ")
# print(my_foods)

# print("\nMy friends's favorite foods are: ")
# print(friend_foods)

# 4-12 starts from here
print("My favorite foods are:")
for my in my_foods[:]:
    print(my)

print("\n")

print("My friends favourite foods are:")
for fried in friend_foods[:]:
    print(fried)