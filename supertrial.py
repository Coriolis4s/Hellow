'''
This is the basic clas inheriting from object.
'''
class A(object):
    def __init__(self, name):
        self.name = name
    def printl(self):
        print "This is class A's constructor %s, %s" %(repr(self), self.name)
'''
This is one angle of the diamond diagram.
'''
class B(A):
    def __init__(self, name):
        super(B, self).__init__(name)
    def printl(self):
        super(B, self).printl()
        print "this is class B: %s, %s" %(repr(self), self.name)
'''
This is the other class.
'''
class C(A):
    def __init__(self, name):
	super(C, self).__init__(name)
	print "this is class c: %s, %s" %(repr(self), self.name)
    def printl(self):
	super(C, self).printl()
	print repr(self)
'''
This is the fourth class that has multiple inheritance.
'''
class D(C, B):
    def __init__(self, name):
	super(D, self).__init__(name)
	#self.name = name
	print "this is class d %s, %s" %(repr(self), self.name)
    def printl(self):
	super(D, self).printl()
	# self.__mro__
	# from pprint import pprint

# b = B("a")
# b.printl()
d = D("b")
d.printl()
tuplet = D.__mro__
for i in xrange(len(tuplet)):
    print tuplet[i]
