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

# Function 5
def ScoreFinder(list1, list2, string):
    index = -1
    string = string.lower()
    player = ''
    for x in range(len(list1)):
        player = player + list1[x] + ' '
    player_list = player.lower().split()
    for i in range(len(player_list)):
        if string == player_list[i]:
            index = i
    if index >= 0:
        output = list1[index] + ' got a score of ' + str(list2[index])
        PrintOutput(output)
    else:
        PrintOutput('player not found')
    
    
    
    
        
    

    
    
    
    
    
    
    
    
    
    
    

