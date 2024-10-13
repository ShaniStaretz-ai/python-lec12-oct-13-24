# ternary:
# ex1
while True:
    try:
        height: float = float(input("height between 0.1-2.8:"))
        if 0.1 <= height <= 2.8:
            break
    except:
        pass

print(f"you are{"" if height > 1.8 else " not"} tall")

# ex2
while True:
    try:
        x = int(input("x between 0-99:"))
        if 0 <= x <= 99:
            break
    except:
        pass
print(f"the number {x} is {"1" if x < 10 else "2"} digits")

print(f"one line: {x} is {"negative" if x < 0 else ("positive" if x > 0 else "zero")}")
l1 = [-4, 1, 200, -3, 0, 2, -3]
l1_1 = ["negative" if x < 0 else ("positive" if x > 0 else "zero") for x in l1]
print(l1_1)

# prime numbers:
print("all primes between 2-100:")
list_prime: list[int] = []
for x in range(2, 100):
    if x == 2:
        list_prime.append(x)
        continue
    elif x % 2 == 0:
        continue
    divider = 3
    found = False
    while divider <= (x ** 0.5 + 1):
        if x % divider == 0:
            found = True
            break
        divider += 2;
    if not found:
        list_prime.append(x)
print(list_prime)

l_modules = []
list_prime2 = []
# prime numbers improve:
for x in range(2, 100 + 1):
    if all([x % i for i in range(2, x)]):
        list_prime2.append(x)
print("list_prime2:", list_prime2)
one_line = [x for x in range(2, 100 + 1) if all([x % i for i in range(2, x)])]
print("one_line:", one_line)
# swap digits
# 2 digits only
x = 97
x1 = x % 10 * 10 + 1 * x // 10
print(x1)
y = '79'
print(y[::-1])
# improve for all numbers:
x = 3784
print("before:", x)
new_x = 0
while x > 0:
    new_x *= 10
    new_x += x % 10
    x //= 10
else:
    print("new x:", new_x)

# sum digits
number = int(input("enter number:"))
print(number, ': ', end='')
sum_nums = 0
while number > 0:
    sum_nums += number % 10
    print(f"{number % 10} {"+ " if number > 0 else "= "}", end="")
    number //= 10
print(sum_nums)

