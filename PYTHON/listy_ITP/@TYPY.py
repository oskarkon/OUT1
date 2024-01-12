# lista=['1976-10-12','2015-04-30','2012-01-18']
# slownik={'Konrad':'1976-10-12', 'Kuba':'2015-04-30','Ola':'2012-01-18'}
# krotka=('1976-10-12','2015-04-30','2012-01-18')
# zbior={'2015-04-30','2012-01-18'}
# a=['2012-01-18']
# lancuch='Konrad'

# krotka

# from PYTHON.modul import vsearch as v
#
# v.search4letters('konrad')

def double(arg):
    print('Przed :' , arg )
    arg = arg *2
    print('Po: ', arg)

def change(arg):
        print('Przed:' , arg)
        arg.append('wiecej danych')
        print('Po:     ', arg)