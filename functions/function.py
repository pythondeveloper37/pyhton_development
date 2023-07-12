def even(i, j, list):
    print("list",list)
    while j < i:
        j+=1
        if j%2==0:
            print("Even Number", j)

def evenList(evli):
    print(evli)

evli = [2,4,6,8]
# evenList(evli)          
even(10, 0, evli)

