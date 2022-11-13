#task 1

from re import S


number = input()
sum = 0
for i in range(len(number)):
    sum+=int(number[i])
print(sum)



#task 2

multiplicationOfNumbersKit = int(input())
multiplication = 1
listOfNumbers = []
for i in range(1,multiplicationOfNumbersKit+1):
    multiplication=multiplication*i
    listOfNumbers.append(multiplication)
print(*listOfNumbers,sep=', ')

#task 3

countOfNumbers = int(input())
sum=0
for i in range (1,countOfNumbers+1):
    sum+=pow(1+1/i,i)
print('%.2f' %sum)


#task 4

from random import random


countOfNumbers = int(input())
file1 = open('positions.txt', 'r', encoding='utf-8')
executionPosition = file1.read()
file1.close()
listOfNumbers = []
multiplication = 1
position = 0
for i in range (-countOfNumbers,countOfNumbers+1):
    listOfNumbers.append(i)
    if executionPosition.find(str(position))>0:
        multiplication=multiplication*listOfNumbers[position]
    position=position+1
print(multiplication)

#task 5
import random

listOfNumbers = [1, 2, 3, 4, 5]
random.shuffle(listOfNumbers)
