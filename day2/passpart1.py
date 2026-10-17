import re

def last_item(lst):
    if not lst:
        return None 
    return lst[-1]

with open('day2/input.txt', 'r') as file:
    result=0
    numberone=[]
    minus =[]
    numbertwo =[]
    targetletter =[]
    validatedstring = []
    for line in file:
        minus.append(line.index('-'))
        numberone.append(line[0:line.index('-')])
        numbertwo.append(line[line.index('-')+1:line.index(' ')])
        if len(numberone) != len(numbertwo):
            print('something is wrong,',len(numberone),'is not',len(numbertwo))
            exit()
        if int(last_item(numbertwo)) < int(last_item(numberone)):
            print('something is wrong with on line', len(numberone)+1,',',last_item(numberone), 'is not smaller than' ,last_item(numbertwo) )
            exit()
        targetletter.append(line[line.index(' ')+1:line.index(' ')+2])
        if not re.fullmatch(r'[a-z]+', last_item(targetletter)):
            print("target letter is weird ",last_item(targetletter),' on line' , len(numberone)+1)
            exit()
        validatedstring.append(line[line.index(':')+2:-1])
    for i in range(len(numberone)):
        print (int(numberone[i]), validatedstring[i].count(targetletter[i]),int(numbertwo[i]) )
        if  (int(numberone[i]) <= int(validatedstring[i].count(targetletter[i])) and int(validatedstring[i].count(targetletter[i])) <= int(numbertwo[i])): 
            result+= 1
            print("valid")
    print(result)
