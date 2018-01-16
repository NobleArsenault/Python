check1 = "* * * *"
check2 =  " * * * *"

for firstline in range (0, 9, 1):
    if firstline % 2 == 0:
        print check2
    else:
        print check1
