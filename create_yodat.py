# -*- coding: cp1251; -*-
import shelve

LIST = map(lambda x: x.strip(), open("yo.txt","rt").readlines())
may_be_yo = filter(lambda x: x.startswith("*"),LIST)
only_yo = filter(lambda x: not x.startswith("*"), LIST)
only_yo = map(lambda x: unicode(x,"cp866"),only_yo)
may_be_yo = map(lambda x: unicode(x[2:],"cp866"),may_be_yo)


YO = unicode("ё","cp1251")
E  = unicode("е","cp1251")

class yo(object):
    may_be_yo = {}
    only_yo = {}

for i in may_be_yo:
    yo.may_be_yo[i.replace(YO,E)]=i
for i in only_yo:
    yo.only_yo[i.replace(YO,E)]=i

sh = shelve.open("yo.dat")

sh["may_be_yo"]=yo.may_be_yo
sh["only_yo"]=yo.only_yo
sh.close()
