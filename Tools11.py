'''
Created on Feb 1, 2019

@author: Keisuke
'''

from pylab import *
from Eco0 import Time

Xlabel = 'time (d)'
tData = [nan,nan,0,1,2,3]
Cell3 = genfromtxt('..//Data//CellCountAve.csv',delimiter=',').T
CellSD = genfromtxt('..//Data//CellCountSD.csv',delimiter=',').T
Nut3 = genfromtxt('..//Data//NutAve.csv',delimiter=',').T
NutSD = genfromtxt('..//Data//NutSD.csv',delimiter=',').T
t,dt = Time()

def SubPl(loc,Title,y,Ylabel):
    subplot(2,2,loc)
    plot(t,y,'#1D75B3',zorder=10)
    xlabel(Xlabel)
    ylabel(Ylabel)
    xlim(right=3.3)
    xticks(arange(4))
    ylim(bottom=0)
    title(Title,y=1.02)

def fig(FigNum,SubPlNum,Ex,Xpro,Xsyn,NO3,NH4):
    figure(FigNum,figsize=(7,5.5)) 
    #For Pro#
    SubPl(SubPlNum + 1,'Pro',Xpro/1000,'X (cell mL$^{-1}$)')
    errorbar(tData,Cell3[Ex],CellSD[Ex],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
    ylim(0,60000)
    #For Syn#
    SubPl(SubPlNum + 2,'Syn',Xsyn/1000,'X (cell mL$^{-1}$)')
    errorbar(tData,Cell3[Ex+1],CellSD[Ex+1],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
    ylim(0,6000)
#     #For NH4#
#     SubPl(SubPlNum + 5,'NH$_4^+$',NH4*1e3,'NH$_{4}^{+}$ (nmol L$^{-1}$)')
#     errorbar(tData,Nut3[Ex],NutSD[Ex],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
#     ylim(0,150)
#     #For NO3#
#     SubPl(SubPlNum + 4,'NO$_3^-$',NO3*1e3,'NO$_{3}^{-}$ (nmol L$^{-1}$)')
#     errorbar(tData,Nut3[Ex+1],NutSD[Ex+1],fmt='o',color='#FF7F0E',markeredgecolor='k',elinewidth=1,ecolor='k',capthick=1,capsize=8,zorder=11)
#     ylim(0,150)
    
def Convert(S,X0,N0,Sno3,Snh4,X0pro,X0syn,N0no3,N0nh4):
    S[0] = Sno3
    S[1] = Snh4
    X0[0] = X0pro
    X0[1] = X0syn
    N0[0] = N0no3
    N0[1] = N0nh4
    return S,X0,N0