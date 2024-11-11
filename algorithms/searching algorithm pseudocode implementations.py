def linearSearch(array, arrayLength, requestedItem):
    pointer = 0
    while True:
        if array[pointer] == requestedItem:
            return array[pointer], pointer
        elif pointer == arrayLength -1:
            return -1
        else:
            pointer +=1
        #endif
    #endwhile
#endfunction

def binarySearch(array, arraylength, requestedItem):
    startPointer = 0
    endPointer = arraylength - 1
    middlePointer = (endPointer - startPointer)//2
    current = array[middlePointer]
    while True:
        if current == requestedItem:
            return array[middlePointer], middlePointer
        elif requestedItem > current:
            startPointer = middlePointer
            middlePointer += ((endPointer - startPointer)//2)
        elif requestedItem < current:
            endPointer = middlePointer
            middlePointer -= ((endPointer - startPointer)//2)
        else:
            return -1
        #endif
    #endwhile
#endfunction
