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

def buildMaxHeap(arrMax):
    array_len = len(arrMax)
    for i in range(array_len,-1,-1):
        print i
        heapifyMax(arrMax,array_len,i)
    print "Max heap is: ",
    for i in range(array_len):
        print("%d " %arrMax[i]),
    print '\n'
    return arrMax

def buildMinHeap(arrMin):
    array_len = len(arrMin)
    for i in range(array_len,-1,-1):
        heapifyMin(arrMin,array_len,i)
    print "Max heap is: ",
    for i in range(array_len):
        print("%d " %arrMin[i]),
    print '\n'
    return arrMin

def insert(number,arrMax,arrMin):
    arrMax.append(int(number))
    arrMin.append(int(number))
    lenOfArrayMax = len(arrMax)
    lenOfArrayMin = len(arrMin)
    if arrMax[lenOfArrayMax-1]>arrMax[((lenOfArrayMax-1)/2)]:
        arrMax = insertMax(arrMax,lenOfArrayMax-1)
        return arrMax
    if arrMin[lenOfArrayMin-1]<arrMin[((lenOfArrayMax-1)/2)]:
        arrMin = insertMin(arrMin,lenOfArrayMin-1)
        return arrMin
        
def insertMax(arr,index):
    if index == 0:
        return
    else: 
        if arr[index]>arr[((index-1)/2)]:
            arr[((index-1)/2)],arr[index]=arr[index],arr[((index-1)/2)]
            insertMax(arr,((index-1)/2))
    return arr

def insertMin(arr,index):
    if index == 0:
        return
    else:
        if arr[index]<arr[((index-1)/2)]:
            arr[((index-1)/2)],arr[index]=arr[index],arr[((index-1)/2)]
            insertMin(arr,((index-1)/2))
    return arr

def find_max(arr):
    return arr[0]
def find_min(arr):
    return arr[0]
    
def heapifyMax(arr,n,i):
    largest = i
    l = 2*i
    r = 2*i+1
    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapifyMax(arr,n,largest)    
        
def heapifyMin(arr,n,i):
    smallest = i
    l = 2*i
    r = 2*i+1
    if l<n and arr[i]>arr[l]:
        smallest=l
    if r<n and arr[smallest]>arr[r]:
        smallest=r
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapifyMin(arr,n,smallest)  

if __name__ == "__main__":
    arrayMin, arrayMax = startTheProg()
    while 1: 
        user_option = raw_input("\nTo build a heap press 1\nTo insert a num press 2\nTo find Max press 3\n"+
        "To find Min press 4\nTo delet Max press 5\nTo delet Min press 6\n")
        if user_option == str(1):
            arrayMax = buildMaxHeap(arrayMax)
            arrayMin = buildMinHeap(arrayMin)
        if user_option == str(2):
            user_option = raw_input("please insert a number\n\n")
            arrayAfterInsert = insert(user_option,arrayMin, arrayMax)
            print "New array after insert action is: "
            for i in range(len(arrayAfterInsert)):
                print("%d " %arrayAfterInsert[i]),
            arrayMax = arrayAfterInsert
        if user_option == str(3):
            print find_max(arrayMax)
        if user_option == str(4):
            print find_min(arrayMin)
            
        