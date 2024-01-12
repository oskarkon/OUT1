# -*- coding: utf-8 -*-
# person3={'Nazwisko': 'Ford Prefect',
#          'Płeć': 'mężczyzna',
#          'Zawód': 'badacz',
#          'Planeta macierzysta':'Betelgeza Siedem'}


vovels=['a','e','i','o','u']
word=input("podaj")
found={}
# found['a']=0
# found['o']=0
# found['e']=0
# found['u']=0
# found['i']=0
for letterr in word:
    if letterr in vovels:
        found.setdefault(letterr,0)
        found[letterr]+=1
for k,v in sorted(found.items()):
    print(k, v)
