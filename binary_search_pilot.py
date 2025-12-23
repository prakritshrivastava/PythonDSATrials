
def index_search(list,item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = int((high+low)/2)
        guess=list[mid]
        if guess == item:
            return mid
        elif guess<item:
            low = mid + 1
        elif guess>item:
            high = mid -1
    return None

my_list=[1,2,3,4,5]
print(index_search(my_list,5))

