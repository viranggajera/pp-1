#Write a Python function to reverses a string if its length is a multiple of 
#4. 
def revercestring(str1):
    if len(str1)%4==0:
        return ''.join (reversed(str1))
    return str1
print(revercestring("abcd"))
print(revercestring("python"))

