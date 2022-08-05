import argparse
import numpy as np
from ctypes import CDLL,c_double
fc = CDLL('./fc/libFC.so')

psr = argparse.ArgumentParser()
psr.add_argument('--discri',dest="discriminate", nargs='+')
psr.add_argument('-o', dest="output")
psr.add_argument('-i', dest="input")
args = psr.parse_args()

m = 0.5*1000
M = 150
N_A=6.02
N_Atimes=23
T = 3
def sensi(sig, t):
    return m/M*N_A*t/sig
discrieffs = [float(i) for i in args.discriminate]
fcAvg = fc.fcAvg
fce = fc.fc
fcAvg.restype=c_double
fce.restype=c_double
with h5py.File(args.ipt, 'r') as ipt:
    originbkg = ipt['bkg']
bkgs = [originbkg*i for i in discrieffs]
signalAvg = [fcAvg(c_double(bkg)) for bkg in bkgs]
signalUl = [fce(c_double(bkg),c_double(0)) for bkg in bkgs]
sensiAvg = [sensi(sig,T) for sig in signalAvg]
sensiUl = [sensi(sig, T) for sig in signalUl]
print(bkgs)
print(signalAvg)
print(signalUl)
print(sensiAvg)
print(sensiUl)
with h5py.File(args.opt,'w') as opt:
    opt.create_dataset('sensiAvg', data=sensiAvg, compression='gzip')
    opt.create_dataset('sensiUl', data=sensiUl, compression='gzip')
    opt.create_dataset('discrieffs', data=discrieffs, compression='gzip')
