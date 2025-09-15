motorcycles = [];
motorcycles.insert(0, 'honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
too_expensive = 'ducati';
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too_expensive for me.")
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)