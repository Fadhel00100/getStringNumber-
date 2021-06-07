import numpy as np

'''
a = np.array([1,2,0])
b = np.array([5,3,10])
w = np.array([5,3,10])
q = np.array([5,3,10])

c = np.sum((a,b,w,q), axis=1)
j = 0
for x in c:
    print('number' + str(j)+ ':'+  f'{x}')

    j = j + 1 

'''


number = 'FadhelBenAbdiAndOneOf'

def camcase(number):
    nu = 0
    for x in range(len(number)):
        if number[x] == number[x].upper():
            nu = nu + 1
    return nu


fadhel = camcase(number)
print(f'the number of the cammal case is: {fadhel}')

# THis is the dictanarey file to do the what we tery to make it more than one tine 
name = {
    'name':'Fadhel',
    'ID':'1234',
    'date':'Nov, 12',
    'teacher':'Sam' 
}

   
print(name.keys())
print(name.values())
