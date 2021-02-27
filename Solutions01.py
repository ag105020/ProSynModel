'''
Created on Feb 24, 2019

@author: keiin
'''

from pylab import *


def Nsolutions1(M,K,m,K3,K4):
    M1 = M[1]
    M2 = M[2]
    M3 = M[3]
    M4 = M[4]
    K1 = K[1]
    K2 = K[2]
    mPro = m[0]
    mSyn = m[1]
    
    NO3 = (-K1*K4*M2*M3 + K2*K3*M1*M4 - K1*K2*M3*mPro + K1*K4*M3*mPro - 
       K1*K2*M4*mPro - K2*K3*M4*mPro - K2*K3*M1*mSyn + K3*K4*M1*mSyn + 
       K1*K4*M2*mSyn + K3*K4*M2*mSyn + K1*K2*mPro*mSyn + K2*K3*mPro*mSyn -
        K1*K4*mPro*mSyn - 
       K3*K4*mPro*mSyn + sqrt(4*K1*K3*(-K4*(M1 + M2 - mPro)*(M3 - 
                mSyn) + 
             K2*(M1 - mPro)*(M3 + M4 - mSyn))*(K2*mPro*(M4 - mSyn) + 
             K4*(-M2 + mPro)*mSyn) + (K1*(K4*(M2 - mPro)*(M3 - mSyn) + 
               K2*mPro*(M3 + M4 - mSyn)) - 
            K3*(K2*(M1 - mPro)*(M4 - mSyn) + 
               K4*(M1 + M2 - mPro)*mSyn))**2))/(2*K4*(M1 + M2 - mPro)*(M3 -
           mSyn) - 2*K2*(M1 - mPro)*(M3 + M4 - mSyn))
    
    NH4 = (-K1*K4*M2*M3 + K2*K3*M1*M4 + K1*K2*M3*mPro + K1*K4*M3*mPro + 
       K1*K2*M4*mPro - K2*K3*M4*mPro - K2*K3*M1*mSyn - K3*K4*M1*mSyn + 
       K1*K4*M2*mSyn - K3*K4*M2*mSyn - K1*K2*mPro*mSyn + K2*K3*mPro*mSyn -
        K1*K4*mPro*mSyn + 
       K3*K4*mPro*mSyn + sqrt(4*K1*K3*(-K4*(M1 + M2 - mPro)*(M3 - 
                mSyn) + 
             K2*(M1 - mPro)*(M3 + M4 - mSyn))*(K2*mPro*(M4 - mSyn) + 
             K4*(-M2 + mPro)*mSyn) + (K1*(K4*(M2 - mPro)*(M3 - mSyn) + 
               K2*mPro*(M3 + M4 - mSyn)) - 
            K3*(K2*(M1 - mPro)*(M4 - mSyn) + 
               K4*(M1 + M2 - mPro)*mSyn))**2))/(-2*K3*(M1 + M2 - 
          mPro)*(M4 - mSyn) + 2*K1*(M2 - mPro)*(M3 + M4 - mSyn))
    
    return NO3,NH4
    
def Nsolutions2(M,K,m,K3,K4):    
    M1 = M[1]
    M2 = M[2]
    M3 = M[3]
    M4 = M[4]
    K1 = K[1]
    K2 = K[2]
    mPro = m[0]
    mSyn = m[1]

    NO3a = (K1*K4*M2*M3 - K2*K3*M1*M4 + K1*K2*M3*mPro - K1*K4*M3*mPro + \
       K1*K2*M4*mPro + K2*K3*M4*mPro + K2*K3*M1*mSyn - K3*K4*M1*mSyn - \
       K1*K4*M2*mSyn - K3*K4*M2*mSyn - K1*K2*mPro*mSyn - K2*K3*mPro*mSyn + \
        K1*K4*mPro*mSyn + K3*K4*mPro*mSyn + \
         sqrt(4*K1*K3*(-K4*(M1 + M2 - mPro)*(M3 - mSyn) + \
             K2*(M1 - mPro)*(M3 + M4 - mSyn))*(K2*mPro*(M4 - mSyn) + \
             K4*(-M2 + mPro)*mSyn) + (K1*(K4*(M2 - mPro)*(M3 - mSyn) + \
               K2*mPro*(M3 + M4 - mSyn)) - \
            K3*(K2*(M1 - mPro)*(M4 - mSyn) + \
               K4*(M1 + M2 - mPro)*mSyn))**2))/(-2*K4*(M1 + M2 - \
          mPro)*(M3 - mSyn) + 2*K2*(M1 - mPro)*(M3 + M4 - mSyn))

    NH4a = (K1*K4*M2*M3 - K2*K3*M1*M4 - K1*K2*M3*mPro - K1*K4*M3*mPro - \
       K1*K2*M4*mPro + K2*K3*M4*mPro + K2*K3*M1*mSyn + K3*K4*M1*mSyn - \
       K1*K4*M2*mSyn + K3*K4*M2*mSyn + K1*K2*mPro*mSyn - K2*K3*mPro*mSyn +\
        K1*K4*mPro*mSyn - \
       K3*K4*mPro*mSyn + sqrt(4*K1*K3*(-K4*(M1 + M2 - mPro)*(M3 - \
                mSyn) + \
             K2*(M1 - mPro)*(M3 + M4 - mSyn))*(K2*mPro*(M4 - mSyn) + \
             K4*(-M2 + mPro)*mSyn) + (K1*(K4*(M2 - mPro)*(M3 - mSyn) + \
               K2*mPro*(M3 + M4 - mSyn)) - \
            K3*(K2*(M1 - mPro)*(M4 - mSyn) + \
               K4*(M1 + M2 - mPro)*mSyn))**2))/(2*K3*(M1 + M2 - mPro)*(M4 - \
           mSyn) - 2*K1*(M2 - mPro)*(M3 + M4 - mSyn))
    
    return NO3a,NH4a

def Xsolutions(M,K,m,S,NO3,NH4,QnPro,QnSyn,K3,K4):
    M1 = M[1]
    M2 = M[2]
    M3 = M[3]
    M4 = M[4]
    K1 = K[1]
    K2 = K[2]
    mPro = m[0]
    mSyn = m[1]
    Sno3 = S[0]
    Snh4 = S[1]
    
    Xpro = -((-((M3*NO3*Snh4)/(K3 + NO3)) + (M4*NH4*Sno3)/(
      K4 + NH4))/(-((
       M1*M4*NH4*NO3*QnPro)/((K4 + NH4)*(K1 + NO3))) + (
      M2*M3*NH4*NO3*QnPro)/((K2 + NH4)*(K3 + NO3))))
    
    Xsyn = -(((K4 + NH4)*(K3 + NO3)*(K2*M1*NO3*Snh4 + M1*NH4*NO3*Snh4 - 
           M2*NH4*(K1 + NO3)*Sno3))/(NH4*NO3*(-K3*M1*M4*NH4 + 
           K1*M2*M3*(K4 + NH4) + K4*M2*M3*NO3 + M2*M3*NH4*NO3 - 
           M1*M4*NH4*NO3 - K2*M1*M4*(K3 + NO3))*QnSyn))
    
    return Xpro,Xsyn

def Xsolutions2(M,K,m,S0,S1,NO3,NH4,QnPro,QnSyn):
    M1 = M[1]
    M2 = M[2]
    M3 = M[3]
    M4 = M[4]
    K1 = K[1]
    K2 = K[2]
    K3 = K[3]
    K4 = K[4]
    mPro = m[0]
    mSyn = m[1]
    Sno3 = S0
    Snh4 = S1
    
    Xpro = -((-((M3*NO3*Snh4)/(K3 + NO3)) + (M4*NH4*Sno3)/(
      K4 + NH4))/(-((
       M1*M4*NH4*NO3*QnPro)/((K4 + NH4)*(K1 + NO3))) + (
      M2*M3*NH4*NO3*QnPro)/((K2 + NH4)*(K3 + NO3))))
    
    Xsyn = -(((K4 + NH4)*(K3 + NO3)*(K2*M1*NO3*Snh4 + M1*NH4*NO3*Snh4 - 
           M2*NH4*(K1 + NO3)*Sno3))/(NH4*NO3*(-K3*M1*M4*NH4 + 
           K1*M2*M3*(K4 + NH4) + K4*M2*M3*NO3 + M2*M3*NH4*NO3 - 
           M1*M4*NH4*NO3 - K2*M1*M4*(K3 + NO3))*QnSyn))
    
    return Xpro,Xsyn

def RatioSolution(Xpro,Xsyn,XproA,XsynA,QnSyn,QnPro,NO3,NH4,NO3a,NH4a):
    Ratio = (Xsyn*QnSyn)/(Xpro*QnPro)
    Ratio[Xpro<0] = 0
    Ratio[Xsyn<0] = 0
    Ratio[NO3<0] = 0
    Ratio[NH4<0] = 0
    
    RatioA = (XsynA*QnSyn)/(XproA*QnPro)
    RatioA[XproA<0] = 0
    RatioA[XsynA<0] = 0
    RatioA[NO3a<0] = 0
    RatioA[NH4a<0] = 0
    
    Ratio = Ratio + RatioA
    Ratio[isnan(Ratio)] = 0
    Ratio = ma.masked_where(Ratio==0,Ratio)
    
    return Ratio

def Karray(Krange,Kresolution,K):
    Kmax = K*Krange
    Kstep = Kmax/Kresolution
    Kmin = Kstep
    return arange(Kmin, Kmax + Kstep, Kstep)

def Decoration01():
    xlim(0,10)
    ylim(0,10)
    colorbar()
    clim(0,5)
    title('Xsyn/Xpro')
    xlabel('K$_{Syn}$NO$_3^-$/K$_{Pro}$NO$_3^-$')
    ylabel('K$_{Sro}$NH$_4^+$/K$_{Pro}$NH$_4^+$')
    gca().set_facecolor('#E7E6E6')
    
