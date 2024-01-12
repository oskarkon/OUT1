

word='butelki'
for i in range(4,0,-1):
    print(i,word, "piwa na scianie")
    print(i,word, "piwa")
    print('jedna weź')
    print("podaj w koło")
    if i==1:
        print( "Nie ma już butelk piwa")
    else:
        new_i=i-1
        if new_i==1:
            word="butelka"
            print(new_i,word, "piwa na scianie")
    print()