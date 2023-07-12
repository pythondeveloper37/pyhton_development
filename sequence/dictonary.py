# sequence Data Types 

thDictionary = {
    "name": "naveen", 
    "class":"python",
    "timings":"7 to 8",
}

print(thDictionary)

# print(thDictionary["name"])
# print(thDictionary["class"])
for i in thDictionary.keys(): 
    print(i)

for k in thDictionary.values():
    print(k)   

for j in thDictionary.values():
    if j == "naveen":
        print("value Matches", j) 

for n in thDictionary.keys(): 
    if n == "name":
        print("Key Matches", n)
        if thDictionary[n] == "naveen":
            print("Value Matches", thDictionary[n])


thDictionarys = {
   "batch1": {
    "name": "naveen", 
    "class":"python",
    "timings":"7 to 8",
   },
   "batch2": {
    "name": "naveen", 
    "class":"python",
    "timings":"8 to 9",
   },
   "batch3": {
    "name": "naveen", 
    "class":"python",
    "timings":"9 to 10",
   }, 
   "batch4": {
    "name": "naveen", 
    "class":"python",
    "timings":"10 to 11",
   }
}

for i in thDictionarys.values(): 
    print(i.values())