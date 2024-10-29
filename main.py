"""
Kveoja problem:
Channing Moor - October 2024
"""

num_int = int(input("Enter the number of integers: "))
total = 0
for i in range(num_int):
    new_int = int(input("Enter a value: "))
    total += new_int
print(total)

