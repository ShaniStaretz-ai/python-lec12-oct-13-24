from statistics import mean

SENTINEL: int = 0

# 11
print("ex11 - sum all negative input numbers - till input 0")
sum_negatives: int = 0
l1: list[str] = []
while True:
    number: int = int(input("enter number:"))
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
count_primes: int = 0
while True:
    x = int(input("enter prime number:"))
    if x == SENTINEL:
        break
    if all([x % i for i in range(2, x)]):
        count_primes+=1
print("total prime numbers count:", count_primes)

# 14
print("ex14- count bigger average 5 input numbers")
l14: list[int] = [int(input("enter number to list:")) for _ in range(5)]
avg = None
if l14 and avg is None:
    avg = mean(l14)
    print(f"The were {len([x for x in l14 if x > avg])} bigger then the average: {avg}")

# 15:
print("ex15 - Dividing numbers using subtractions")
result: int = 0
bigger = int(input("enter first number:"))
smaller = int(input("enter second number:"))
if smaller > bigger:
    bigger, smaller = bigger, smaller
ex: str = f"{bigger}/{smaller}"

while bigger - smaller >= 0:
    bigger -= smaller
    result += 1
if bigger:
    remain = bigger / smaller
    if remain:
        result += remain
print(f"{ex}={result}")
