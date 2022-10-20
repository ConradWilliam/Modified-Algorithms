def bubble(list_a):
    indexing_length = len(list_a) - 1 #Scan does not apply to comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i] > list_a[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a # Return our list "unsorted_list" which is not sorted.
list_a = [1,6,8,7,9,3,4]
print(bubble(list_a))

def binary_search(arr, search_value):
    begin = 0
    end = len(arr)-1

    while begin <= end:
        midd = int((begin + end)//2)

        if search_value == arr[midd]:
            return True

        elif search_value < arr[midd]:
            end = midd-1
        
        else:
            begin = midd + 1

    return False


print(binary_search(list_a,3))