

user = input('Enter you string: ')

def theuser(user):
    fadhel = user.split()
    d={}

    for x in fadhel:
        if x not in d.keys():

            d[x] = 0
        d[x] += 1
    print(d)


theuser(user)

'''
username = input('enter: ')

def strring(username):

    var = username.split()
    dict = {}

    for x in var:
        if x not in dict.keys():
            
            dict[x] = 0
        dict[x] += 1
    print(dict)

strring(username)
'''
        

