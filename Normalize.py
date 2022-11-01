import pandas as pd
import sqlite3
import numpy as np
import itertools
from sklearn import preprocessing


con = sqlite3.connect("C:/Users/MikhailAnd/Desktop/Result/DATA.db")


#F_frag
F_frag = pd.read_sql('SELECT F_frag FROM Positive', con)
_F_frag1 = np.array(F_frag)
_F_frag = list(itertools.chain(*_F_frag1))
n_F_frag1 = preprocessing.normalize([_F_frag])
n_F_frag = list(itertools.chain(*n_F_frag1))


#STETEOF_1_frag
STETEOF_1_frag = pd.read_sql('SELECT STETEOF_1_frag FROM Positive', con)
_STETEOF_1_frag1 = np.array(STETEOF_1_frag)
_STETEOF_1_frag = list(itertools.chain(*_STETEOF_1_frag1))
n_STETEOF_1_frag1 = preprocessing.normalize([_STETEOF_1_frag])
n_STETEOF_1_frag = list(itertools.chain(*n_STETEOF_1_frag1))

#STETEOF_2_frag
STETEOF_2_frag = pd.read_sql('SELECT STETEOF_2_frag FROM Positive', con)
_STETEOF_2_frag1 = np.array(STETEOF_2_frag)
_STETEOF_2_frag = list(itertools.chain(*_STETEOF_2_frag1))
n_STETEOF_2_frag1 = preprocessing.normalize([_STETEOF_2_frag])
n_STETEOF_2_frag = list(itertools.chain(*n_STETEOF_2_frag1))

#STETEO_frag
STETEO_frag = pd.read_sql('SELECT STETEO_frag FROM Positive', con)
_STETEO_frag1 = np.array(STETEO_frag)
_STETEO_frag = list(itertools.chain(*_STETEO_frag1))
n_STETEO_frag1 = preprocessing.normalize([_STETEO_frag])
n_STETEO_frag = list(itertools.chain(*n_STETEO_frag1))

#STEZCRTEO_1_frag
STEZCRTEO_1_frag = pd.read_sql('SELECT STEZCRTEO_1_frag FROM Positive', con)
_STEZCRTEO_1_frag1 = np.array(STEZCRTEO_1_frag)
_STEZCRTEO_1_frag = list(itertools.chain(*_STEZCRTEO_1_frag1))
n_STEZCRTEO_1_frag1 = preprocessing.normalize([_STEZCRTEO_1_frag])
n_STEZCRTEO_1_frag = list(itertools.chain(*n_STEZCRTEO_1_frag1))

#STEZCRTEO_2_frag
STEZCRTEO_2_frag = pd.read_sql('SELECT STEZCRTEO_2_frag FROM Positive', con)
_STEZCRTEO_2_frag1 = np.array(STEZCRTEO_2_frag)
_STEZCRTEO_2_frag = list(itertools.chain(*_STEZCRTEO_2_frag1))
n_STEZCRTEO_2_frag1 = preprocessing.normalize([_STEZCRTEO_2_frag])
n_STEZCRTEO_2_frag = list(itertools.chain(*n_STEZCRTEO_2_frag1))


#STE_frag
STE_frag = pd.read_sql('SELECT STE_frag FROM Positive', con)
_STE_frag1 = np.array(STE_frag)
_STE_frag = list(itertools.chain(*_STE_frag1))
n_STE_frag1 = preprocessing.normalize([_STE_frag])
n_STE_frag = list(itertools.chain(*n_STE_frag1))


#ZCRTEO_frag
ZCRTEO_frag = pd.read_sql('SELECT ZCRTEO_frag FROM Positive', con)
_ZCRTEO_frag1 = np.array(ZCRTEO_frag)
_ZCRTEO_frag = list(itertools.chain(*_ZCRTEO_frag1))
n_ZCRTEO_frag1 = preprocessing.normalize([_ZCRTEO_frag])
n_ZCRTEO_frag = list(itertools.chain(*n_ZCRTEO_frag1))

#ZCR_frag
ZCR_frag = pd.read_sql('SELECT ZCR_frag FROM Positive', con)
_ZCR_frag1 = np.array(ZCR_frag)
_ZCR_frag = list(itertools.chain(*_ZCR_frag1))
n_ZCR_frag1 = preprocessing.normalize([_ZCR_frag])
n_ZCR_frag = list(itertools.chain(*n_ZCR_frag1))

with sqlite3.connect(r'C:/Users/MikhailAnd/Desktop/Result/DATAn.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Positive(
    F_frag REAL, 
    STETEOF_1_frag REAL, 
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
    STEZCRTEO_2_frag,STE_frag,ZCRTEO_frag,ZCR_frag) VALUES(?,?,?,?,?,?,?,?,?)''',(n_F_frag[i3], n_STETEOF_1_frag[i3], n_STETEOF_2_frag[i3], n_STETEO_frag[i3], n_STEZCRTEO_1_frag[i3], n_STEZCRTEO_2_frag[i3], n_STE_frag[i3], n_ZCRTEO_frag[i3], n_ZCR_frag[i3]))
con.commit()