numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if numbers:
    for nums in numbers:
        if nums == 1:
            print(f"{nums}st")
        elif nums == 2:
            print(f"{nums}nd")
        elif nums == 3:
            print(f"{nums}rd")
        else:
            print(f"{nums}th")
else:
    print("Please! enter the number cause list is empty")