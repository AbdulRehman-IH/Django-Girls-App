
#creating a function which compares two integers
def compare_integers(a=0,b=0):
    if (a > b):
        print(f"{a} is greater than {b}")
    elif (a<b):
        print(f"{a} is less than {b}")
    else :
        print(f"{a} and {b} are equal")

#Calling the above created function
compare_integers(20,50)

'''experimenting with range function please note that range function
    is inclusive from left but exclusive from right'''
for i in range(10,20):
    print(i)

#Simple for loop on a List
countries_visited = ['Pakistan', 'Turkey', 'Amstradam']
for i in countries_visited:
    if (i == 'Pakistan'):
        print(f'you\'ve visited {i}')


        