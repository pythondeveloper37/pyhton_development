# Verify the Given Number is Positive or not

val = int(input("Input Number"))
if val %2 == 0:
    print("Its a even number", val)
else: 
    print("odd Number", val)

# with function 
def verify_postive(val): 
    if val %2 == 0:
        return "Its a even number", val
    else: 
        return "odd Number", val

val = int(input("provide a number to check is even or odd"))
msg, value = verify_postive(val)
print(msg, value)

# Class Function 

class Exercise1:
    def even_odd_check(val):
        if val %2 == 0:
            return "even number", val
        else: 
            return "odd number", val

val = int(input("provide a number"))
msg, value = Exercise1.even_odd_check(val)
print(msg, val)