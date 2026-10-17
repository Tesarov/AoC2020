with open('day1/input.txt', 'r') as file:
    spam =[]
    for line in file:
        value = int(line)
        spam.append(value)
    for a in spam:
        for b in spam:
            if a + b == 2020:
              print(a*b,'with the two numbers being', a,'and',b)
              exit()
        

