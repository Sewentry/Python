# #tasl 1

# def oddMulti (someList):
#     sum = 0
#     for i in range (1,len(someList),2):
#         sum+=someList[i]
#     return sum

# someList = [1,2,3,4]
# print(oddMulti(someList))

# #task 2

# def findPairMulti(some_list):
#     multi_list = []
#     if some_list % 2 == 0:
#         for i in range(int(len(some_list)/2)):
#             multi_list.append(some_list[i]*some_list[-i-1])
#         return multi_list
#     else:
#         for i in range(int(len(some_list)/2)+1):
#             multi_list.append(some_list[i]*some_list[-i-1])
#         return multi_list

# some_list = [1,2,3,4,5]
# print(findPairMulti(some_list))

#task 3
# def findDifferenceBetweenMinMax (some_list):
#     fractionalList= list(map(float,findFractionalPart(some_list)))
#     return max(fractionalList)-min(fractionalList)
# def findFractionalPart (some_list):
#     frationalList = []
#     for i in range (len(some_list)):
#         frationalList.append(str(some_list[i]).replace(str(some_list[i]).split(".")[0],'0',1))
#     return frationalList

# someList = [1.01,1.2,1.3]
# print(findDifferenceBetweenMinMax(someList))

#task 4

# number = int(input())
# result = ''
# while number>0:
#     result+=str(number%2)
#     number//=2
# print(int(result[::-1]))

#task 5

def fibbonachi (count):
    if count in (1,2):
        return 1
    else:
        return fibbonachi(count-1)+fibbonachi(count-2)


def negaFibbonachi (count):
    if count == 0:
        return 0
    if count == -1:
        return 1
    else:
        return negaFibbonachi(count+2)-negaFibbonachi(count+1)

number = int(input())
result = []
for i in range(-number,number):
    if i<=0:
        result.append(negaFibbonachi(i))
    else:
        result.append(fibbonachi(i))
print(result)