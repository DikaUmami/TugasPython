#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

#A placeholder can include a modifier to format the value. A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#A placeholder can contain Python code, like math operations:
#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)