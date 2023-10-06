name="gajera virang nareshbhai"
print("the oringinal string is:" +str(name))

mid_str="and"

word=name.split()

mid_pos=len(word)//2

word.insert(mid_pos,mid_str)


res=" ".join(word)

print("after string is:" +str(res))