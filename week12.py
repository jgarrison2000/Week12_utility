# James Garrison
# CSCI 102 - Section C
# Week 12 - utility



# Function 1
def PrintOutput(a):
    print('OUTPUT', a)


# Function 2
def LoadFile(filename):
    lines = open('file.txt','r')
    read = lines.readlines()
    lines.close()
    print('OUTPUT', lines)


# Function 3
def UpdateString(x,y,num):
    list1 = list(x)
    list1[num] = y
    ret = ''.join(list1)
    print('OUTPUT', ret)


# Function 4
def FindWordCount(list1, string):
    count = 0
    for x in list1:
        if x == string:
            count +=1
    print('OUTPUT', count)
        
    

    
    
    
    
    
    
    
    
    
    
    

