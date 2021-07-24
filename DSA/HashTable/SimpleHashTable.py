# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/ 
#the elements inside the list is a tuple('25','usa')
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
country_code = [('25', 'USA'), ('20', 'India'), ('10', 'Nepal')]
print(type(country_code))

def insert(map,key,value):
    map.append((key,value))

def search(map,key):
    print("yo i am searching")
    for item in map:
        print(item[0])
        if item[0] == key:
            return item[1]

def delete(map,key):
    print("Deleting key:" + str(key))
    for i in range(len(map)):
        item = map[i]
        if item[0] == key:
            del map[i]
    else:
        print(str(key) + " key not found")

print("Search result")
print(search(country_code,"25"))

insert(country_code,1,'Australia')
print(country_code)

delete(country_code,1)
print(country_code)

delete(country_code,12)

