name = "Swaraj"
name1 = "Swaraj"
print(name == name1)

name3 = "Tanishq"
print(name == name3)

print(name.lower())

num = 10
num1 = 20
print(num == num1)
if(num >= num1):
    print(num)
else:
    print(num1)

if(num<= num1):
    print(num)
else:
    print(num1)

if num >= num1 or num<=num1:
    print(True)

if num<=num1 and num == name3:
    print(True)
else:
    print("nan")


food = ['Paneer', 'chicken']
if 'Mutton' in food:
    print("Mutton in food")
else:
    print('Mutton not in food')

if "Paneer" not in food:
    print("Paneer is not in food")
else:
    print("Paneer is in food")
