
def odd_even(arg):
    for number in range(1, (arg+1), 1):
        if number % 2 == 0:
            print("Number is {}. This number is even".format(number))
        else:
            print("Number is {}. This number is odd".format(number))

odd_even(2000)


multlist = [1, 5, 25, 100]

def multiply(multlist, mult):
    for numberinlist in multlist:
        numberinlist = numberinlist * mult
        print multlist

mult = 5
multlist = [1, 5, 25, 100]
multiply(multlist, mult)
