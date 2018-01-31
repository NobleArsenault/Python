print "hello world!"

x = "Hello Python"
print x


print "this is a sample string"


name = "noble"
number = 12
print "My name is", name , number #you can use number or 12 as the integer but cannot concatenate with the + sign

print "My name is " + name


first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)




drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens




x = [1,2,88,4,9]

y = [666,777]
x.append(y)
print x


#for <counter> in <sequence or range>:
  # do something

for doesnothavetobenamedcount in range (0, 5):
    print "looping -", doesnothavetobenamedcount


for val in "string":
    if val == "i":
        break
    print val



for val in "string":
    if val == "i":
        continue
    print val



x='1'
y = 2
print x + str(y)
print str(x) + str(y)
print int(x) + y
print x + y
