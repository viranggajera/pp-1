## Write a Python function to reverses a string if its length is a multiple of 4

def revervenumber(str1):
    if len(str1)%5==0:
        return "".join(reversed(str1))
    else:
        return str1
print(revervenumber("abcd"))
print(revervenumber("python"))
print(revervenumber("gajer"))