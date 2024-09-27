'''
userInput = int (input("How much money do you have? "))
wii=100
afford=int (userInput/wii)
neededMoney = abs ((userInput % wii) - wii)


print("You",userInput,"Pesos")
print("You can afford",afford,"Wii's")
print("You needed ",neededMoney,"pesos to afford a wii's")
'''

'''
sum = 0 
for x in range (1,11):
    sum = sum + x
    print("This is the sum of the numbers",sum)

'''
'''
Input1 = int(input("Enter first Numbers: "))
Input2 = int(input("Enter second Number: "))
sum = 0

for x in range(Input1,Input2):
    sum = sum + x
print("The ",sum," of the Inputed numbers of",Input1,"and",Input2)

'''
'''
userInput = int(input("Enter a number:"))
factorial = 1

for x in range(1, userInput+1):
    factorial = factorial * x
print("The factorial of ", x, "is", factorial)
'''
'''
userInput = int(input("Enter a number: "))
print("The factors of your number are: ")
for x in range(1, userInput + 1):
        if userInput % x == 0:
         print(x)
'''


