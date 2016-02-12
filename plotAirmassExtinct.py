#!/usr/bin/python

from pylab import *
import sys
import math

def main(argv):

  wave = []
  extinct = []

  file = 'kpnoextinct.dat'
  f = open(file,'r')
  for line in f.readlines():
    if line[0] != '#':
     splitLines = map(float, line.strip().split())
     if len(splitLines) == 2:
      wave.append(splitLines[0])
      extinct.append(-2.5*math.log(splitLines[1],10))


  plot(wave, extinct)
  xlabel("Wavelength")
  ylabel("Extinction (mag/airmass)")
  xlim(3500, 8500)
  ylim(0, 3.5)

  font = {'family' : 'fantasy',
  "weight" : "normal",
  "size" : 13}

  rc("font", **font)
  rcParams['axes.linewidth']=5.0
  savefig('extinct.png')


if __name__ == "__main__":
  main(sys.argv)
