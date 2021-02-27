'''
Created on 07/12/2020
Using new data and focusing only on Pro and Syn
@author: Keisuke
From p000 02 03
'''

from pylab import *
from FigSetting2 import *
from Eco2 import *
from Tools10 import *
from Savefig3 import *

rcParams.update({'font.size': 15})
    
#======Preparing arrays=======
M = zeros(7); K = copy(M); m = zeros(3); S = zeros(2); X0 = zeros(2); N0 = zeros(3)

########################################################################################
# Parameterization
########################################################################################
#======Defining values common for all the cases=====
#----- Mu max (d-1)--------------------
M[1] = 1.9 #(d-1) MuMaxProNO3
M[2] = 2.7 #(d-1) MuMaxProNH4
M[3] = 2.3 #(d-1) MuMaxSynNO3
M[4] = 3.6  #(d-1) MuMaxSynNH4

#----- Ks (umol L-1)-------------------
K[1] = 0.06 #(umol L-1) KsProNO3
K[2] = 0.01 #(umol L-1) KsProNH4
K[3] = 0.06 #(umol L-1) KsSynNO3
K[4] = 0.04 #(umol L-1) KsSynNH4

#----- mortality (d-1)-----------------
m[0] = 0.85 #(d-1) mPro
m[1] = 0.7 #(d-1) mSyn

#=== Source term of XXX under XXX addition (or control) (umol L-1 d-1) ==========
#---NH4 adding case------
Sno3nh4 = -0.001
Snh4nh4 = -0.050

#---NO3 adding case------
Sno3no3 = -0.026
Snh4no3 = -0.004

#---Control case---------
Sno3cont= -0.0012
Snh4cont= -0.006

#=== Initial cell densities (cell L-1) ===========
conv = 1000 #There was an unit error (data was cell mL-1)
#-----NH4 adding case---------
X0proNH4 = 0.4e4*conv
X0synNH4 = 0.04e3*conv

#-----NO3 adding case---------
X0proNO3 = 0.36e4*conv
X0synNO3 = 0.048e3*conv

#-----Control case------------
X0proCont= 0.36e4*conv
X0synCont= 0.1e3*conv

#=== Initial N concentrations (umol L-1) =========
#---NH4 adding case--------
N0no3nh4 = 0.01
N0nh4nh4 = 0.10

#---NO3 adding case--------
N0no3no3 = 0.12
N0nh4no3 = 0.01

#---Control case-----------
N0no3cont= 0.01
N0nh4cont= 0.015

################################################
# Main calculation
################################################
#=====NH4 adding case ========
S,X0,N0 = Convert(S,X0,N0,Sno3nh4,Snh4nh4,X0proNH4,X0synNH4,N0no3nh4,N0nh4nh4)
Xpro,Xsyn,NO3,NH4 = Eco(M,K,m,S,X0,N0)
fig(1,0,6,Xpro,Xsyn,NO3,NH4)
#--Legend--
subplot(3,5,2)
errorbar([],[],[],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11,label='Data')
plot([],[],label='Model',color='#1D75B3')
legend(loc=1,edgecolor='k')

subplot(3,5,4)
errorbar([],[],[],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11,label='Data')
plot([],[],label='Model',color='#1D75B3')
legend(loc=1,edgecolor='k')

#=====NO3 adding case ========
S,X0,N0 = Convert(S,X0,N0,Sno3no3,Snh4no3,X0proNO3,X0synNO3,N0no3no3,N0nh4no3)
Xpro,Xsyn,NO3,NH4 = Eco(M,K,m,S,X0,N0)
fig(1,5,10,Xpro,Xsyn,NO3,NH4)

#=====Control case ===========
S,X0,N0 = Convert(S,X0,N0,Sno3cont,Snh4cont,X0proCont,X0synCont,N0no3cont,N0nh4cont)
Xpro,Xsyn,NO3,NH4 = Eco(M,K,m,S,X0,N0)
fig(1,10,2,Xpro,Xsyn,NO3,NH4)

Savefig3('02\\01 ProSyn\\05 Submition','Same Kno3',300)

show() 


