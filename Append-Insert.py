user = ['SOHAM','SATYAJIT']
#ADD WORD IN LIST
user.append('PATIL')
print(user)
#Replace WORD
user[0] = 'SOM'
print(user)
#Remove Word From List
user.remove('SOM')  #print(user.pop(0)) Show result
print(user)
#Insert/append word at INDEX
user.insert(0, 'Mr.')
print(user)
#DELETE WORD From LIST
del user[0]
print(user)
#Number of Items in List
print(len(user))
#Sorting In alphabeticals
user.insert(0, 'SOHAM')
user.sort()
print(user)
