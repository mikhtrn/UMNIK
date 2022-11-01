import numpy as np
import scipy.io as sc
import os
import itertools
import sqlite3

path = 'C:/Users/MikhailAnd/Desktop/Новая папка/Сигналы/Положительные сигналы'
for dirs, folder, files in os.walk(path):
    print('Выбранный каталог: ', dirs)
    print('Вложенные папки: ', folder)
    break

_F_frag = np.array([])
_STETEOF_1_frag = np.array([])
_STETEOF_2_frag = np.array([])
_STETEO_frag = np.array([])
_STEZCRTEO_1_frag = np.array([])
_STEZCRTEO_2_frag = np.array([])
_STE_frag = np.array([])
_ZCRTEO_frag = np.array([])
_ZCR_frag = np.array([])

for i in folder:
    pathh = 'C:/Users/MikhailAnd/Desktop/Новая папка/Сигналы/Положительные сигналы/' + i + '/results/result_pref_name_settinng_AI_1_ai.mat'
    mat = sc.loadmat(pathh)
    if os.path.exists('C:/Users/MikhailAnd/Desktop/Новая папка/Сигналы/Положительные сигналы/' + i + '/results/result_pref_name_settinng_AI_1_ai.mat'):

        a = mat['F_frag_s']
        aa = list(itertools.chain(*a))
        _F_frag1 = np.array(aa)
        _F_frag = np.append(_F_frag, _F_frag1)

        b = mat['STETEOF_1_frag_s']
        bb = list(itertools.chain(*b))
        _STETEOF_1_frag1 = np.array(bb)
        _STETEOF_1_frag = np.append(_STETEOF_1_frag, _STETEOF_1_frag1)

        c = mat['STETEOF_2_frag_s']
        cc = list(itertools.chain(*c))
        _STETEOF_2_frag1 = np.array(cc)
        _STETEOF_2_frag = np.append(_STETEOF_2_frag, _STETEOF_2_frag1)

        d = mat['STETEO_frag_s']
        dd = list(itertools.chain(*d))
        _STETEO_frag1 = np.array(dd)
        _STETEO_frag = np.append(_STETEO_frag, _STETEO_frag1)

        e = mat['STEZCRTEO_1_frag_s']
        ee = list(itertools.chain(*e))
        _STEZCRTEO_1_frag1 = np.array(ee)
        _STEZCRTEO_1_frag = np.append(_STEZCRTEO_1_frag, _STEZCRTEO_1_frag1)

        f = mat['STEZCRTEO_2_frag_s']
        ff = list(itertools.chain(*f))
        _STEZCRTEO_2_frag1 = np.array(ff)
        _STEZCRTEO_2_frag = np.append(_STEZCRTEO_2_frag, _STEZCRTEO_2_frag1)

        g = mat['STE_frag_s']
        gg = list(itertools.chain(*g))
        _STE_frag1 = np.array(ff)
        _STE_frag = np.append(_STE_frag, _STE_frag1)

        k = mat['ZCRTEO_frag_s']
        kk = list(itertools.chain(*k))
        _ZCRTEO_frag1 = np.array(kk)
        _ZCRTEO_frag = np.append(_ZCRTEO_frag, _ZCRTEO_frag1)

        l = mat['ZCR_frag_s']
        ll = list(itertools.chain(*l))
        _ZCR_frag1 = np.array(ll)
        _ZCR_frag = np.append(_ZCR_frag, _ZCR_frag1)
    else:
        continue


#БД
with sqlite3.connect(r'C:/Users/MikhailAnd/Desktop/Result/DAT.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Positive(
    F_frag REAL, 
    STETEOF_1_frag DOUBLE, 
    STETEOF_2_frag REAL, 
    STETEO_frag REAL, 
    STEZCRTEO_1_frag REAL,
    STEZCRTEO_2_frag REAL,
    STE_frag REAL,
    ZCRTEO_frag REAL,
    ZCR_frag REAL )''')

for i3 in range(0,len(_F_frag)):
    c = con.cursor()
    c.execute('''INSERT INTO Positive(F_frag, STETEOF_1_frag , STETEOF_2_frag, STETEO_frag, STEZCRTEO_1_frag,
    STEZCRTEO_2_frag,STE_frag,ZCRTEO_frag,ZCR_frag) VALUES(?,?,?,?,?,?,?,?,?)''',(_F_frag[i3], _STETEOF_1_frag[i3], _STETEOF_2_frag[i3], _STETEO_frag[i3], _STEZCRTEO_1_frag[i3],_STEZCRTEO_2_frag[i3],_STE_frag[i3],_ZCRTEO_frag[i3],_ZCR_frag[i3]))
con.commit()
