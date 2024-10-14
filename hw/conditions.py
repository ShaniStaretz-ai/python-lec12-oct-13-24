# 1


number1: float = float(input("enter a number:"))
print(number1)
if number1 > 10:
    print("#1 :", 10 - number1)
else:
    print("#1:", 10 * number1)
# 2

l_sum: list[float] = [float(input("enter a number:")) for _ in range(3)]
sum_nums: float = sum(l_sum)
if sum_nums > 100:
    print(f"#2: the sum is {sum_nums}")
else:
    print(f"#2:sum {sum_nums} is smaller than 100")

# 3
number2: float = float(input("enter a number:"))
number3: float = float(input("enter a number:"))
diff2: float = number2 - int(number2)
diff3: float = number3 - int(number3)
print(f"#3:{"equals" if diff2 == diff3 else (diff2 if diff2 > diff3 else diff3)}")

# 4
x: int = int(input("enter age between 0-120:"))
print(f" #4:the age is {x}" if 0 < x < 120 else "#4: invalid age")

# 5
y: int = int(input("enter number with 3 digits:"))
print(f"#5:{y // 10 % 10}")
