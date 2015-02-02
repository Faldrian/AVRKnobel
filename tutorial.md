Einrichtung des Raspberry Pi
----------------------------

GPIO-Treiber installieren:
```python
pacman -Sy file base-devel abs git  
wget https://aur.archlinux.org/packages/ra/raspberry-gpio-python/raspberry-gpio-python.tar.gz
tar xf raspberry-gpio-python.tar.gz
cd raspberry-gpio-python
makepkg -Acs --asroot
pacman -U raspberry-gpio-python<hit-tab-key-here>
```

Hilfeseite zur Library: [raspberry-gpio-python/wiki/Inputs/](http://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/)

Info zum Layout des Rev.2 Model B-Boards: [Pin-Belegung und so Zeugs](http://www.instructables.com/id/Simple-and-intuitive-web-interface-for-your-Raspbe/)