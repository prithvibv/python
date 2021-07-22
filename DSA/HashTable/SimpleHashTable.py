# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/ 
#the elements inside the list is a tuple('25','usa')
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

print("Search result")
print(search(country_code,"25"))

insert(country_code,1,'Australia')
print(country_code)