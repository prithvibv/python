""" result = [1,2,3,4]

def listToInt(ip):
    r = ""
    for i in ip:
        r += str(i)
    return int(r)

print(type(listToInt([2,3,4]))) """
#print(ord('A'))

""" i = 5 
print("integer"+ i) """

#Linear probing: (n+1)%TABLE_SIZE
#quadratic probing: (n+i^2)%TABLE_SIZE
#double hashing: (h1 + i h2)%TABLE_SIZE
#h1 = key % TABLE_SIZE
#h2 = PRIME – (key % PRIME)
#PRIME is a prime smaller than the TABLE_SIZE
# In java implementation 31 is chosen

lst = [10,20,30,40]
for i in range(len(lst)):
    print(lst[i])