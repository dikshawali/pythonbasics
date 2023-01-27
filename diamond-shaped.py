# this is a problem that is an issue for most of the programming language but not in python because of order

    #     A
    # /       \
    # B       C
    # \       /
    #     D



class A:
    var='A'
    print(var)

class B(A):
    var=('Inside class B')
    print(var)

class C(A):
    var=('inside class C')
    print(var)

class D(B, C):
    pass
    # var('Inside class D')

a=D()
print('Final result=')
print(a.var)