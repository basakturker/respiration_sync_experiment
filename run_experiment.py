# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:22:18 2018

@author: basak
"""
import pygame as pg
from psychopy import  core
import pandas as pd
import time
import os
import parallel

os.chdir("/home/fraimondo/Desktop/respi_eeg/Stim")

# open parallel port
parallel_port = parallel.Parallel()
parallel_port.setData(11)


list=pd.read_csv('nadine1_list_S1.csv')
stims=list['stims'].tolist()
timestim=list['time'].tolist()
triggers=list['trigger'].tolist()

pg.mixer.init()
pg.mixer.set_num_channels(7)
timer=core.Clock()
back = pg.mixer.Sound("nadine1.wav")
back.set_volume(0.5)

back.play()
timer.reset()
while True:
    parallel_port.setData(0)
    a=timer.getTime()
    a=("%.1f" % a)
    a=float(a)
    print(a)
    if a in timestim:
        ind=timestim.index(a)
        stim=stims[ind]
        s=pg.mixer.Sound(stim)
        s.play()
        parallel_port.setData(triggers[ind])
    if a==222.0:
        break
    time.sleep(.1)
parallel_port.setData(11)
parallel_port.setData(0)
