
reference_number = 0
x = [1, 34, 56, 67, 8, 0]
for number in x:
    if number > reference_number:
        reference_number = number
        print(reference_number)
print("The Largest Number is: ", reference_number)