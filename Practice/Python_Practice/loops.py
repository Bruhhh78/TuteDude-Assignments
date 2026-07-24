# For-Loop
a= int(input("Enter how many time you want Hey:- "))
for a in range (0,a):
  a=a+1
  print("Hey",a)

#Table using for Loop
num = int(input("Which Table You Want to Print:- \n"))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# While-Loop

count = int(input("Enter Count Number"))

while count >= 1:
    print(count)
    count -= 1

print("Blast Off! 🚀")

# Sum of First 10 Numbers using While Loop

i = 1
sum = 0

while i <= 10:
    sum += i
    i += 1

print("Sum of First 10 Natural Number is:- ", sum)

