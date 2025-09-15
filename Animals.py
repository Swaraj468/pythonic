Animals_with_common_characteristics = ['Dog', 'Wolf', 'Jackal']
for animals in Animals_with_common_characteristics:
    print(f"A {animals} would make a great pet")
    break;
Animals_with_common_characteristics.pop(0)
# print(Animals_with_common_characteristics)
for animal1 in Animals_with_common_characteristics:
    print(f"A {animal1} would not make a great pet")
print("All of these animal have 4 legs can bark and they are mammal")