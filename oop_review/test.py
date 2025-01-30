class A:
    # def greeting(self):
    #     print("Hello from A")
    pass
        
        
class B:
    def greeting(self):
        print("Hello from B")
class C(A):
    def greeting(self):
        print("Hello from C")
    
    
class D(A, B):
    # def greeting(self):
    #     print("Hello from D")
    pass

class E(D, C):
    pass

c = E()
c.greeting()