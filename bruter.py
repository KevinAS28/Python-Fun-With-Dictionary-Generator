#!/usr/bin/python3

#my english is bad. i hope you understand what i say :)
#create dictionary with word you  type
#using python 3.5
#just type any word and separated by space.example: this is a word
#to edit leet mode go to line 346. and you need to edit that
#dont forget to like and leave comments
#inspired from CUPP.
#in the word file, some of them is the same.so run bruter11.py to remove the same
#if you want to repost it, please tell me first. email me to adiasoymantap@gmail.com (not my real email. so dont try to bruteforce it :). need 1 week to write it. )
#if you want ask anything, just email me, or leave comment
#want to thanks to me? just pray me so i can be great programmer
#by kevin agusto, from indonesia. now 16 years old




#import daemon
import os
import sys
import time
from getpass import getpass
import string
import platform                              
import pkg_resources


#kata apa saja
#kata_apa(dan seterusnya)
#kata_ajas(dibalik yang kedua)
#atak_saja(dibalik yang pertama)
#atak_ajas(dibalik dua2nya)

#lakukan yang sebelumnya tapi dengan mode 133t dan simbol penghubung yang berbeda


try:

 spab = (lambda x: [print(' ') for taudah in range(x)])
 spabjadul = """def spab(x):
  for nivek in range(x):
   print(' ')"""
 enter = (lambda x: [print("""
""") for eyentes in range(x)])
 enter1 = """
"""



 print("""
``````##``````##````````````````````````````````````````````````````````````````
``````##`````##`````######`````##```````````````##``####``##```#####````````````
``````##````##`````#``````#`````##`````````````##```####``##``#````##```````````
``````##```##`````#````````#`````##```````````##``````````####``````#```````````
``````##``##`````#``````````#`````##`````````##`````####``##````````#```````````
``````##`##`````#```#########``````##```````##``````####``##````````#```````````
``````####```````#``````````````````##`````##```````####``##````````#```````````
``````####````````#``````````````````##```##````````####``##````````#```````````
``````##`##````````#``````````````````##`##`````````####``##````````#```````````
``````##``##````````#########``````````##```````````####``##````````#```````````
``````##```##```````````````````````````````````````````````````````````````````
``````##````##``````````````````````````````````````````````````````````````````
``````##`````##`````````````````````````````````````````````````````````````````
``````##``````##````````````````````````````````````````````````````````````````

""")
 time.sleep(2)
 os.system('clear')
 spab(5)
 print('versi python yang digunakan: %s' %(sys.version))
 spab(1)
 #cek versi python
 pyv = list(sys.version)
 if pyv[0] == '2':
  spab(3)
  print('''PERINGATAN!!! ANDA SEDANG MENGGUNAKAN PYTHON VERSI 2.
SEDANGKAN PROGRAM INI DIBUAT DI VERSI 3''')
  spab(3)
  time.sleep(2)
 print('os yang digunakan: %s . detail: %s' %(platform.system(), os.name))
 time.sleep(1)
 spab(3)
 print('''
 LOGIN''')
 spab(2)
 user = input('username: ')
 spab(1)
 print('password yang diketik tidak akan terlihat')
 sandi = getpass('password: ')
 spab(3)
 usvalid = ['kevin']
 savalid = ['otsuganivek']
 try:
  yang = usvalid.index(user)
 except:
  print('username atau password salah')
  print('dasar penipu :) ')
  sys.exit() 


 if (user == usvalid[yang]) and (sandi == savalid[yang]):
  spab(3)
  print('username dan password valid. selamat datang kevin :) ')
  time.sleep(1)
  spab(3)
 else:

  print('username atau password salah')
  print('dasar penipu :) ')
  sys.exit()



 os.system('clear')
 

 
 #kata-katanya diproses ke list dan rapih
 words = input('word = ')
 word = list(words)
 word.append(' ')
 


 def rang():
  global one
  global satu
  global null
  global nol
 
  one = 1
  satu = 1
  null = 0
  nol = 0
 #mengetahui letak spasi
 jumlh = int(len(word))
 #null = 0
 rang()
 spasi = []
 for abc in range(jumlh):
  if word[null] == ' ':
   spasi.append(null)
  null += 1
 
 spab(3)
 #kata yang terpisah oleh spasi
 #null = 0
 #nol = 0
 #one = 1
 rang()
 kata = []
 kataa = []
 
 spc = int(spasi[null])
 kata.append(word[:(spasi[null])])
 for wow in range(len(word)):
  try:
   kata.append(word[(spasi[null]):(spasi[one])])
   null += 1
   one += 1
  except:
   pass
 
 rang()
# print(kata)


 #menghapus spasi dalam kata
 btpn = len(kata)
 for masasih in range(btpn):
  try:
   kata[nol].remove(' ')
  except:
   try:
    kata[satu].remove(' ')
    satu += 1
   except:
    pass
 

 spab(3)
 #print(kata)


#============================================================
#membuat dictionary

#mempersiapkan file
 rang()
 dirs = os.getcwd()
 print('skarang ada di direcotry: %s' %(dirs))
 time.sleep(1)
 fname = input('file name you want: ')
 ada = os.access(fname, os.W_OK)
 if ada == True:
  sdhada = input('file is exist.want to replace? y/n ')
  if sdhada.lower() == 'y':
#   os.system('touch %s' %(fname))
   print(os.access(fname, os.W_OK))
  else:
   print('ga jadi program keluar')
   sys.exit()
 else:
  os.system('touch %s' %(fname))
  print(os.access(fname, os.W_OK))

#menulis
 rang()
 brut = len(kata)
 jmlhk = []
 rang()
 jaditext = []
 selsai = False
 oke = """while not selsai:
  try:
   with open(fname, 'a+') as python:
#   jmlhk.append(kata[null][nol])
    python.write(kata[null][nol])
    
    
  except:
   selsai = True
  nol += 1"""
 rang() 

######################
#BAGIAN TULIS MENULIS#
######################
 def tulis():
  with open(fname, 'a+') as python: #tinggal nulis ini mah
   python.write(kata[nol][null])  


 
 
 def jalankan():
  global nol
  global null
  while not selsai:
   if nol > (brut + 1):
    break
   try:
    tulis()
    null += 1
   except:
    null = 0
    nol += 1
    with open(fname, 'a+') as asus:
     asus.write('\n')
    jalankan() 

 jalankan()
 
#konsep logika
 try:
  if nol == (len(kata[null])):
   nol = 0
   null += 1
   os.access(fname, os.W_OK)
       
 except:
  pass
############ 
#biar baris kosong 1
 with open(fname, 'a+') as java:
  java.write('\n')  
    
 solo = []
 #mencoba tulis dengan gabungan kata underscore
 rang() 
 def tulisund():
  global nol
  global null
  global solo
  global solo
  for wow in range(brut + 1):
   try:
    solo.append(str(kata[nol]))
    solo.append('_')
   except:
    pass
   nol += 1
 
 
 
 tulisund()

 #mencoba menghapus simbol terakhir
 smbtr = (len(solo)) - 1
 solo[smbtr] = ''

# smbtr = len(solo)
# solo[smbtr] = ''

 soloo = str('''"''' + (str(solo)) + '''"''')
 rang()
 sol0 = soloo.replace('[', '')
 sol1 = sol0.replace(']', '')
 sol2 = sol1.replace('''"''', '')
 sol3 = sol2.replace("""'""", '')
 sol4 = sol3.replace(',', '')
 sol5 = sol4.replace(' ', '')
# solooo = soloo.replace("""'""", ''), soloo.replace('''"''', '')#, soloo.replace("[", ''), soloo.replace("]", ''), soloo.replace(",", '')
 
 

 with open(fname, 'a+') as cpu:
  cpu.write(str(sol5))
 #print(solo)
 #print(sol5)

#biar baris kosong 1
 with open(fname, 'a+') as java:
  java.write('\n')

 rang()
 symb = ["_", " ", "-", "~", "=", "%", ">", "<", "+", ""]

#teknik normal_normal (dua kata dengan underscrore)
 und2l = []
 rang()


 def und2():
  #dirapihin dulu#
  #menghapus simbol terakhir
  global enter1
  null = 0
  nol = 0
  global und2l
  global one
  global sol5
  for keyboard in range(len(und2l)):
   try:
    und2l[null][(len(und2l[null]) - 1)] = ''
   except:
    break
   null += 1
  #ke baris bawah
  rang()

  rang()
  null = 0
  for nnn in range(len(und2l)):
#   try:
#    print((und2l))
#    und2l = und2l[null]

   
    sol0 = str(und2l[null]).replace('[', '')
    sol1 = sol0.replace(']', '')
    sol2 = sol1.replace('''"''', '')
    sol3 = sol2.replace("""'""", '')
    sol4 = sol3.replace(',', '')
    sol5 = sol4.replace(' ', '')
    sol12 = sol5.replace('a', '@')
    sol13 = sol12.replace('e', '3')
    sol14 = sol13.replace('i', '1')
    sol15 = sol14.replace('B', '8')
    sol16 = sol15.replace('t', '7')
    sol17 = sol16.replace('o', '0')
    sol18 = sol17.replace('s', '5')
    sol19 = sol18.replace('G', '6')
    sol20 = sol19.replace('g', '9')
  

    with open(fname, 'a+') as und22:
     und22.write(str(sol5))
     und22.write('\n')

    null += 1
#   except:
#    null += 1#pass  
 print(nol, null)


 def und222(bingung, owo, sym, reverse, leet):
  global nol
  global null
  global kata
#  global bingung
#  global owo
#  global sym
  rang()
  while True:
   try:
    if owo > (len(kata)):
     bingung += 1
     owo = 0
   except:
    bingung += 1
    owo = 0
   if bingung > (brut + 1):
    break
#   print(und2l)
#   print(null)
   print(owo)
   print(nol)
   try:
    und2l.append((kata[bingung] + sym + kata[bingung] + sym))#sym)) 00 00
    und2l.append((kata[bingung] + sym + kata[owo] + sym))#sym)) 00 10
    und2l.append((kata[owo] + sym + kata[bingung] + sym))#      10 00 
    und2l.append((kata[owo] + sym + kata[owo] + sym))#          10 10
#    und2l.append((kata[bingung] + sym + kata[bingung] + sym))#  00 00
    if reverse == 1:
     semen0 = kata[bingung]
     semen1 = kata[owo]
     und2l.append((semen0.reverse() + sym + semen1 + sym))#01 10
     und2l.append((semen0 + sym + semen1.reverse() + sym))#00 11
     und2l.append((semen0.reverse() + sym + semen1.reverse() + sym)) #01 11
    
     und2l.append((semen1.reverse() + sym + semen0 + sym))#11 00
     und2l.append((semen1 + sym + semen0.reverse() + sym))#10 01
     und2l.append((semen1.reverse() + sym + semen0.reverse() + sym))#11 01


     und2l.append((semen0.reverse() + sym + semen0 + sym))#01 00
     und2l.append((semen1 + sym + semen1.reverse() + sym))#10 11

     und2l.append((semen1.reverse() + sym + semen1.reverse() + sym))#11 11
     und2l.append((semen1.reverse() + sym + semen1 + sym))#11 10     
     und2l.append((semen0.reverse() + sym + semen0.reverse() + sym))#01 01     

     und2l.append((semen0 + sym + semen0.reverse() + sym))#00 01
#     und2l.append((semen0.reverse() + sym + semen0 + sym))#01 00

     und2l.append((semen1.reverse() + sym + semen1.reverse() + sym))#11 11     


   

#    und2l.append((symb[0]))
#    und2l.append((kata[nol]))
   except:
    gabut = 0#    bingung += 1
   owo += 1
  owo, bingung, sym, reverse = 0, 0, 0, 0   
      


 #eksekusi function dengan argument
# for macosx in range(brut):
 rang()
 #for byksm in symb:
 und222(null, nol, (list(symb[0])), 0, 0)
 und222(null, nol, (list(symb[0])), 1, 0)
 und222(null, nol, (list(symb[0])), 0, 1)
 und222(null, nol, (list(symb[0])), 1, 1)

 und222(null, nol, (list(symb[1])), 0, 0)
 und222(null, nol, (list(symb[1])), 1, 0)
 und222(null, nol, (list(symb[1])), 0, 1)
 und222(null, nol, (list(symb[1])), 1, 1)

 und222(null, nol, (list(symb[2])), 0, 0)
 und222(null, nol, (list(symb[2])), 1, 0)
 und222(null, nol, (list(symb[2])), 0, 1)
 und222(null, nol, (list(symb[2])), 1, 1)

 und222(null, nol, (list(symb[3])), 0, 0)
 und222(null, nol, (list(symb[3])), 1, 0)
 und222(null, nol, (list(symb[3])), 0, 1)
 und222(null, nol, (list(symb[3])), 1, 1)

 und222(null, nol, (list(symb[4])), 0, 0)
 und222(null, nol, (list(symb[4])), 1, 0)
 und222(null, nol, (list(symb[4])), 0, 1)
 und222(null, nol, (list(symb[4])), 1, 1)

 und222(null, nol, (list(symb[5])), 0, 0)
 und222(null, nol, (list(symb[5])), 1, 0)
 und222(null, nol, (list(symb[5])), 0, 1)
 und222(null, nol, (list(symb[5])), 1, 1)

 und222(null, nol, (list(symb[6])), 0, 0)
 und222(null, nol, (list(symb[6])), 1, 0)
 und222(null, nol, (list(symb[6])), 0, 1)
 und222(null, nol, (list(symb[6])), 1, 1)

 und222(null, nol, (list(symb[7])), 0, 0)
 und222(null, nol, (list(symb[7])), 1, 0)
 und222(null, nol, (list(symb[7])), 0, 1)
 und222(null, nol, (list(symb[7])), 1, 1)

 und222(null, nol, (list(symb[8])), 0, 0)
 und222(null, nol, (list(symb[8])), 1, 0)
 und222(null, nol, (list(symb[8])), 0, 1)
 und222(null, nol, (list(symb[8])), 1, 1)


 # null += 1
 #null += 1
 # nol = 0

 

 ###function nulis###
 und2()
 ###function nulis
 print(und2l)
# print(null)
 spab(5)
 #print(kata[bingung][-1:0])
 
 
except KeyboardInterrupt:
 spab(5)
 print("""anda telah menekan tombol CTRL + C
 program sekarang keluar""")
 sys.exit()
