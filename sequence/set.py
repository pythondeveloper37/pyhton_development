# Sequence Data Type set 

sampleSet = {"apple", "mango", "orange", "orange"}

print("apple" in sampleSet)

sampleSet.add("Banana")
print(sampleSet)

sampleSet.remove("mango")
print(sampleSet)

newSample = {"Carrot", "Beetroot"}
sampleSet.update(newSample)
print(sampleSet)