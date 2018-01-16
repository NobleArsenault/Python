# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = []

for item in word_list:
    for letter in item:
        if letter is char:
            new_list.append(item)
print new_list

pr



"""
for item in range(len(word_list))
    print item
    print (word_list[item])
"""


