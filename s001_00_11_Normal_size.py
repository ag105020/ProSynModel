'''
Created on Mar 2, 2019

@author: keiin
'''

from pylab import *
from FigSetting2 import *
from Solutions01 import *
from Savefig3 import *

#======Preparing arrays=======
M = zeros(5); K = copy(M); m = zeros(2); S = zeros(2); X0 = zeros(3); N0 = zeros(3)

########################################################################################
# Parameterization
########################################################################################
#======Defining values common for all the cases=====
#----- Mu max (d-1)--------------------
M[1] = 1.9 #(d-1) MuMaxProNO3
M[2] = 2.7 #(d-1) MuMaxProNH4
M[3] = 2.3 #(d-1) MuMaxSynNO3
M[4] = 3.6 #(d-1) MuMaxSynNH4

#----- Ks (umol L-1)-------------------
K[1] = 0.10 #(umol L-1) KsProNO3
K[2] = 0.01 #(umol L-1) KsProNH4
K[3] = 0.02 #(umol L-1) KsSynNO3
K[4] = 0.04 #(umol L-1) KsSynNH4

#----- mortality (d-1)-----------------
m[0] = 0.85 #(d-1) mPro
m[1] = 0.7 #(d-1) mSyn

#---- Log10Array Function -------------
def Log10Array(Min,Max,LogStep):
    LogMax = log10(Max)
    LogMin = log10(Min)
    Log10array = arange(LogMin,LogMax+LogStep,LogStep)
    return 10**Log10array
    
#--- Source term (umol L-1 d-1) -------
Sratio = Log10Array(0.025,4,0.0001)

S1 = 0.005 #(umol L-1 d-1) NH4 source
S0 = S1*Sratio  #(umol L-1 d-1) NO3 source

#--- Qn values (umol cell-1) ----------
QnProPg = 0.009177 #(pg N cell-1) from "Cell Volume.xlsx"
QnSynPg = 0.030932 #(pg N cell-1) from "Cell Volume.xlsx"
QnEukPg = 6.035480 #(pg N cell-1) from "Cell Volume.xlsx"

#....... Conversion.......
QnPro = QnProPg/14*1e-6  #(umol cell-1)
QnSyn = QnSynPg/14*1e-6  #(umol cell-1)    

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Main computation
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
NO3,NH4 = Nsolutions1(M,K,m,K[3],K[4])
Xpro,Xsyn = Xsolutions2(M,K,m,S0,S1,NO3,NH4,QnPro,QnSyn)
Ratio = (Xpro*QnPro)/(Xsyn*QnSyn)
Ratio[Xpro<0] = nan #Making the invalid part nan
Ratio[Xsyn<0] = nan

#======== to find out the border ==========
for i in arange(size(Ratio))[:-1]:
   if isnan(Ratio[i])==1 and Ratio[i+1]>0:
       LowerBorder = Sratio[i]
   if Ratio[i]>0 and isnan(Ratio[i+1])==1:
       UpperBorder = Sratio[i+1]

#========== Creating a background =========
Ymin = 0.0001; Ymax = 10000
Y = Log10Array(Ymin,Ymax,0.1)
Y = Y.reshape(size(Y), 1)
Background = zeros((size(Y),size(Sratio)))*nan #Set nan for everywhere
Background[:,Sratio<=LowerBorder] = 0 #Set 0 for the Pro only part
Background[:,Sratio>=UpperBorder] = 1 #Set 1 for the Syn only part

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Plotting
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#========================
# Setting manual color
#========================
cmap = mpl.colors.ListedColormap(['#E2EFDA','#FCE4D6'])

figure(1)#,figsize=(8,5))
pcolormesh(Sratio,Y,Background,cmap=cmap)
clim(0,1)
plot(Sratio,Ratio,'k')
xscale('log')
yscale('log')
ylim(Ymin,Ymax)
title(' ',y=1.02)
xlabel('S$_{NO3}$/S$_{NH4}$')
ylabel('N$_{Pro}$/N$_{Syn}$')
Savefig3('02\\01 ProSyn\\02 ForPaper','Sratio',300)

show()
