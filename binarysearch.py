def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
myList = [1,3,4,6,7,8,10,12,23]
item=int(input("item: "))
print("siz qidirgan elementning indexi: ",binary_search(myList, item))