'''
Created on May 7, 2018

@author: Kosta
'''
def startTheProg():
    arrayMin = list()
    arrayMax = list()
    numbers = raw_input("Please enter how many numbers do you want\n")
    print "Please enter the numbers"
    for i in range(int(numbers)):
        num = raw_input("num "+str(i+1)+" :")
        arrayMin.append(int(num))
        arrayMax.append(int(num))
    print 'The array is: ',arrayMin
    print 'The array is: ',arrayMax
    return arrayMin, arrayMax

def buildMaxHeap(arr):
    array_len = len(arr)
    for i in range(array_len,-1,-1):
        heapify(arr,array_len,i)
    print "Max heap is: ",
    for i in range(array_len):
        print("%d " %arr[i]),
    print '\n'
    buildMinHeap(arr,array_len)

def buildMinHeap(arrMin,n):
    for i in range(n-1,0,-1):
        arrMin[i],arrMin[0] = arrMin[0],arrMin[i]
        heapify(arrMin,i,0)
    print "Min heap is: ",
    for i in range(n):
        print("%d " %arrMin[i]),

def insert(number,arrMax,arrMin):
    arrMax.append(int(number))
    arrMin.append(int(number))
    lenOfArrayMax = len(arrMax)
    lenOfArrayMin = len(arrMin)
    if arrMax[lenOfArrayMax-1]>arrMax[((lenOfArrayMax-1)/2)]:
        a = insertMax(arrMax,lenOfArrayMax-1)
        return a
    if arrMin[lenOfArrayMin-1]<arrMin[((lenOfArrayMax-1)/2)]:
        insertMin(arrMin,lenOfArrayMin-1)
        return a
        
def insertMax(arr,index):
    lenOfArray= len(arr)
    if index == 0:
        return
    else: 
        arr[index]>arr[((index-1)/2)]# and index != 0:
        arr[((index-1)/2)],arr[index]=arr[index],arr[((index-1)/2)]
        insertMax(arr,((index-1)/2))
    print "New MaxHeap is: \n"
    for i in range(lenOfArray):
        print("%d " %arr[i]),

def insertMin(arr,index):
    lenOfArray= len(arr)
    if arr[index]<arr[((index-1)/2)] and index != 0:
        arr[((index-1)/2)],arr[index]=arr[index],arr[((index-1)/2)]
        insertMin(arr,((index-1)/2))
    print "New MinHeap is: \n"
    for i in range(lenOfArray):
        print("%d " %arr[i]), 
    
def find_max(arr):
    print arr[0]
    return arr[0]
    
def heapify(arr,n,i):
    largest = i
    l = 2*i
    r = 2*i+1
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)    

if __name__ == "__main__":
    arrayMin, arrayMax = startTheProg()
    while 1: 
        user_option = raw_input("\nTo build a heap press 1\nTo insert a num press 2\nTo find Max press 3\n"+
        "To find Min press 4\nTo delet Max press 5\nTo delet Min press 6\n")
        if user_option == str(1):
            buildMaxHeap(arrayMax)
        if user_option == str(2):
            user_option = raw_input("please insert a number\n\n")
            array = insert(user_option,arrayMin, arrayMax)
            print "New MaxHeap is: \n"
            for i in range(len(array)):
                print("%d " %array[i]),
        if user_option == str(3):
            find_max(arrayMax)
        