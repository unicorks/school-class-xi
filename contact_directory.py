contacts = {}
def add_new(name, number):
    contacts[name]=number

def fetch_by_name(name):
    return contacts.get(name, 'not found')

def fetch_by_no(number):
    for k,v in contacts.items():
        if v==number:
            return k,v
    return 'not found'

def delete_no(name):
    return name, contacts.pop(name)

def update(name, number):
    contacts[name]=number
    return contacts


add_new('sona', 1234)
add_new('ak', 12345)
add_new('da', 10000)
print(contacts)
print(fetch_by_name('ak'))
print(fetch_by_no(10000))
print(delete_no('da'))
print(update('sona', 1324))
