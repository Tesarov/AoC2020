with open('day3/input.txt', 'r') as file:
    result=0
    trees=[]
    length=0
    angle=3
    i=0
    j=0
    for line in file:
        trees.append(line)
        length = len(line)-1
        #print(line)
        if str(line[(j % length)]) =='#':
            result+=1
            print(i,j)
        print(j % length)
        if str(line[(j % length)]) =='#':
            row = list(trees[i])          # turn the string into a list of characters
            row[j % length] = 'X'
        else:
            row = list(trees[i]) 
            row[j % length] = 'O'          # now item assignment works
        trees[i] = ''.join(row)        # convert back to a string and store it
        #print(trees[i-1])
        #print(trees[i])
        i+=1
        j+= angle
        print(length)
    print (i,j,length)
    print('the result is:',result)
