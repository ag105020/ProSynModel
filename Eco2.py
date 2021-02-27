'''
Created on Jan 29, 2019
Here we define Time in function so that it can be used in other modules (files)
We also define Eco, the main function for computing ecosystems based on N
@author: Keisuke
'''

from pylab import *

def Time():
    tMax = 4 #(d)
    dt= tMax/1000
    tMin = 0
    t = arange(tMin,tMax+dt,dt)
    return t,dt

def Eco(M,K,m,S,X0,N0):

    Aboga = 6.22*10**23 #(count/mol)
    
    t,dt = Time()

    U = arange(size(t))
    
    o = zeros(size(t))
    
    QnProPg = 0.119557032 #(fmol N cell-1) from "15_ProSyn_av_QN.xlsx" New value used (see the original excel file)!
    QnSynPg = 0.288118551 #(fmol N cell-1) from "15_ProSyn_av_QN.xlsx"
    
    QnPro = QnProPg*1e-9  #(umol cell-1)
    QnSyn = QnSynPg*1e-9  #(umol cell-1)
    
    Xpro = copy(o)   #(cell L-1)
    Xsyn = copy(o)   #(cell L-1)
    NO3 = copy(o)    #(umol L-1)
    NH4 = copy(o)    #(umol L-1)
    DON = copy(o)    #(umol L-1)
    LostN = copy(o)  #(umol L-1)
    
    M1 = M[1] #(d-1) MuMaxProNO3
    M2 = M[2] #(d-1) MuMaxProNH4
    M3 = M[3] #(d-1) MuMaxSynNO3
    M4 = M[4] #(d-1) MuMaxSynNH4
    
    K1 = K[1] #(umol L-1) KsProNO3
    K2 = K[2] #(umol L-1) KsProNH4
    K3 = K[3] #(umol L-1) KsSynNO3
    K4 = K[4] #(umol L-1) KsSynNH4
    
    mPro = m[0] #(d-1)
    mSyn = m[1] #(d-1)
    mEuk = m[2] #(d-1)
    
    Sno3 = S[0] #(umol L-1 d-1) NO3 source
    Snh4 = S[1] #(umol L-1 d-1) NH4 source
    
    Xpro[0] = X0[0]
    Xsyn[0] = X0[1]
    NO3[0] = N0[0]
    NH4[0] = N0[1]   #(umol L-1) Original 9 nmol + added 100 nmol
    
    for i in U[:-1]:
        dXproDt = (M1*NO3[i]/(NO3[i]+K1) + M2*NH4[i]/(NH4[i]+K2))*Xpro[i] - mPro*Xpro[i]
        dXsynDt = (M3*NO3[i]/(NO3[i]+K3) + M4*NH4[i]/(NH4[i]+K4))*Xsyn[i] - mSyn*Xsyn[i]
        dNO3dt = - M1*QnPro*NO3[i]/(NO3[i]+K1)*Xpro[i] - M3*QnSyn*NO3[i]/(NO3[i]+K3)*Xsyn[i] + Sno3
        dNH4dt = - M2*QnPro*NH4[i]/(NH4[i]+K2)*Xpro[i] - M4*QnSyn*NH4[i]/(NH4[i]+K4)*Xsyn[i] + Snh4
        dDONdt = mPro*Xpro[i]*QnPro + mSyn*Xsyn[i]*QnSyn
        
        if NH4[i] <= 0 and dNH4dt < 0:
            dNH4dt = 0
            
        if NO3[i] <= 0 and dNO3dt < 0:
            dNO3dt = 0
        
        Xpro[i+1] = Xpro[i] + dXproDt*dt
        Xsyn[i+1] = Xsyn[i] + dXsynDt*dt
        NO3[i+1] = NO3[i] + dNO3dt*dt
        NH4[i+1] = NH4[i] + dNH4dt*dt
        DON[i+1] = DON[i] + dDONdt*dt
        
        if NH4[i+1] < 0:
            NH4[i+1] = 0
        if NO3[i+1] < 0:
            NO3[i+1] = 0
    
    return Xpro,Xsyn,NO3,NH4


