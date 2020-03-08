#starter kit
import os
import time


#pierwszy folder 'klasy'
try:
    path0 = '/klasy'
    os.mkdir(path0)
except OSError:
    print ("Stworznie folderu %s zakończyło się niepowodzeniem" % path0)
else:
    print ("Pomyślnie stworzono folder %s" % path0)



#klasy
parent_dir = '/klasy'
try:
    path1 = os.path.join(parent_dir, '1')
    os.mkdir(path1)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path1)
else:
    print ("Pomyślnie stworzono folder %s" % path1)
    
try:
    path2 = os.path.join(parent_dir, '2' )
    os.mkdir(path2)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path2)
else:
    print ("Pomyślnie stworzono folder %s" % path2)
    
try:
    path3 = os.path.join(parent_dir, '3' )
    os.mkdir(path3)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path3)
else:
    print ("Pomyślnie stworzono folder %s" % path3)

#klasa 1
klasa1_dir = '/klasy/1'

try:
    path4 = os.path.join(klasa1_dir, 'Stanisław Dobrzański')
    os.mkdir(path4)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path4)
else:
    print ("Pomyślnie stworzono folder %s" % path4)
    
try:
    path5 = os.path.join(klasa1_dir, 'Julia Stachnik')
    os.mkdir(path5)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path5)
else:
    print ("Pomyślnie stworzono folder %s" % path5)

try:
    path6 = os.path.join(klasa1_dir, 'Jacek Szuba')
    os.mkdir(path6)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path6)
else:
    print ("Pomyślnie stworzono folder %s" % path6)

try:
    path7 = os.path.join(klasa1_dir, 'Jakub Wołowicz')
    os.mkdir(path7)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path7)
else:
    print ("Pomyślnie stworzono folder %s" % path7)


#klasa 2
klasa2_dir = '/klasy/2'

try:
    path8 = os.path.join(klasa2_dir, 'Robert Lewiński')
    os.mkdir(path8)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path8)
else:
    print ("Pomyślnie stworzono folder %s" % path8)
    
try:
    path9 = os.path.join(klasa2_dir, 'Wiktoria Mendyk')
    os.mkdir(path9)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path9)
else:
    print ("Pomyślnie stworzono folder %s" % path9)

try:
    path10 = os.path.join(klasa2_dir, 'Paweł Ptasznik')
    os.mkdir(path10)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path10)
else:
    print ("Pomyślnie stworzono folder %s" % path10)


#klasa 3
klasa3_dir = '/klasy/3'

try:
    path11 = os.path.join(klasa3_dir, 'Karolina Korneluk')
    os.mkdir(path11)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path11)
else:
    print ("Pomyślnie stworzono folder %s" % path11)

try:
    path12 = os.path.join(klasa3_dir, 'Wojciech Ostrowski')
    os.mkdir(path12)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path12)
else:
    print ("Pomyślnie stworzono folder %s" % path12)

try: 
    path13 = os.path.join(klasa3_dir, 'Joanna Żurek')
    os.mkdir(path13)
except OSError:
    print ("Stworzenie podfolderu %s nie udało się" % path13)
else:
    print ("Pomyślnie stworzono folder %s" % path13)

