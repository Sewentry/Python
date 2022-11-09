# #task 1

# number = float(input())
# error = float(input())
# multi = 1
# while (error<1):
#     error*=10
#     multi+=1
# print(round(number,multi-1))

#task 2

# def Eratosfen(number):
#     result=[]
#     for i in range(number+1):
#         result.append(i)
#     result[1]=0
#     for i in range(len(result)):
#         if result[i]!=0:
#             j=i+1
#             while j<number:
#                 result[j]=0
#                 j+=1
#     result=set(result)
#     return result

# number = int(input())
# print(Eratosfen(number))

#task 3

# number = int(input)
# result = []
# for _ in range (number):
#     result.append(int(input()))
# print(set(result))

#task 4

def koeff (number):
    s='1+'
    if number==1:
        s+='x+'
        return s
    if number==2:
        s+='x^'
        s+=str(number)
        s+='+'
        return s
    else:
        return koeff(number-1)+'x^'+str(number)+'+'
number = int(input())
with open("result.txt",'w') as file:
    file.write(koeff(number))
