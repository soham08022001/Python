#Tuple
days = ('sun', 'mon', 'tue', 'sun', 'sun')
#Check Type
print(type(days))
#Check Index
print(days.index('mon'))
#Count no.times word arrived
print(days.count('sun'))
#########
#DICTIONARY
marks= {'physics':85, 'chemistry':94, 'biology':87}
#Type
print(type(marks))
#ADD MARKS
marks['Maths'] = 88
print(marks)
#particular key:value
print(marks.get('physics'))
print(marks.get('biology'))
print(f"I have obtain {marks.get('chemistry')} in Chemistry" )
print(marks.get('Maths'))
chemistry= marks.get('chemistry')
print(chemistry)
#Added Concatenation
print(f"Samir has obtain {marks.get('physics')} in Physics" )