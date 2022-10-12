#task 1

dayWeek = int(input())
if (dayWeek%3 == 0 and dayWeek%2 == 0) or dayWeek%7==0:
    print('да')
else:
    print('нет')

#task 2

for i in range (2):
    for j in range (2):
        for k in range (2):
            if not(i or j or k) == (not(i) and not(j) and not(k)):
                print ('выражение тождественно')
            else:
                print ('выражение не тождественно')

#task 3

pointX = int(input())
pointY = int(input())

if(pointX>0 and pointY>0):
    print('1-ая четверть')
elif(pointX<0 and pointY<0):
    print('2-ая четверть')
elif(pointX<0 and pointY<0):
    print('3-я четверть')
elif(pointX>0 and pointY<0):
    print('4-ая четверть')

#task 4

numberOfQuarter = int(input())

if(numberOfQuarter == 1):
    print('X>0, Y>0')
if(numberOfQuarter == 2):
    print('X<0, Y>0')
if(numberOfQuarter == 3):
    print('X<0, Y<0')
if(numberOfQuarter == 4):
    print('X>0, Y<0')

#task 5
import math

coordinateA = input()
coordinateB = input()
length = math.sqrt(pow(int(coordinateB[0])-int(coordinateA[0]),2)+pow(int(coordinateB[2])-int(coordinateA[2]),2))
print("%.2f" % length)