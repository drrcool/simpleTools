from pylab import *

f = open('mmirszernfield.tab')

#Tkae care of the header
f.readline();
f.readline();

radArray = []
z1Array = []
z2Array =  []
z3Array = []
z4Array = []
z5Array = []
z6Array = []
z7Array = []
z8Array = []
z9Array = []
z10Array = []
z11Array = []

for line in f.readlines():
	rad, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11 = map(float, line.split())
 	
 	#fill arrays
 	radArray.append(rad)
 	z1Array.append(z1)
 	z2Array.append(z2)
 	z3Array.append(z3)
 	z4Array.append(z4)
 	z5Array.append(z5)
 	z6Array.append(z6)
 	z7Array.append(z7)
 	z8Array.append(z8)
 	z9Array.append(z9)
 	z10Array.append(z10)
 	z11Array.append(z11)

font = {'family' : 'fantasy',
        'weight' : 'normal',
        'size'   : 13}

rc('font', **font)
plot([0, 1], [0,0], '--k', linewidth=2)
z4plt = plot(radArray,z4Array,label="z4: focus", linewidth=3) 
plot(radArray,z5Array,label="z5 : astig", linewidth=3)
plot(radArray,z8Array, label="z8: coma", linewidth=3)
plot(radArray,z9Array, label="z9: trefoil", linewidth=3)
plot(radArray,z11Array, label="z11:spherical", linewidth=3)
xlabel("Off-axis Distance (deg)")
ylabel(u"Zernike Fringe Coefficient (\u03bcm)")
ylim(-0.25, 0.3)
xlim(0, 0.12)
legend(prop={'size':10})
savefig('mmirsOffAxis.png')

