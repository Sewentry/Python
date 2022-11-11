#task 1
# stroka = str(input())
# strReplacement = str(input()) 
# while stroka.find(strReplacement)>=0:
#     stroka=stroka.replace(strReplacement,'')
# print(stroka)

#task 2
# import random

# skittles = int(input('Введите число конфет: '))
# while skittles>0:
#     humanTurn = int(input('введите число конфет, которые хотите забрать. Максимум 28:'))
#     skittles-=humanTurn
#     if(skittles>0):
#         machineTurn = random.randint(1,28)
#         skittles-=machineTurn
#         if(skittles<0):
#             print('Пластмассовый мир победил')
#             break
#     else:
#         print('Человек победил')
#         break

#task 3

#Реализовывал игру на java, когда обучался тут ранее. Пробовал реализовать там ИИ, но так и не справился с определенными багами. Игра позволяет выбрать любое поле NxN. Ссылка: https://github.com/Sewentry/Java/blob/Homework4/src/main/java/Homework4/CrossesZerosApp.java 
# Стратегия бота описана в самом коде.


#task 4

from ctypes import resize


def countSymbol (string,index):
    count = 1
    j = index+1
    while j<len(string):
        if(string[index]==string[j]):
            count+=1
            j+=1
        else:
            break
    return count
print(countSymbol('vvv',0))
def replaceString (index,count,string):
    string = str(count)+string[index]
    return string
string = input()
result =''
i=0
while string!='':
    index=countSymbol(string,i)
    result+=replaceString(i,index,string)
    string=string[index:]
print(result)

