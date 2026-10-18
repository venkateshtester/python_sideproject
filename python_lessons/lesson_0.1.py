marks =39
if marks >= 75:
    print('Distinction')
elif 40 <= marks <= 74:
    print('Pass')
else:
    print('Fail')


#exer-2
for n in range(1, 6):
    print(f"{n} squared is {n ** 2}")

#exer-3
programming_languages= ["Java", "Python", "SQL"]
for program in programming_languages:
    print(f"{program} has {len(program)} of characters")

#Exercise 4: indentation error

programming_languages= ["Java", "Python", "SQL"]
for program in programming_languages:
        print(f"{program} has {len(program)} of characters")

#exc 5: While loop
n=1
while n<= 5:
    print(n)
    n +=1
else:
     print('break')    

#even nos
for number in range(1, 21):
     if number % 2 == 0:
          print(number)

#sum of list
numbers =[10,20,30,50]
total =0
for number in numbers:
     total = total+number
print(total)  

#find vowels

found =[]
str="programming"
vowels= "aeiou"
count=0

for char in str:
     if char in vowels:
          found.append(char)
          count+=1;
print(count)
print(found)

#Count digits: Count how many digits are in 98765 using a while loop.

num = 98765
count =0
while num>0:
    n= num%10
    count+=1
    num = num//10;
print(count)

#Reverse the string
str= "python"
rev =""
for char in str:
     rev = char+rev
print(rev)

#Largest digit: Find the biggest digit in 48251 (answer: 8).
num = 48251
largest =0
while num >0:
    digit = num%10
    if digit > largest:
        largest = digit
    num = num//10;

print(largest)

     
     
     





