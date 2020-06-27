import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
d ='cmatrix'
def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','>
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


def banner():
    os.system('clear')
    print(a+'Shortcut for help you'.center(40))
    print(b+'【CLAY】'.center(40))
    print(b+'⫷instagram⫸ : inds_clay'.center(20))
    print(b+'⫷Facbook⫸   : inyoman clay'.center(20))
    print(b+'⫷whatsapp⫸  : 081380407571'.center(20))
    print(d+''.center(40))
    print("".join([i for i in "\n"*3]))


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print('\rPlease wait '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
# ini cuma shortcut buat bantu para nub
# CLAY