listone = [1,2,5,6,2]
listtwo = [1,2,5,6,2]
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
list_one1 = [1,2,5,6,5,16]
list_two2 = [1,2,5,6,5]
listone1 = ['celery','carrots','bread','milk']
listtwo2 = ['celery','carrots','bread','cream']


def comparelist(argument1, argument2):
    if argument1 == argument2:
        print "the lists are the same"
    else:
        print "the lists are not the same"

comparelist(listone, listtwo)
