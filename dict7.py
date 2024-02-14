'''7. Check if a value exists in a dictionary'''
'''
lst1=['course','fee','Duration','discount']

lst2=[]

lstkey=[]

print("Enter the course,fees,duration,discount")

for i in range(4):

    item=input("Enter the items to be added to dictionary")

    lst2.append(item)

newdict=dict(zip(lst1,lst2))

print(newdict)

value=input("Enter the value that has to be checked in the dictionary")

for x in newdict.values():

    lstkey.append(x)

if value  in lstkey:

    print(value,"is present")

else:

    print(value,"not present")
'''

'''8. Rename key of a dictionary'''

lst1=['course','fee','Duration','discount']

lst2=[]

lstkey=[]

print("Enter the course,fees,duration,discount")

for i in range(4):

    item=input("Enter the items to be added to dictionary")

    lst2.append(item)

newdict=dict(zip(lst1,lst2))

print(newdict)

key=input("Enter the value that has to be removed in the dictionary")

for x in newdict.keys():

    lstkey.append(x)

print(lstkey)

if key in lstkey:

    del newdict("key")

print("The dictionary after removing the required key",newdict)

'''9. Get the key of a minimum value from the following dictionary'''

'''lst1=[]

lst2=[]

for i in range(5):

    items=input("Enter the items to be added to the dictionary")

    lst1.append(items)

for i in range(5):

    item=input("Enter the items to be added to dictionary")

    lst2.append(item)

newdict=dict(zip(lst1,lst2))

print("The converted dictionary is :",newdict)

x=min(newdict.values())

print("The minimum value in the dictionary is",x)

res=[key for key in newdict if newdict[key]==x]

print(" The key of the minimum value is:",res)'''

'''Change value of a key in a nested dictionary'''

'''Employee = {

    'emp1': {

        'name': 'Lisa',

        'age': '29',

        'Designation':'Programmer'

            },

    'emp2': {

             'name': 'Steve',

             'age': '45',

             'Designation':'HR'

             }

}

print(Employee)

empno=input("Enter the employee number(1,2)")

print(empno)

changekey=input("Enter the key to be changed")

print(changekey)

changedvalue=input("Enter the value to be changed to")

print(changedvalue)

Employee[empno][changekey]=changedvalue

print("The edited dictionary is",Employee)'''
