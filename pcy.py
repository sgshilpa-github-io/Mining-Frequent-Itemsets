__author__ = 'shilpagulati'


import sys
import itertools

def createCombo(totalItems,size):
    PossibleCombolist=itertools.combinations(totalItems,size)
    totalPair=[]
    for each in PossibleCombolist:
        totalPair.append(list(each))
    totalPair.sort()
    return totalPair



def count(Item,TotalItems):
    countV=0
    for each in TotalItems:
        if Item in each:
            countV=countV+1
    return countV


def CountfromALL(item,ItemList):
       totalC=0
       for eachE in ItemList:
           if all(x in eachE for x in item):
               totalC=totalC+1
       return totalC


def HashValue(item):
    sumV=0
    for i in range(0,len(item)):
        sumV +=uniqueItem.index((item[i]))
    return sumV


# return BucketValues and Bit vector
def HashBaskets(ALLitemList,bucket_size,combo_size):
    Buckets=[0]*bucket_size
    for each in ALLitemList:

        eachPair=createCombo(each,combo_size)

        for each in eachPair:

            Buckets[HashValue(each)%bucket_size] =  Buckets[HashValue(each)%bucket_size]+1
    return Buckets

def BitBucket(BucketList):
    BucketBit = [False]*len(BucketList)
    for i in range(0,len(BucketList)):
        if BucketList[i] >= support:
            BucketBit[i] = True
    return BucketBit


def PCYalgo(totalItems,uniqueItem,support,bucket_size):
    FrequentList=[]
    for each in uniqueItem:
        if count(each,totalItems) >= support:
            FrequentList.append(each)
    print FrequentList
    print "\n"

    while(len(FrequentList)!=0):

        TempFrequent=[]
        FinalFrequent=[]
        Buckets = HashBaskets(totalItems,bucket_size,len(FrequentList[0])+1)
        BitBuckets=BitBucket(Buckets)
        # print Buckets
        BucketDict={}
        for ind,value in enumerate(Buckets):
            BucketDict[ind]=value


        # print totalItems

        for each in totalItems:

            temp=createCombo(each,len(FrequentList[0])+1)

            for eachT in temp:

                flag = 1

                TempComb=createCombo(eachT,len(eachT)-1)

                for eachC in TempComb:


                    if len(eachC) == 0:
                        # flag=0
                        continue
                    if len(eachC)==1:
                        if eachC[0] in FrequentList:
                            continue
                        else:
                            flag=0
                            break
                    else:

                        if eachC in FrequentList:
                     
                            continue
                        else:
                            flag=0
                            break
                if flag==1:
                   
            
                    if eachT not in TempFrequent:
                        TempFrequent.append(eachT)







        TempFrequent.sort()

        for each in TempFrequent:

            if BitBuckets[HashValue(each)%bucket_size] == True and  CountfromALL(each,totalItems)>=support:
                    FinalFrequent.append(each)
        if len(FinalFrequent)>1:
            print BucketDict
            print FinalFrequent
            print "\n"
        FrequentList=FinalFrequent










input=open(sys.argv[1])
support=int(sys.argv[2])
bucket_size=int(sys.argv[3])

# read the input and make list of lists containing baskets
AllItems=[]
for line in input:
    line = line.strip().replace(',', "")
    smallList=[]
    for i in range(0,len(line)):
        smallList.append(line[i])
        smallList.sort()
    AllItems.append(smallList)

# create list if unique Items

uniqueItem = []

for sublist in AllItems:

    for each in sublist:

           if each not in uniqueItem:
                uniqueItem.append(each)
uniqueItem.sort()



PCYalgo(AllItems,uniqueItem,support,bucket_size)
# HashBaskets(uniqueItem,20)
