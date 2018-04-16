words = "its thanksgiving day. its my birthday, too!"

print words.find('day')

print words.replace("day", "month", 1)


mylist = [2,54,-2,7,12,98]
print min(mylist)
print max(mylist)


alist = [19,2,54,-2,7,12,98,32,10,-3,6];
alist.sort();

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]
print alist

print split_list(alist, wanted_parts=2)
