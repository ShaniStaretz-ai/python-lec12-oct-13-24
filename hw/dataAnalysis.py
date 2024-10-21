from statistics import mean

SENTINEL: int = 0

# # 11
sum_negatives = 0
while True:
    number = int(input("enter number:"))
    if number == SENTINEL:
        break
    if number < SENTINEL:
        sum_negatives += number;
print("sum_negatives:", sum_negatives)

# 12:
print("reverse list:", [int(input("enter number to list:")) for _ in range(2)][::-1])

# 13:
list_prime2: list[int] = []
while True:
    x = int(input("enter prime number to list:"))
    if x == SENTINEL:
        break
    if all([x % i for i in range(2, x)]):
        list_prime2.append(x)
print("total prime numbers count:", len(list_prime2))

# 14
l14 = [int(input("enter number to list:")) for _ in range(5)]
if l14:
    mean = mean(l14)
    print("count bigger then the average: ", len([x for x in l14 if x > mean]))

# 15:
number1 = int(input("enter number:"))
number2 = int(input("enter number:"))
bigger, smaller = number2, number1
ex = f"{number2}/{number1}"
if number1 > number2:
    bigger, smaller = number1, number2
    ex = f"{number1}/{number2}"
result = 0
while bigger > 0:
    result += 1
    bigger -= smaller
print(f"the result of {ex}={result}")
