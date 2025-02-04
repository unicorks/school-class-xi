# binary search
def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    while first <= last and not found:
        mid = (first+last)//2
        if lst[mid] == item:
            found = True
        elif lst[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    if not found:
        print("Not found.")
    else:
        print(f"Found at {mid+1}th position.")
    return found
binary_search([1,2,3,5,8], 6)
binary_search([1,2,3,5,8], 8)
