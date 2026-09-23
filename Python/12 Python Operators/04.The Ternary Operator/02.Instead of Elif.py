#Assign:
# "Fri" if num is 5
# at" if num is 6
# "Sun" if num is 7
#  otherwise assign "weekday":

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)