'''
Created on 07/12/2020
Using new data and focusing only on Pro and Syn
@author: Keisuke
From p000 02 03
'''

from pylab import *
from FigSetting2 import *
from Eco2 import *
from Tools11 import *
from Savefig3 import *

rcParams.update({'font.size': 15})
    
#======Preparing arrays=======
M = zeros(7); K = copy(M)

########################################################################################
# Parameterization
########################################################################################
#======Defining values common for all the cases=====
#----- Mu max (d-1)--------------------
M[1] = 1.1434816951386526 #(d-1) MuMaxProNO3
M[2] = 2.4193379503515127 #(d-1) MuMaxProNH4
M[3] = 2.1666245853028836 #(d-1) MuMaxSynNO3
M[4] = 3.980711265660864  #(d-1) MuMaxSynNH4

#----- Ks (umol L-1)-------------------
K[1] = 0.035514825129346485 #(umol L-1) KsProNO3
K[2] = 0.011781732396251077 #(umol L-1) KsProNH4
K[3] = 0.019948479780040967 #(umol L-1) KsSynNO3
K[4] = 0.06918257358686321 #(umol L-1) KsSynNH4

N = arange(0.1,100+1e-10,0.1) #(nmol L-1) nutrient concentration (note: this one is in nano molar)

V1 = M[1]*N/(N+K[1]*1000)
V2 = M[2]*N/(N+K[2]*1000)
V3 = M[3]*N/(N+K[3]*1000)
V4 = M[4]*N/(N+K[4]*1000)

figure(1, figsize=(4.8,3.6))
plot(N,V1,zorder=100, color='#1F77B4')
plot(N,V4,zorder=10, color='#FF7F0E')
plot(N,V2, color='#2CA02C')
plot(N,V3, color='#D62728')

xlabel('[N] (nmol L$^{-1}$)')
ylabel('V$_{N}$ (d$^{-1}$)')
xlim(0,100)
ylim(0,2.5)

Savefig3('02\\01 ProSyn\\05 Submition','Nutrient',450)

figure(2, figsize=(4.8,3.6))
plot([],[], color='#2CA02C',label='V$_{NH4}^{Pro}$')
plot([],[],zorder=100, color='#1F77B4',label='V$_{NO3}^{Pro}$')
plot([],[],zorder=10, color='#FF7F0E',label='V$_{NH4}^{Syn}$')
plot([],[], color='#D62728',label='V$_{NO3}^{Syn}$')

legend(edgecolor='k').get_frame().set_boxstyle('Round', pad=0.2, rounding_size=0.00001)
Savefig3('02\\01 ProSyn\\05 Submition','Nutrient_legend',450)

show() 


