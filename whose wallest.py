import random 
print ('welcom to "whose wallest"? ')
print ('you will give me a list of names , and i will pick a person to pay  ')
name= input ('If you are ready , enter the names separated by a comma \n') . split (', ')
print (f'please ask "{random.choice(name)}" to take his wallest out , dinner is on him')
