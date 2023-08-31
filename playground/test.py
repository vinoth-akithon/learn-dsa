


class Sample:
    pass

class Sample1():
    pass

class Sample2(object):
    pass

class Sample3(Sample2):
    pass

sam = Sample3()

print(type(Sample))
print(type(Sample1))
print(type(Sample2))
print(type(Sample3))


print(type(Sample.__base__()))
print(type(Sample1.__base__()))
print(type(Sample2.__base__()))
print(type(Sample3.__base__()))

print(Sample3.__bases__)