def sortit(L):
    counter=0
    while counter < len(L):
        comparing=1
        original=0
        for minn in L[:-1]:
            number=L[original]
            compared=L[comparing]
            if minn>compared:
                L[original] = compared
                L[comparing]= number
            comparing+=1
            original+=1
        counter+=1
    return (L)
#
# sortit([5,4,6,4])
# sortit([47,1,100,10,2,3,4,5,6,1,2,4,6,3454,89,45,22,34,54,67,12,4,1,3,6])


def contains(L, num):
    sayit= 0
    for i in L:
        if i == num:
            sayit= True
    if sayit:
        print (True)
    else:
        print (False)

# contains([5,4,6,4],3) #False
# contains([47,1,100,10,2,3,4,5,6,1,2,4,6,3454,89,45,22,34,54,67,12,4,1,3,6],9) #False
# contains([3,4,5], 3) #True

def findNum(L,num):
    new = sortit(L)
    start= 0
    end = len(L)-1
    while abs(end - start) > 1:
        mid= int((start+end)/2)
        if new[mid] > num:
            end= mid
        elif new[mid] < num:
            start= mid
        elif new[mid]== num:
            return True
    mid= int((start+end)/2)
    if new[mid]==num:
        return True
    else:
        return False
#
# print ("--------------------------")
# print (findNum([101,1,5,57,102,84,96,100,102], 96)) #True
# print (findNum([5,4,6,4], 3)) #False
# print (findNum([47,1,100,10,2,3,4,5,6,1,2,4,6,3454,89,45,22,34,54,67,12,4,1,3,6], 9)) #False
# print (findNum([3,4,5], 3)) #True

def insertsort(L):
    index=0
    counter=0
    while index<len(L):
        while counter== index:
            if L[index]> L[index+1]:
                place= L[index]
                L[index]=L[index+1]
                L[index+1]= place
            counter+=1
        index+=1
    print (L)

insertsort([6,5])
