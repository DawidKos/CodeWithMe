# import requests
# from coloratura import cprint, Pantone, Bit4

# print('KLUCZE:'
#       'id_stacji,'
#       'stacja,'
#       'data_pomiaru,'
#       'godzina_pomiaru,'
#       'temperatura,'
#       'predkosc_wiatru,'
#       'kierunek_wiatru,'
#       'wilgotnosc_wzgledna',
#       'suma_opadu,',
#       'cisnienie')

# imgw = requests.get('https://danepubliczne.imgw.pl/api/data/synop').json()
#
#
# def pogoda(miasto, czynnik):
#     for i in imgw:
#         if i['stacja'] == miasto:
#             cprint(i['stacja'], color=Pantone.ILLUMINATING)
#
#             if czynnik == 'tmp':
#                 temperatura = float(i['temperatura'])
#                 if temperatura <= -1:
#                     cprint(i['temperatura'], color=Pantone.CLASSIC_BLUE)
#                 elif 0 <= temperatura <= 10:
#                     cprint(i['temperatura'], color=Bit4.BLUE)
#                 elif 11 <= temperatura <= 20:
#                     cprint(i['temperatura'], color=Pantone.ILLUMINATING)
#                 elif 21 <= temperatura <= 30:
#                     cprint(i['temperatura'], color=Pantone.LIVING_CORAL)
#                 elif temperatura >= 31:
#                     cprint(i['temperatura'], color=Bit4.RED)
#
#
# pogoda(input('Podaj nazwę miasta: '), input('Podaj nazwę klucza: '))


# lista = [60, 77, 76, -74, -56, -16, -15, -63, -87, -38]
# max = lista[0]
# for i in lista:
#     if max < i:
#         max = i
# print(max)
import naz as naz

# a = ['a', 94, 'c', 64, 98]
# b = [43, -49, -25, -50, -91]
#
# dictionary = dict(zip(a, b))
# print(dictionary)


