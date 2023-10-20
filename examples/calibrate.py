import numpy as np
try:
    import matk
except:
    try:
        sys.path.append(os.path.join('..', 'src'))
        import matk
    except ImportError as err:
        print('Unable to load MATK module: '+str(err))
from multiprocessing import freeze_support

def fv(a):
    a0 = a['a0']
    a1 = a['a1']
    a2 = a['a2']
    X = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12.])

    out = a0 / (1. + a1 * np.exp( X * a2))
    return out
    #obsnames = ['obs'+str(i) for i in range(1,len(out)+1)]
    #return dict(zip(obsnames,out))

def run():
    p = matk.matk(model=fv)
    p.add_par('a0', value=0.7, min=-2000., max=2000.)
    #p.add_par('a0', value=0.7)
    #p.add_par('a1', value=10., min=-2000., max=2000.)
    p.add_par('a1', value=10.)
    #p.add_par('a2', value=-0.4, min=-20000., max=20000.)
    p.add_par('a2', value=-0.4)
    #p.forward()
    p.obsvalues = [5.308,7.24,9.638,12.866,17.069,23.192,31.443,38.558,50.156,62.948,75.995,91.972]

    p.calibrate(cpus=6,verbose=True)

# Freeze support is necessary for multiprocessing on windows
if __name__== "__main__":
	freeze_support()
	run()
