import sys


def fundk_1():
    pass


class Human:
    pass


rq=request
fun=funck_1
nick=Human

print(request.__name__)
print(rq.__name__)
print(fun.__name__)
print(funck_1.__name__)
print(human.__name__)
print(nick.__name__)
print(__name__)
print(type(2))
print(type(2.9))
print(type(2==2))
print(type("gfgfg"))
print(type(list))

#intro_list=[]
#for method in dir(intro_list):
    #print(method)

set={}
for method in dir(set):
    print(method)

print(inspect.ismodule(request))
print(inspect.isfunction(request))
print(inspect.isclass(Human))
print(inspect.getmodule(request.get))
print(inspect.getmodule(list))

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)

for _ in dir(__builtins__):
    print(_)