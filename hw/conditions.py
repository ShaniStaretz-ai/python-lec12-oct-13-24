# 1
print("ex1- diff/multiple by 10:")
number1: float = float(input("enter a number:"))

print(f"{number1} {" - " if number1 > 10 else "x"} 10 = {number1 - 10 if number1 > 10 else 10 * number1}", end=" ")
print()

# 2
print("ex2- sum is smaller then 100:")
sum_nums: float = sum([float(input("enter a number:")) for _ in range(3)])
print(f"The sum is {sum_nums} {"" if sum_nums > 100 else "is smaller than 100"}")

# 3
print("ex3 - diff fractions:")
number2: float = float(input("enter a decimal number:"))
number3: float = float(input("enter a decimal number:"))
fraction2: float = number2 - int(number2)
fraction3: float = number3 - int(number3)
print(
    f"{"Equal fractions" if fraction2 == fraction3 else (f"{fraction2} is bigger" if fraction2 > fraction3 else f"{fraction3} is bigger")}")

# 4
print("ex4- valid age:")
x: int = int(input("enter age between 0-120:"))
print(f" The age is {x}" if 0 < x < 120 else f"Invalid age {x}")

# 5
print("ex5- middle digit:")
while True:
    try:
        y: int = int(input("enter number with 3 digits:"))
        if y < 100:
            raise ValueError("invalid,try again")
        break;
    except ValueError as e:
        print(e)
print(f"For number {y} the middle digit is:{y // 10 % 10}")
