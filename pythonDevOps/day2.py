#task1
#Task 1: WAP to create a function which returns the sum of all the element provided to it as an arguement. The arguement list will be dynamic.

def variableArgs(*args):
    for arg in args:
        print(arg)

variableArgs('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def variableArgsSum(*args):
    sum = 0
    for arg in args:
        sum += arg
    print("sum: " + str(sum))

variableArgsSum(10,20,30,50)


def addition(*args):
   result = 0
   for i in args:
      result += i
   return result

print(addition(10,20,30,50))

def kwArgs(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

kwArgs(a=1,b=2,c=3)

a_dict = [
    {
        "name": "gara",
        "power": "some sand related jutsu",
        "powerlevel": 199,
        "frieds": [
            {
                "name": "Naruto",
                "friend_points": 28,
                "enemies": ["Saitama"]
            },
            {
                "name": "Boruto",
                "friend_points": 18,
                "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "Alex",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Soniya",
            "friend_points": 128,
            "enemies": ["Saitama"]
            }
        ]
    },
    {
        "name": "King",
        "power": "some titans powers",
        "powerlevel": 1199,
        "frieds": [
            {
            "name": "Saitama",
            "friend_points": 128,
            "enemies": ["Naruto", "gara", "boruto"]
            }
        ]
    }

]

for listElement in a_dict:
    print(listElement["name"])
    print(listElement["power"])
    print(listElement["powerlevel"])
    print(listElement["frieds"][0]["name"])
    print(listElement["frieds"][0]["friend_points"])
    enemies = listElement["frieds"][0]["enemies"]
    for enemy in enemies:
        print(enemy)