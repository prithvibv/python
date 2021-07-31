# underscore in python https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc
# unpacking k,v = item

hash_table = [[] for _ in range(10)]
print(hash_table)

def hash(value):
    return value % len(hash_table)

print(hash(10))

def insert(map,key,value):
    index = hash(key)
    bucket = map[index]
    isKey = False
    for item in bucket:
        k,v = item
        if(k == key):
            isKey = True
            break

    if(isKey == True):
        print("Cannot insert key already available")

    if(isKey == False):
        bucket.append((key,value))

def search(map,key):
    index = hash(key)
    for item in map[index]:
        k,v = item
        if(k == key):
            print("key found"+ str(item))
            return item


insert(hash_table,20,"hello1")
insert(hash_table,10,"hello")
insert(hash_table,10,"hello10")

insert(hash_table,21,"hello3")
search(hash_table,10)
print(hash_table)
