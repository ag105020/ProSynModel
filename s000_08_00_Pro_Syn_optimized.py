'''
Created on Feb 12, 2019

@author: keiin
'''

from pylab import *
from FigSetting2 import *
from Solutions03 import *

rcParams['image.cmap'] = 'plasma'
rcParams.update({'axes.facecolor':'#bfbfbf'})
#======Preparing arrays=======
M = zeros(5); K = copy(M); m = zeros(2); S = zeros(2); X0 = zeros(3); N0 = zeros(3)

########################################################################################
# Parameterization
########################################################################################
NRF = 3 #Nutrietn Ratio Factor
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

#----- mortality (d-1)-----------------
m[0] = 0.7061766409625276 #(d-1) mPro
m[1] = 0.5174304397808549 #(d-1) mSyn

#--- Source term (umol L-1 d-1) -------
S[0] = 0.005 #(umol L-1 d-1) NO3 source
S[1] = 0.005*NRF  #(umol L-1 d-1) NH4 source

#--- Qn values (umol cell-1) ----------
QnProPg = 0.009177 #(pg N cell-1) from "Cell Volume.xlsx"
QnSynPg = 0.030932 #(pg N cell-1) from "Cell Volume.xlsx"
QnEukPg = 6.035480 #(pg N cell-1) from "Cell Volume.xlsx"

#....... Conversion.......
QnPro = QnProPg/14*1e-6  #(umol cell-1)
QnSyn = QnSynPg/14*1e-6  #(umol cell-1)
QnEuk = QnEukPg/14*1e-6  #(umol cell-1)

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Defining axis terms 
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#------ Setting K3 and K4 arrays -------
K1original = K[1]
K2original = K[2]
K3 = K[3]
K4 = K[4]

K1range = 10
K1resolution = 800
K2range = 10
K2resolution = 800

K1 = Karray(K1range,K1resolution,K3)
K2 = Karray(K2range,K2resolution,K4)
K2 = K2.reshape(size(K2), 1)

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Main computation
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

#=== The second solution From "11 Review of first half (06).nb" ===
NO3,NH4 = Nsolutions1(M,K,m,K1,K2)
NO3a,NH4a = Nsolutions2(M,K,m,K1,K2)

Xpro,Xsyn = Xsolutions(M,K,m,S,NO3,NH4,QnPro,QnSyn,K1,K2)
XproA,XsynA = Xsolutions(M,K,m,S,NO3a,NH4a,QnPro,QnSyn,K1,K2) #Only NO3a and NH4a are different

Ratio = RatioSolution(Xpro,Xsyn,XproA,XsynA,QnSyn,QnPro,NO3,NH4,NO3a,NH4a)

#--- Source term new (umol L-1 d-1) -------
S[0] = 0.01 #(umol L-1 d-1) NO3 source
S[1] = 0.005*NRF  #(umol L-1 d-1) NH4 source

Xpro,Xsyn = Xsolutions(M,K,m,S,NO3,NH4,QnPro,QnSyn,K1,K2)
XproA,XsynA = Xsolutions(M,K,m,S,NO3a,NH4a,QnPro,QnSyn,K1,K2) #Only NO3a and NH4a are different

Ratio2 = RatioSolution(Xpro,Xsyn,XproA,XsynA,QnSyn,QnPro,NO3,NH4,NO3a,NH4a)

#--- Source term new (umol L-1 d-1) -------
S[0] = 0.005 #(umol L-1 d-1) NO3 source
S[1] = 0.01*NRF  #(umol L-1 d-1) NH4 source

Xpro,Xsyn = Xsolutions(M,K,m,S,NO3,NH4,QnPro,QnSyn,K1,K2)
XproA,XsynA = Xsolutions(M,K,m,S,NO3a,NH4a,QnPro,QnSyn,K1,K2) #Only NO3a and NH4a are different

Ratio3 = RatioSolution(Xpro,Xsyn,XproA,XsynA,QnSyn,QnPro,NO3,NH4,NO3a,NH4a)

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Plotting
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
figure(1)
pcolormesh(K1/K3,K2/K4,1/Ratio)
plot(K1original/K3,K2original/K4,'^',color='cyan',markersize=10,markeredgewidth=2,\
     markeredgecolor='black')
Decoration01(K1range,K2range)

figure(2)
pcolormesh(K1/K3,K2/K4,1/Ratio2)
plot(K1original/K3,K2original/K4,'^',color='cyan',markersize=10,markeredgewidth=2,\
     markeredgecolor='black')
Decoration01(K1range,K2range)

figure(3)
pcolormesh(K1/K3,K2/K4,1/Ratio3)
plot(K1original/K3,K2original/K4,'^',color='cyan',markersize=10,markeredgewidth=2,\
     markeredgecolor='black')
Decoration01(K1range,K2range)

from Savetxt import *
savefolder = "02\\01 ProSyn\\01 MultiplePlots"
Savetxt(Ratio,savefolder,'Ratio')
Savetxt(K1/K3,savefolder,'x')
Savetxt(K2/K4,savefolder,'y')
Savetxt(Ratio2,savefolder,'Ratio2')
Savetxt(Ratio3,savefolder,'Ratio3')
Savetxt((K1original/K3,K2original/K4),savefolder,'xy0')

show()

