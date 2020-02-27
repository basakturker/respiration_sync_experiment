import random
import numpy
import pandas as pd

all=range(1,21)
for al in all:

    ##TARGETS
    #Non target sounds
    stim=["3_13_400.wav","13_3_400.wav","3_13_3.wav","13_3_13.wav","3_8.wav","8_3.wav"]
    stims=[]
    for i in range(37):
            stims=stims+stim
    random.shuffle(stims)

    #TARGET PLACES
    target_place=[]
    while True:
        count=0
        cc=0
        c=0
        target_place=[]
        r=numpy.random.uniform(low=10, high=225, size=12)
        r.sort()
        for i in r:
            target_place.append(int(i))
        for k in range(11):
            if target_place[k]+1!=target_place[k+1]:
                count=count+1
            if target_place[k]+2!=target_place[k+1]:
                cc=cc+1
            if target_place[k]+3!=target_place[k+1]:
                c=c+1
        if len(target_place)==len(list(numpy.unique(target_place))) and count==11 and cc==11 and c==11:
            break


    #Insert targets
    tp=target_place[:]
    for i in target_place:
        stims.insert(i,'target.wav')

    #Trigger
    trigger=[]
    for i in range(len(stims)):
        if i in tp:
            trigger.append(1)
        else:
            trigger.append(2)

    #TIMING
    intervals=[0.8,0.9,1.0,1.1]
    tt=[2.2]
    time=[]
    for i in range(233):
        a=numpy.random.choice(intervals)
        tt.append(tt[-1]+a)
    for i in tt:
        i=("%.1f" % i)
        i=float(i)
        time.append(i)

    stimTime=pd.DataFrame({'stims': stims, 'time': time, 'trigger': trigger})
    stimTime.to_csv("/home/fraimondo/Desktop/respi_eeg/Stim/nadine1_list_S%s.csv" %al)
