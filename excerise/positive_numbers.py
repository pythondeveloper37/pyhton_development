# Verify the Given Number is Positive or not

val = int(input("Input Number"))
if val >= 0:
    print("Its a positive number", val)
else: 
    print("Negative Number", val)

# with function 
def verify_postive(val): 
    if val >=0: 
        return "positive number", val
    else: 
        return "negative number", val

val = int(input("provide a number to check is positive or negative"))
msg, value = verify_postive(val)
print(msg, value)

# Class Function 

class Exercise1:
    def positive_check(val):
        if val >0:
            return "positive number", val
        else: 
            return "negative number", val

val = int(input("provide a number"))
msg, value = Exercise1.positive_check(val)
print(msg, val)