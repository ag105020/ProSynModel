'''
Created on 07/12/2020
Using new data and focusing only on Pro and Syn
@author: Keisuke
From p000 02 03
'''

from pylab import *
from FigSetting2 import *
from Savefig3 import *

#rcParams.update({'font.size': 15})

HOT = genfromtxt("..\\Data\\HOT Pro Syn NO3.csv", delimiter=',').T

Pro = HOT[0]
Syn = HOT[1]
NO3 = HOT[2]

figure(1)
plot(NO3, Pro/Syn,'ro',markersize=15,markeredgewidth=1.5,markeredgecolor='k')
xscale('log')
yscale('log')
xlabel('NO$_{3}^{-}$ ($\mu$mol kg$^{-1}$)')
ylabel('Pro/Syn')
xlim(0.01,10)
ylim(bottom=10,top=1000)
title("HOT data",y=1.02)

Savefig3('02\\01 ProSyn\\02 ForPaper','HOT',300)

show() 


