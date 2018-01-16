def drawstars( thelist ):
    for element in thelist:
        if type(element) == int:
            n = "*" * element
            print n
        if type(element) == str:
            a = 0
            a = element[:1] * len(element)
            print a

drawstars( [1, "sum ting wong", 69, 666, "fucking took forever because of a stupid bug"] )