
test_str = 'geekforgeeks is for geeks'


print("The original string is : " + str(test_str))

mid_str = "best"

words = test_str.split()

mid_pos = len(words) // 2

words.insert(mid_pos, mid_str)

res = ' '.join(words)


print("Formulated String : " + str(res))
