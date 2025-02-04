friends = ['akshra', 'inshirah', 'siya', 'sonakshi', 'suhani']
friend = 'sonakshi'
for i in range(len(friends)):
    if friends[i]==friend:
        print(friend, 'found at', i+1)

first = 0
last = len(friends)-1
found = False
while first<=last and not found:
    mid = (first+last)//2
    if friends[mid]==friend:
        found = True
    elif friends[mid]>friend:
        last = mid-1
    elif friends[mid]<friend:
        first = mid+1
if found:
    print(friend, 'found at', mid+1)
else:
    print('not found')
