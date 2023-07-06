# Conditional Operator 
# a = 6
# val = input("provide value") 
# val = int(val)

list = [1,2,3,4,5]

for val in list:
    if val%2==0: 
        print("Even Number", val * 2)
    elif val%2!=0:
        print("Odd Number", val)
    else: 
        print("value is greater than 100")