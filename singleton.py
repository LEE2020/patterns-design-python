# Real Singleton instance
class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

a = Singleton()
a.toto = 12

b = Singleton()
print b.toto
print id(a), id(b)  #  same 
