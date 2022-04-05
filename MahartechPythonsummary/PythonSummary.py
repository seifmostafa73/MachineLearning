from audioop import reverse


print("Hello world")
#---Types---
'''
Text Type:	str (non scalar)
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''
pi=float(22/7)
piapprox=int(pi)
print(type(piapprox))
print(type(True))
print(type(["apple", "banana", "cherry"]))
print(type(1+9j))

#Tuples:array that their value can't be changed in runtime
tup = ()# defining an empty Tuple
tup = (1,1+1j,"hi")
print(tup[2])
tup2 = tup+('c',) # tuples has to have commas in them
print(tup2)

#Lists : this is an array and you can change it in runtime
lst = []
lst.append("d")
lst.extend([1,3,'c'])
del(lst[0]) #removes element of given index
lst.remove('c') #removes first element of given value
print(lst)
lst.pop() # removes and returns the last element by defaule , can also take an index
lst = sorted(lst) # also reversed for reverse ordering

#Dictionaries : it's an array-like structure where elemtents are indexed by a key
dict = {'key0':'value0',3:'val'}
dict2 = {3:"d"}
print(dict["key0"]) # dict.get("key") is better as it doesn't break the code
dict["newKey"] = 'new value'
dict.keys()#retruns all keys names
dict.values()#returns all values
dict.update(dict2) # adds a dictionary to another one

#---String---
Firstname = "Seif"
Lastname = 'Mostafa'
name = "name:"+Firstname+Lastname
namex3=name*3
print(len(name))
lst = ["hi","Hello",'lkk']
s = ' '.join(lst) #Converting list to string with a character seperator

#---Indexing ---
arrayofint = [1,2,3,"Seif",True,1+9j]
print(arrayofint[3]) # starts from zero
print(arrayofint[-2]) # starts from -1->last element

print(arrayofint[0:2])
print(arrayofint[1:len(arrayofint)]) #not inclusive
print(arrayofint[0:4:2]) #[Start(inclusive):end(exclusive:Stepsize)
print(arrayofint[::-1])

print("Seif" in arrayofint) #checks if element is in array

#---input Function---
x=int( input("Enter an integer ") )
print(x)

#---functions ----
"""
this function prints the sum of two arguments
Input:Arg0:int64,Arg1:int64
Output:None
"""
def PrintInput(Arg0,Arg1):
    print(Arg0+Arg1)
    tup = (Arg1,Arg0)
    return tup # you can return a Tuple !
print(PrintInput(1,3))

#--- 