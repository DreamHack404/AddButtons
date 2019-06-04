import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t    + Tombol Tambahan Termux ')
print(a+'\t    + UP,Down,right,Left, CTRL ')
print(b+'\t    + Author: DreamHack404')
print('\t      + Team : Black Cyber Anonymous')
print('\t      + Facebook : Tumis Kangkung')
print('\t      + Github : https://github.com/DreamHack404')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] Wait dulu ya tolol')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Ditinggal Chat an juga gpp:)!')
sleep(1)
print(b+'\n[!] Bentar lagi done..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Sedikit lagi ya coeg  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Done Muncul kaga coeg?!! '+c+'\nBelum keluar juga? : Hubungi @DreamHack yg Gans:082228270627 No System Is Safe *\n\n')
