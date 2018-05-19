'''
Created on May 7, 2018

@author: Kosta Djamilov
'''
import sys
global arrayMin
global arrayMax
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
    #print "Max heap is: ",
    #printArray(arrMax)
    return arrMax

#Min heap function. Receives the array minimum and return the minimum sorted heap. 
#Time complexity is o(n)
def buildMinHeap(arrMin):
    array_len = len(arrMin)
    for i in range(array_len,-1,-1):
        heapifyMin(arrMin,array_len,i)
    #print "Min heap is: ",
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
#Heapify-maximum algorithm. Receives array, size and index and performs max heapify  
#Time complexity is o(lgn)     
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
#Heapify-minimum algorithm. Receives array, size and index and performs min heapify  
#Time complexity is o(lgn)  
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
#Deletes the maximum number from the array. Receives relevant array and returns the array + the deleted number
#Time complexity is o(lgn)
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
#Deletes the minimum number from the array. Receives relevant array and returns the array + the deleted number
#Time complexity is o(lgn)
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
#Print the given array values    
def printArray(arr):
    for i in range(len(arr)):
        print("%d " %arr[i]),
#Finds the minimum values index in max array in order to delete it after performing deletMin.
#Time complexity is o(lgn) 
def MinInMax(arr):
    indexMin=0
    n = len(arr)
    index = n/2
    if index == 0:
        return arr[index]
    minimum = arr[index+1] 
    count = index+2 
    for count in range(n):
        if arr[count]<minimum:
            minimum = arr[count]
            indexMin = count  
    print 'The minimum is: ' + str(minimum)
    print 'The index of ' + str(minimum) + ' is at: ' +str(indexMin)
    return indexMin 
#Finds the maximum values index in min array in order to delete it after performing deletMax.
#Time complexity is o(lgn) 
def MaxInMin(arr):
    indexMax=0
    n = len(arr)
    index = n/2
    if index == 0:
        return arr[index]
    maximum = arr[index+1] 
    count = index+2 
    for count in range(n):
        if arr[count]>maximum:
            maximum = arr[count]
            indexMax = count  
    print 'The maximum is: ' + str(maximum)
    print 'The index of ' + str(maximum) + ' is at: ' +str(indexMax)
    return indexMax   
#Deletes the relevant index(maximum value)from min array and re builds the min heap
#Time complexity is o(1) - deletes the index
#Time complexity is o(n) - build the heap
def reOrgMinHeap(arr,index):
    del arr[index]
    buildMinHeap(arr)
    return arr
#Deletes the relevant index(minimum value)from max array and re builds the max heap
#Time complexity is o(1) - deletes the index
#Time complexity is o(n) - build the heap
def reOrgMaxHeap(arr,index):
    del arr[index]
    buildMaxHeap(arr)
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
            print 'Max heap is: '+ str(arrayMax)
            print 'Min heap is: '+ str(arrayMin)
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
            print 'Max heap after delet Max' + str(arrayMax)
            index = MaxInMin(arrayMin)
            arrayMin = reOrgMinHeap(arrayMin, index)
            print 'Min heap after delet Max' + str(arrayMin)
        if user_option == str(6):
            arrayMin, deletedMinNum = deletMin(arrayMin)
            print 'The deleted minimum is: '+ str(deletedMinNum)
            index = MinInMax(arrayMax)
            arrayMax = reOrgMaxHeap(arrayMax, index)
            print 'Max heap after delet Min' + str(arrayMax)
            print 'Min heap after delet Min' + str(arrayMin)

        if user_option == str(999):
            print '999 was pressed, ending the program!'
            sys.exit()
        