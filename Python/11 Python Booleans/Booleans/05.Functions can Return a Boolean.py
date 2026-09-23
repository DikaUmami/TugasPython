#You can create functions that returns a Boolean Value:
#Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

#You can execute code based on the Boolean answer of a function:
#Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  #Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
  #Check if an object is an integer or not:

x = 200
print(isinstance(x, int))