## Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 


str1=(input("enter a first sting:"))
str2=(input("enter a second string:"))

##kano
##noka

a1=str2[:2] + str1[2:]
b1=str1[:2] + str2[2:]


print("first string after swaping:",a1)
print("second string after swaping :",b1)