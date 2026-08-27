patient_ids =[101, 112, 130,145,190,205]
medical_record_numbers =[145, 101, 190,157,130, 205, 112]
def binary_search(array):
    key = int(input("What are you looking for: "))
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low +high)//2
        if key== array[mid]:
            print("The ID is here: ", mid)
            return mid
        elif key< array[mid]:
            high = mid - 1 
        else:
            low = mid + 1
    return -1
        
binary_search(array=patient_ids)
##linear serach
def linear_search(array):
    target = int(input("What are you looking for: "))
    for i in range(len(array)):
        if array[i] == target:
            print("This is the item:", array[i])
            print("Found at index", i)
            return i
    print("not here")

    return -1
linear_search(array = medical_record_numbers)
##quick sort
def quic_sort(array):
    if len(array)<=1:
        return array
    middle = array[len(array)//2]
    pivot = middle
    less_than_piv = [x for x in array if x<pivot]
    middle_part = [x for x in array if x == pivot]
    greater_than = [ x for x in array if x> pivot]

    return quic_sort(less_than_piv) + quic_sort(middle_part) + quic_sort(greater_than)

sorted_array = quic_sort(array = medical_record_numbers)
print(sorted_array)