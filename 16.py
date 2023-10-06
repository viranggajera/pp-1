##Write a Python function to reverses a string if its length is a multiple of 4


def reverce(s):
    str=""
    for i in s:
        str=i+str
    return str

s="gajera"

print("the oringnal value is:", end=" ")
print(s)

print("the reverse value is using loop:",end=" ")
print(reverce(s))


a=input("enter a your string:")

print(reverce(a))

