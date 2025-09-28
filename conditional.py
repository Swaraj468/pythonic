car = 'subaru'
if car == 'subaru':
    print(car == 'subaru')
else:
    print("Nothing")

food = ['Paneer', 'Mutton', 'Egg', 'Pizza']
food1 = 'Biryani'
if food1 in food:
    print(f"I love {food1.title()}!")
else:
    print(food)

age_1 = 19
age_2 = 20
if age_1 >= 18 and age_2 >= 20:
    print(True)
else:
    print(False)

mouse = ['Razer', 'Logitech', 'AntEsports']
mouse1 = 'Razer'
if mouse1 in mouse:
    print(True)
else:
    print(False)


age_0 = 23
age_3 = 19

if age_0 >= 22 or age_3 > 20:
    print(True)
else:
    print(False)


water_Tank = 'Empty'
if water_Tank == 'Empty':
    print(True)
    print('Fill the water tank')
else:
    print("The water is not empty")


number = [1, 3, 5, 7, 9]
for num in number:
    if(num % 2 == 0):
        print(True)
        print("The numbers are even")
else:
    print('The numbers are Odd')


age_10 = 22;
age_11 = 22;
print(age_10 != age_11)

food = 'Margerita Cake'
print("Is food == 'Margerita Pizza' ? I predict False")
print(food == 'Margerita Pizza')

print("\n food == 'Mutton Biryani' ? I predict False")
print(food == 'Mutton Biryani')

name = 'Swaraj'
name1 = 'Tanishq'
print(name == name1)