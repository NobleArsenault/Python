from datetime import datetime

class call(object):
    def __init__(self, id, name, phone, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = datetime.now()
        self.reason = reason

    def display(self):
        print("{} | {} | {} | {} | {}".format(self.id, self.name, self.phone, self.time, self.reason))

#call1 = call(1, "Nina", "123-1234", "just because")
#call1.display()

class callcenter(object):
    def __init__(self):
        self.calllist = []

    def add(self, id, name, phone, reason):
        new_call = call(id, name, phone, reason)
        #new_call.display()
        self.calllist.append(new_call)
        #print self.calllist
        print("Call added to list")
        return self

    def remove(self):
        if len(self.calllist) > 0:
            self.calllist.pop(0)
            print ("call removed")
        else:
            print("there are no calls to remove")
        return self

    def info(self):
        print("legth of queue: {}".format(len(self.calllist)))
        for call in self.calllist:
            call.display()
        return self


center1 = callcenter()
center1.add(1, "Nina", "123-1234", "just because").add(2, "rob", "123-1274", "just because").info().remove().info().remove().info()
