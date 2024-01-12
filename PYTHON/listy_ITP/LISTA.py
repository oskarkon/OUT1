# odds = [1, 3, 5, 7,9,11,13,15,17,19,21
#     ,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
# print(type(odds))
#
# prices=[]
# temps=[0.0,100.0,-17.78,27.5,37.78,7.39]
# words=['witaj','swiecie']
# car_details=['Toyota','RAV4', 2.2, 60807]
#
# # print(words)
#
# everything=[prices,temps,words,car_details]
# print(everything)
#
#
# # vovels=['a', 'o', 'e', 'i', 'u']
# # word = "Miliard"
# # foung=[]
# # for i in word:
# #     if i in vovels:
# #         print(i)
#
#
# vovels=['a', 'o', 'e', 'i', 'u']
# word = input("podaj słowo :")
# found=[]
# for i in word:
#     if i in vovels:
#         if i not in found:
#             found.append(i)
# for i in found:
#     print(i)

# nums=[1,2,3,4]
# nums

paranoid_android='Marvin, paranoiczny android'
letters=list(paranoid_android)

# for i in letters:
#     print('\t',i)
# print()
for i in letters[:6]:
    print('\t',i)
print()
for i in letters[-7:]:
    print('\t'*2,i)
print()
for i in letters[8:19]:
        print('\t'*3,i)
