from statistics import mean

SENTINEL: int = 0

# 11
print("ex11- sum all negative input numbers - till input 0")
sum_negatives: int = 0
l1: list[str] = []
while True:
    number = int(input("enter number:"))
    if number == SENTINEL:
        break
    if number < SENTINEL:
        l1.append(str(number))
        sum_negatives += number;
if l1:
    print(f"{("+".join(l1))}={sum_negatives}")

# 12:
print("ex12 - reverse list of 10 input numbers")
print("reverse list:", [int(input("enter number to list:")) for _ in range(10)][::-1])

# 13:
print("ex13- total count prime input numbers - till input 0")
list_prime2: list[int] = []
while True:
    x = int(input("enter prime number to list:"))
    if x == SENTINEL:
        break
    if all([x % i for i in range(2, x)]):
        list_prime2.append(x)
print("total prime numbers count:", len(list_prime2))

# 14
print("ex14- count bigger average 5 input numbers")
l14: list[int] = [int(input("enter number to list:")) for _ in range(5)]
avg = None
if l14 and avg is None:
    avg = mean(l14)
    print(f"The were {len([x for x in l14 if x > avg])} bigger then the average: {avg}")

# 15:
print("ex15-Dividing numbers using subtractions")
number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))
bigger, smaller = number2, number1
if number1 > number2:
    bigger, smaller = number1, number2
ex:str = f"{bigger}/{smaller}"
result = 0
while bigger > 0:
    result += 1
    bigger -= smaller
print(f"{ex}={result}")
