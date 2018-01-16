girls = [
     {'first_name':  'Ashley', 'last_name' : 'Kim'},
     {'first_name' : 'Mya', 'last_name' : 'Baker'},
     {'first_name' : 'Emily', 'last_name' : 'Milton'},
     {'first_name' : 'Cecelia', 'last_name' : 'Tucker'}
]

def dames (mydic):
    for item in mydic:
        print item['first_name'] + " " + item['last_name']

dames (girls)

"""
def dames( mydic ):
    for i, entry in enumerate(mydic):
        print (i + 1) 
        print entry['first_name']


dames(students)
"""

"""
for i, entry in enumerate(myList):
    print i;
    print entry['age'];
"""
"""
def dames( mydic ):
    firstname = [key['first_name'] for key in mydic]
    print (firstname)

dames(students)
"""



users = {
 'Students': [
     {'first_name':  'Nick', 'last_name' : 'Russ'},
     {'first_name' : 'Aly', 'last_name' : 'Kandeel'},
     {'first_name' : 'Jake', 'last_name' : 'Aramayo'},
     {'first_name' : 'Tye', 'last_name' : 'Online'}
  ],
 'Instructors': [
     {'first_name' : 'Noble', 'last_name' : 'Arsenault'},
     {'first_name' : 'Chow', 'last_name' : 'From The Hangover'}
  ]
 }
"""
def peep(dic):
 for key, value in dic.iteritems() :
    print key, value

peep(users)
"""
"""
def peep(dic):
    for key in dic:
        val = '%('+key+')s'
        print key, val % dic

peep(users)
"""
"""
d={'a':'apple','b':'ball'}
d.keys()  # displays all keys in list
['a','b']
d.values() # displays you values in list
['apple','ball']
d.items() # displays you pair tuple of key and value
[('a','apple'),('b','ball')
"""
"""
def peep(dic):
    for k, v in dic.iteritems():
        print k, v

peep(users)

"""
"""
def peep(dic):
    for kv in dic.items():
        print kv[0],'\t',kv[1]

peep(users)
"""
"""
def peep(dic):
    for people in dic:
        print people

peep(users)
"""
def peep(dic):
    for key,data in dic.iteritems():
        print key
        count = 0
        for value in data:
            count += 1
            print str(count) + ' - ' + value['first_name'] + ' ' + value['last_name'] + ' - ' + str(len(value['first_name']) + len(value['last_name']))

peep(users)