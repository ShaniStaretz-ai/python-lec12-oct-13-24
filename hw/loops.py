# 6
print("ex6- numbers till n")
n: int = int(input("enter number:"))
for i in range(1, n + 1):
    print(i, end=" ")
print()

# 7
print("ex7- even numbers within input numbers")
start:int = int(input("enter start number:"))
end:int = int(input("enter end number:"))
start = start if start % 2 == 0 else start + 1
for i in range(start, end + 2, 2):
    print(i, end=" ")
print()

# 8
print("ex8- all dividable by 5 or 3 till input number")
n:int = int(input("enter end number:"))
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
print()

# 9
print("ex9- all dividable by 7 till input number")
n = int(input("enter end number:"))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()
