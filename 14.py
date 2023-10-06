list=["gajera","virang","nareshbhai","laxmanbhai"]


if len(list)%4==0:
    list.append("bachubhai") 
else:
    list.remove("virang")
    print(list)