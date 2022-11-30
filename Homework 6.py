#task 1
def checkListForFindNumerical (someList):
    string =''
    result=''
    for i in range(len(someList)):
        string = someList[i]
        if(string[0] in'+-'):
          if(len(string)==2):
            string+='0'
            l=list(string)
            l[1],l[2] = l[2],l[1]
            result+='"'
            result+=''.join(l)
            result+='" '
            continue
          else:
            result+='""'
            result+=string
            continue
        if(string[0].isdigit()):
            if(len(string)==1):
                string+='0'
                l=list(string)
                l[0],l[1] = l[1],l[0]
                result+='"'
                result+=''.join(l)
                result+='" '
                continue
            else:
                result+='"'
                result+=string
                result+='" '
                continue
        result+=string
        result+=' '
    print(result) 

string=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
checkListForFindNumerical(string)

task 2

someList = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result=''
for i in range(len(someList)):
    result+='Привет, '
    result+=someList[i].split()[len(someList[i].split())-1].lower().capitalize()
    result+='!'
    print(result)
    result=''


