for number in range(1,10):
    print(number)

# range(stop) -> 0 up to stop-1
for i in range(5):
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)

# Counting backwards
for i in range(5, 0, -1):
    print(i)

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping over a string
for char in "python":
    print(char)

# enumerate -> index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Looping over a dictionary
student = {"name": "Venkatesh", "age": 22}
for key, value in student.items():
    print(key, value)

# break -> stop the loop early
for number in range(1, 10):
    if number == 5:
        break
    print(number)

# continue -> skip the current iteration
for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number)

# for ... else -> else runs if the loop was not stopped by break
for number in range(1, 5):
    if number == 10:
        break
else:
    print("Loop finished without break")

# Nested loops (multiplication table)
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# Sum of numbers
total = 0
for number in range(1, 11):
    total += number
print("Sum:", total)


for row in range(1,5):
    for col in range(1, row+1):
        print(col, end='')
    print() 
    
print('---------') 

for row in range(4,0,-1):
    for col in range(1, row+1):
        print(col, end='')
    print()     


#while loop


# ---------- while loop ----------

# Basic while loop: runs as long as the condition is True
count = 1
while count <= 5:
    print(count)
    count += 1  # without this, the loop would never end

# Counting down
n = 5
while n > 0:
    print(n)
    n -= 1
print("Liftoff!")

# Sum of numbers until a limit
total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print("Sum:", total)

# break -> stop the loop early
n = 0
while True:  # infinite loop, stopped by break
    if n == 5:
        break
    print(n)
    n += 1

# continue -> skip the current iteration
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# while ... else -> else runs if the loop ended without break
n = 1
while n < 4:
    print(n)
    n += 1
else:
    print("Loop finished without break")

# Practical example: keep asking until the input is valid
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted")

# Digits of a number
num = 1234
digit_sum = 0
while num > 0:
    digit_sum = digit_sum + num % 10  # last digit
    num = num // 10                   # remove last digit
print("Digit sum:", digit_sum)
