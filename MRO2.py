class A:
    def m1(self):
        print("This is m1")
class B(A):
    def m2(self):
        print("This is m2")
class C(A):
    def m3(self):
        print("This is m3")
class D(B):
    def m4(self):
        print("This is m4")
print(D.mro())

