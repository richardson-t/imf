import imf
from imf.sampling import sample_mass
import pylab as pl

maxmass = [sample_mass(500, verbose=False, silent=True).max() for ii in
           range(10000)]
maxmass_sorted = [sample_mass(500, stop_criterion='sorted', verbose=False,
                                   silent=True).max() for ii in range(10000)]
maxmass_before = [sample_mass(500, stop_criterion='before', verbose=False,
                                   silent=True).max() for ii in range(10000)]
maxmass_after = [sample_mass(500, stop_criterion='after', verbose=False,
                                   silent=True).max() for ii in range(10000)]

pl.clf()
pl.hist(maxmass, bins=50, alpha=0.5, label='nearest', histtype='step')
pl.hist(maxmass_sorted, bins=50, alpha=0.5, label='sorted', histtype='step')
pl.hist(maxmass_before, bins=50, alpha=0.5, label='before', histtype='step')
pl.hist(maxmass_after, bins=50, alpha=0.5, label='after', histtype='step')
pl.legend(loc='best')
