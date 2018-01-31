l = ['magical unicorns',19,'hello',98.98,'world']


sumint = 0
for item in l:
    if type(item) is int or type(item) is float:
        sumint = sumint + item
print ("sum of numbers", sumint)

sumstr = []
for item in l:
    if type(item) is str:
        sumstr.append(item)
print ("sum of strings {} {}".format(sumstr, sumint))
