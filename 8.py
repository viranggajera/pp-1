## Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 



def check_nbr (x,y):
    if x==5 or (x*y)==10 or (x-y)==10:
        return True
    else:
        return False
    
    print(check_nbr(5,2))
    print(check_nbr(2,5))
    print(check_nbr(10,5))
    print(check_nbr(5,5))