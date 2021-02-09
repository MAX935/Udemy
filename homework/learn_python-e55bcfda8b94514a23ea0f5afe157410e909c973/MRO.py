class A:
    def some_method(self):
        print('Method of class A')



class B(A):
    def some_method(self):
        print('Method of class B')



class C(A):
    def some_method(self):
        print('Method of class C')


class D(B, C):
    def some_method(self):
        print('Method of class D')


obj_D = D()
obj_D.some_method()



help(D)