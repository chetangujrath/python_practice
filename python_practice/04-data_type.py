s = "hello world" #sting data type
print(type(s))

i = 25 #integer
print(type(i))

f = 3.14 #float
print(type(f))

b = 10 < 20
#b = True #boolean
print(b)
print(type(b))

l = ["aws","azure","gcp"] #list
print(type(l))

t = ("aws","azure","gcp") #tuple
print(type(t))

s = {"aws","azure","gcp"} #set
print(type(s))

r = range(5) #range
print(type(r))
print(list(r)) #print range list

d = {
    "name" : "Chetan",
    "age" : 39,
    "lname" : "Sharma"
}
print(d)
print(type(d)) #dictonary

f = frozenset([1,2,3,4,5]) #frozenset
print(f)
print(type(f))

n =  None #Nonetype
print(n)
print(type(n))

b = b"hello" #bytes or binary type
print(b)
print(type(b))

a = bytearray([97,98,99,96]) #bytearray
print(a)
print(type(a))