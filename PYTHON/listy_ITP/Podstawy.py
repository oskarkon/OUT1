from datetime import datetime
#
# odds = [1, 3, 5, 7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
#
# right_this_minute = datetime.today().minute
# print (right_this_minute)
#
# if right_this_minute in odds:
#     print ('Minuta nieparzysta')
# else:
#     print('Minuta parzysta')
import os
from os import getcwd
import sys
print(sys.platform)
print(sys.version)
print(os.getcwd())
# print(os.environ)
import datetime
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print(datetime.date.isoformat(datetime.date.today()))

import time
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))
from time import gmtime, strftime
print(gmtime())
print(time.strptime("30 Nov 00", "%d %b %y"))

from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

from datetime import datetime

date_string = "2023-11-24 15:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)

datka='2023-11-23'
datakap=datetime.strptime(datka,"%Y-%m-%d")
print('to jest' ,datka)
print(type(datakap))


tera=datetime.now()
print(tera)
datka1=tera.strftime("%Y-%m-%d")
print(type(datka1))

today='Sobota'
if today == "Sobota":
    print('IMpreza!!!')
elif today == 'Niedziela':
    print('Odpoczynek')
else:
    print('praca')