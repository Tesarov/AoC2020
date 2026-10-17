with open('day1/input.txt', 'r') as file:
    spam =[]
    for line in file:
        value = int(line)
        spam.append(value)
    for a in spam:
        for b in spam:
            for c in spam:
                if a + b + c == 2020:
                    print(a*b*c,'with the three numbers being', a,'and',b,'and',c)
                    exit()
        

