'''
Created on 02/14/2023
Plotting climate model comparison 
provided by Curtis Deutsch
'''

from pylab import *
from FigSetting3 import *
from Savefig3 import *

c = genfromtxt("..\\Data\\CMIP5_dNutr_Lat30_ProSyn.csv", delimiter=',').T

y = c[0] # year
GFDL = c[1]
IPSL = c[2]
HadGEM = c[3]
CESM = c[4]
MPI = c[5]

figure(1)
plot(y,y*0,':',color='k',zorder=100)
plot(y, GFDL,label='GFDL',color="#F01424")
plot(y, IPSL,label='IPSL',color="#5AFF00")
plot(y, HadGEM,label='HadGEM',color="#3800FA")
plot(y, CESM,label='CESM',color="#FAF900")
plot(y, MPI,label='MPI',color="#66FFF1")
legend(edgecolor='k',fontsize=20).get_frame().set_linewidth(1)

xlabel('Year')
ylabel('$\u0394$NO$_{3}^{-}$ (%) 0-50m')
xlim(1860,2100)
ylim(top=50,bottom=-100)
yticks(arange(-100,51,50))

Savefig3('02\\01 ProSyn\\02 ForPaper','Climate',450)

show()





