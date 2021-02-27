'''
Created on Feb 28, 2019
Here reading files and create border on the contor plot.
@author: keiin
'''

import matplotlib
from pylab import *
from FigSetting2 import *
from Savefig3 import *

rcParams['image.cmap'] = 'plasma'
rcParams.update({'axes.facecolor':'#757171'})

#OOOOOOOOOOOOOOOOO
# Reading files
#OOOOOOOOOOOOOOOOO
Loc = "C:\\Users\\Keiin\\OneDrive\\Desktop\\figures\\02\\01 ProSyn\\01 MultiplePlots\\"
Ratio1 = genfromtxt(Loc + "Ratio.csv", delimiter=',')
Ratio2 = genfromtxt(Loc + "Ratio2.csv", delimiter=',')
Ratio3 = genfromtxt(Loc + "Ratio3.csv", delimiter=',')
x = genfromtxt(Loc + "x.csv", delimiter=',') 
y = genfromtxt(Loc + "y.csv", delimiter=',')
xy0 = genfromtxt(Loc + "xy0.csv", delimiter=',')

#OOOOOOOOOOOOOOOOOOOOOO
# Border creation
#OOOOOOOOOOOOOOOOOOOOOO
borderX = arange(size(x))
borderY = arange(size(y))

BorderLeft = zeros(size(y))
BorderRight = zeros(size(y))

for j in borderY:
    for i in borderX[1:]:
        if Ratio1[j,i-1]==0 and Ratio1[j,i]>0:
            BorderLeft[j] = x[i-1]
        if Ratio1[j,i-1]>0 and Ratio1[j,i]==0:
            BorderRight[j] = x[i] 

BorderRight[BorderRight==max(BorderRight)] = max(x)
BorderLeft[BorderLeft==0] = nan
BorderRight[BorderRight==0] = nan

#OOOOOOOOOOOOOOOOOOOOOO
# Marking ratios
#OOOOOOOOOOOOOOOOOOOOOO
Ratio1 = ma.masked_where(Ratio1==0,Ratio1)
Ratio2 = ma.masked_where(Ratio2==0,Ratio2)
Ratio3 = ma.masked_where(Ratio3==0,Ratio3)

#OOOOOOOOOOOOOOOOOOOOOO
# Plotting
#OOOOOOOOOOOOOOOOOOOOOO
def LOG():
    xscale('log')
    yscale('log')

def FigDecorationAndSave(name):
    colorbar()
    clim(0.1,10)
    plot(BorderLeft,y,'--',color='w')
    plot(BorderRight,y,'--',color='w')
    title('N$_{Pro}$/N$_{Syn}$', y=1.02)
    xlabel('K$_{NO3}^{Pro}$/K$_{NO3}^{Syn}$')
    ylabel('K$_{NH4}^{Pro}$/K$_{NH4}^{Syn}$')
    xlim(0.1,10)
    ylim(0.1,10)
    LOG()
    Savefig3('02\\01 ProSyn\\02 ForPaper',name,300)

ms = 20
mew = 2.5

figure(1)
pcolormesh(x,y,1/Ratio1,norm=matplotlib.colors.LogNorm())
plot(xy0[0],xy0[1],'^',color='cyan',markersize=ms,markeredgewidth=mew,\
     markeredgecolor='black')
FigDecorationAndSave('Default')

figure(2)
pcolormesh(x,y,1/Ratio2,norm=matplotlib.colors.LogNorm())
plot(xy0[0],xy0[1],'^',color='cyan',markersize=ms,markeredgewidth=mew,\
     markeredgecolor='black')
FigDecorationAndSave('x2NO3')

figure(3)
pcolormesh(x,y,1/Ratio3,norm=matplotlib.colors.LogNorm())
plot(xy0[0],xy0[1],'^',color='cyan',markersize=ms,markeredgewidth=mew,\
     markeredgecolor='black')
FigDecorationAndSave('x2NH4')

figure(4)
Ratio11 = zeros(shape(Ratio1))
Ratio11[Ratio1>0] = 1
Ratio11 = ma.masked_where(Ratio11==0,Ratio11)
pcolormesh(x,y,Ratio11,cmap='viridis')
clim(0,1)
plot(BorderLeft,y,'--',color='k')
plot(BorderRight,y,'--',color='k')
xlabel('K$_{NO3}^{Pro}$/K$_{NO3}^{Syn}$')
ylabel('K$_{NH4}^{Pro}$/K$_{NH4}^{Syn}$')
gca().set_facecolor('#E7E6E6')
LOG()
xlim(0.1,10)
ylim(0.1,10)
Savefig3('02\\01 ProSyn\\02 ForPaper','Schematic',300)

show()

 