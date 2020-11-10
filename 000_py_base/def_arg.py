# coding: utf-8


## default para
def test(a, b, c=1):
    print(type(a))
    print(type(b))
    print(type(c), c)


test(2, "b")
test(2, "b", "cc")


## args
def foo(a, b, *args):
    print(type(a))
    print(type(b))
    print(type(args), args)


foo(1, 3, "我是", [2, 3, 3, 3])
print(str('我'))


## dict
def bar(a, b, **kw):
    print(type(a))
    print(type(b))
    print(type(kw), kw)


dict1 = {"1": "one", "2": "two"}
bar(1, 3, dict1=dict1)
