# 16
number = int(input("enter number:"))
print(number, ': ', end='')
sum_nums = 0
while number > 0:
    sum_nums += number % 10
    print(f"{number % 10} {"+ " if number > 0 else "= "}", end="")
    number //= 10
print(f"{"divisible by 3" if sum_nums % 3 == 0 else "NOT divisible by 3"}")

# 17 - polindrom:
string1: str = input("enter word:")
length = len(string1)
i = 0
while i < length:
    if string1[i] != string1[length - 1 - i]:
        print("not Palindrome")
        break;
    i += 1
else:
    print("Palindrome")
