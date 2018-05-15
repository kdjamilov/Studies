'''
Created on May 7, 2018

@author: Kosta Djamilov
'''
import sys

def startTheProg():
    arrayMin = list()
    arrayMax = list()
    print 'Welcome to Maman 14'
    numbers = raw_input("Please enter the amount of numbers for the data base\n")
    for i in range(int(numbers)):
        num = raw_input("num "+str(i+1)+" :")
        arrayMin.append(int(num))
        arrayMax.append(int(num))
    #print 'The Max array is: ',arrayMin
    #print 'The Min array is: ',arrayMax
    return arrayMin, arrayMax

#Max heap function. Receives the array minimum and return the maximum sorted heap.
#Time complexity is o(n)
def buildMaxHeap(arrMax):
    array_len = len(arrMax)
    for i in range(array_len,-1,-1):
        heapifyMax(arrMax,array_len,i)
    print "Max heap is: ",
    printArray(arrMax)
    print '\n'
    return arrMax

#Min heap function. Receives the array minimum and return the minimum sorted heap. 
#Time complexity is o(n)
def buildMinHeap(arrMin):
    array_len = len(arrMin)
    for i in range(array_len,-1,-1):
        heapifyMin(arrMin,array_len,i)
    print "Min heap is: ",
    printArray(arrMin)
    return arrMin

#Insert function. Gets the number to insert and the 2 arrays
#This function will split the insert action for min heap and for max heap
def insert(number,arrMax,arrMin):
    arrMax.append(int(number))
    arrMin.append(int(number))
    lenOfArrayMax = len(arrMax)
    lenOfArrayMin = len(arrMin)
    if arrMax[lenOfArrayMax-1]>arrMax[((lenOfArrayMax-1)/2)]:
        arrMax = insertMax(arrMax,lenOfArrayMax-1)
    if arrMin[lenOfArrayMin-1]<arrMin[((lenOfArrayMax-1)/2)]:
        arrMin = insertMin(arrMin,lenOfArrayMin-1)
    return arrMax, arrMin

#Insert Max function. Gets the relevant array and the index to start. The function returns the new array.
#Time complexity is o(lgn)        
def insertMax(arr,index):
    if index == 0:
        return
    else: 
        if arr[index]>arr[((index-1)/2)]:
            arr[((index-1)/2)],arr[index]=arr[index],arr[((index-1)/2)]
            insertMax(arr,((index-1)/2))
    return arr

#Insert Min function. Gets the relevant array and the index to start. The function returns the new array.
#Time complexity is o(lgn)  
def insertMin(arr,index):
    if index == 0:
        return
    else:
        if arr[index]<arr[((index-1)/2)]:
            arr[((index-1)/2)],arr[index]=arr[index],arr[((index-1)/2)]
            insertMin(arr,((index-1)/2))
    return arr

#Finds max number. Receives relevant array and return first index.
#Time complexity is o(1)   
def find_max(arr):
    return arr[0]

#Finds min number. Receives relevant array and return first index.
#Time complexity is o(1)  
def find_min(arr):
    return arr[0]
    
def heapifyMax(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapifyMax(arr,n,largest)    
        
def heapifyMin(arr,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[i]>arr[l]:
        smallest=l
    if r<n and arr[smallest]>arr[r]:
        smallest=r
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapifyMin(arr,n,smallest)  

def deletMax(arr):
    if len(arr)<1:
        print "\nHeap has not elements, exiting the program!"
        sys.exit()
    else:
        max_num = arr[0]
        arr[0] = arr[len(arr)-1]
        del arr[len(arr)-1]
        heapifyMax(arr,len(arr)-1,0)
        return arr,max_num

def deletMin(arr):
    if len(arr)<1:
        print "\nHeap has not elements, exiting the program!"
        sys.exit()
    else:
        min_num = arr[0]
        arr[0] = arr[len(arr)-1]
        del arr[len(arr)-1]
        heapifyMin(arr,len(arr)-1,0)
        return arr,min_num
    
def printArray(arr):
    for i in range(len(arr)):
        print("%d " %arr[i]),
    

def reOrgTheArray(arr):
    del arr[len(arr)-1]
    return arr

if __name__ == "__main__":
    arrayMin, arrayMax = startTheProg()
    while 1:
        print '\n'
        print "-----Menu-----" 
        print "Press 1 to build a Heap"
        print "Press 2 to insert a number"
        print "Press 3 to find Max"
        print "Press 4 to find Min"
        print "Press 5 to delet Max"
        print "Press 6 to delete Min"
        print "Press 999 to end the program"
        user_option = raw_input()
        if user_option == str(1):
            arrayMax = buildMaxHeap(arrayMax)
            arrayMin = buildMinHeap(arrayMin)
        if user_option == str(2):
            user_option = raw_input("please insert a number\n\n")
            arrayMaxAfterInsert,arrayMinAfterInsert = insert(user_option,arrayMax, arrayMin)
            print "New Max array after insert action is: "
            printArray(arrayMaxAfterInsert)
            arrayMax = arrayMaxAfterInsert
            print '\n'
            print "New Min array after insert action is: "
            printArray(arrayMinAfterInsert)
            arrayMin = arrayMinAfterInsert
            
        if user_option == str(3):
            max_num = find_max(arrayMax)
            print 'Maximum number is: ' + str(max_num)
        if user_option == str(4):
            min_num = find_min(arrayMin)
            print 'Minimum number is: ' + str(min_num)
        if user_option == str(5):
            arrayMax, deletedMaxNum = deletMax(arrayMax)
            print 'The deleted maximum is: '+ str(deletedMaxNum)
            arrayMin = reOrgTheArray(arrayMin)
            print 'Max heap after delet Max' + str(arrayMax)
            print 'Min heap after delet Max' + str(arrayMin)
        if user_option == str(6):
            arrayMin, deletedMinNum = deletMin(arrayMin)
            print 'The deleted minimum is: '+ str(deletedMinNum)
            arrayMax = reOrgTheArray(arrayMax)
            print 'Max heap after delet Max' + str(arrayMax)
            print 'Min heap after delet Max' + str(arrayMin)
        if user_option == str(999):
            print '999 was pressed, ending the program!'
            sys.exit()
        