## Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 



def sum_three(x,y,z):

    if x==y or y==z or z==x:
        sum=0
    else:
        sum=x+y+z
    return sum

print(sum_three(10,20,10))
print(sum_three(30,20,10))
print(sum_three(20,30,20))
print(sum_three(30,10,20))

